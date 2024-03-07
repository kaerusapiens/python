#gcloud auth application-default login
from google.cloud import translate_v2

def translate_text(text, target_language='ko'):
    # Instantiates a client
    translate_client = translate_v2.Client()

    # Translates the text into the target language
    translation = translate_client.translate(
        text,
        target_language=target_language
    )

    return translation['translatedText']

if __name__ == '__main__':
    english_text = input("Enter the English text to translate: ")
    translated_text = translate_text(english_text)
    print(f"Translated text: {translated_text}")
