from google.cloud import language

def get_sentiment(in_text):
    language_client = language.Client()
    document = language_client.document_from_text(in_text)
    sentiment = document.analyze_sentiment().sentiment

if __name__ == '__main__':
    language_client = language.Client()
    text= 'Ya boobay!'
    document = language_client.document_from_text(text)
    sentiment = document.analyze_sentiment().sentiment
    print(f'Sentiment: {sentiment.score}, {sentiment.magnitude}')
