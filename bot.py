import json
from fuzzywuzzy import process
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters
import wikipediaapi
import wikipedia

# Wikipedia API'ye bağlanırken user_agent parametresi ekleyelim (wikipedia-api kütüphanesi)
wiki_wiki = wikipediaapi.Wikipedia(
    language='tr', 
    user_agent="MyChatBot/1.0 (https://example.com)"
)

# Wikipedia API - wikipedia-api kütüphanesi ile bilgi arama
def wiki_ara_wikipediaapi(sorgu):
    page = wiki_wiki.page(sorgu)
    if not page.exists():
        return "Bu konuda bilgi bulunamadı."
    return page.summary[:500]  # İlk 500 karakteri döndürüyoruz

# Wikipedia API - wikipedia kütüphanesi ile bilgi arama
wikipedia.set_lang("tr")

def wiki_ara_wikipedia(sorgu):
    try:
        sonuc = wikipedia.summary(sorgu, sentences=2)
        return sonuc
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Bu konuda birden fazla sonuç var: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "Bu konuda bilgi bulunamadı."
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

# Veri setini yükleme fonksiyonu
def load_dataset(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

# Veri setine yeni bir soru-cevap ekleme fonksiyonu
def add_to_dataset(soru, cevap, filename):
    with open(filename, "a", encoding="utf-8") as f:
        new_entry = {"soru": soru, "cevap": cevap}
        json.dump(new_entry, f, ensure_ascii=False)
        f.write("\n")

# En iyi eşleşen cevabı bulma fonksiyonu
def get_best_response(user_input, dataset):
    sorular = [entry["soru"] for entry in dataset]
    en_iyi_eslesme, benzerlik_orani = process.extractOne(user_input, sorular)

    if benzerlik_orani > 80:  # Eşik değer (20 ve üstü olursa kabul ediyoruz)
        for entry in dataset:
            if entry["soru"] == en_iyi_eslesme:
                return entry["cevap"]

    return "Bunu bilmiyorum! Bana öğretmek ister misin? (Evet/Hayır)"

# /start komutu ile kullanıcıya hoş geldin mesajı
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("ML-GPT'ye Hoş Geldin!")

# Mesajlara yanıt veren fonksiyon
async def respond(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    dataset = load_dataset("dataset.jsonl")
    
    if user_input.lower() == "çık":
        await update.message.reply_text("Bot: Görüşürüz kanka! 🚀")
    elif user_input.lower() == "evet":
        await update.message.reply_text("Bana öğretmek istediğin soruyu ve cevabını yaz.")
        # Sonraki adıma geçmek için durdurulabilir bir süreç ekleyebiliriz (state management)
    elif user_input.lower() == "hayır":
        await update.message.reply_text("Tamam, başka bir zaman konuşuruz.")
    elif user_input.lower().startswith("wiki "):  # Wikipedia araması için kontrol
        sorgu = user_input[5:]  # 'wiki ' kısmını çıkar
        wiki_sonuc = wiki_ara_wikipediaapi(sorgu)  # Wikipedia API - wikipedia-api kütüphanesi
        # Eğer hata alırsak wikipedia kütüphanesini de kullanabilirsin:
        if wiki_sonuc == "Bu konuda bilgi bulunamadı.":
            wiki_sonuc = wiki_ara_wikipedia(sorgu)  # Wikipedia API - wikipedia kütüphanesi
        await update.message.reply_text(f"🔎 Wikipedia: {wiki_sonuc}")
    else:
        response = get_best_response(user_input, dataset)
        await update.message.reply_text(response)

# Telegram Botunun ana fonksiyonu
def main():
    # Telegram bot tokenınızı buraya girin
    application = Application.builder().token("********---TELEGRAM---TOKEN---******").build()

    # Komut ve mesaj handler'larını ekleyin
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

    # Botu başlatın
    application.run_polling()

if __name__ == "__main__":
    main()
