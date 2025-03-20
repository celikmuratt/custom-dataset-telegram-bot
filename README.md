# Telegram Chatbot with Custom Dataset

This project is a Telegram chatbot that uses a custom dataset to provide answers to user queries. The bot is capable of responding to specific questions based on the dataset and can also fetch data from Wikipedia when requested.

## Features
- AI-powered chatbot that answers based on a custom dataset.
- Users can teach the bot by adding new question-answer pairs to the dataset.
- Wikipedia search integration using `/wiki` command to fetch data.
- Easy to set up and use.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your Telegram bot token to `bot.py`. Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual token:
    ```python
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    ```

4. Add your custom dataset in the `dataset.jsonl` file. For example:
    ```json
    {"soru": "selam", "cevap": "Selam! Naber?"}
    ```

5. Run the bot:
    ```bash
    python bot.py
    ```

## Usage
- To teach the bot, simply add new question-answer pairs to `dataset.jsonl`.
- To search Wikipedia, use the `/wiki <query>` command. The bot will fetch the result from Wikipedia.

## License
This project is open source and available under the MIT License.



# Telegram Chatbot Özelleştirilmiş Veri Kümesi ile

Bu proje, özelleştirilmiş bir veri kümesiyle çalışan bir Telegram sohbet botudur. Bot, kullanıcıların sorularına veri kümesine dayalı olarak yanıt verir ve ayrıca Wikipedia'dan veri çekebilir.

## Özellikler
- Özelleştirilmiş veri kümesine dayalı olarak cevap veren AI destekli sohbet botu.
- Kullanıcılar, yeni soru-cevap çiftleri ekleyerek botu öğretebilirler.
- Wikipedia araması yapabilen `/wiki` komutu ile entegrasyon.
- Kurulumu ve kullanımı kolay.

## Kurulum

1. Repository'i klonlayın:
    ```bash
    git clone https://github.com/kullanici-adi/repo-adi.git
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3. `bot.py` dosyasındaki Telegram bot tokeninizi ekleyin. `YOUR_TELEGRAM_BOT_TOKEN` kısmını gerçek tokeninizle değiştirin:
    ```python
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    ```

4. `dataset.jsonl` dosyasına özelleştirilmiş veri kümenizi ekleyin. Örneğin:
    ```json
    {"soru": "selam", "cevap": "Selam! Naber?"}
    ```

5. Botu çalıştırın:
    ```bash
    python bot.py
    ```

## Kullanım
- Botu öğretmek için, `dataset.jsonl` dosyasına yeni soru-cevap çiftleri ekleyebilirsiniz.
- Wikipedia araması yapmak için `/wiki <sorgu>` komutunu kullanabilirsiniz. Bot, Wikipedia'dan sonuçları çekecektir.

## Lisans
Bu proje açık kaynaklıdır ve MIT Lisansı altında kullanılabilir.
