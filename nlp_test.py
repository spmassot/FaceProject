from google.cloud import language

if __name__ == '__main__':
    language_client = language.Client()
    text= 'Ya boobay!'
    document = language_client.document_from_text(text)
    sentiment = document.analyze_sentiment().sentiment
    print(f'Sentiment: {sentiment.score}, {sentiment.magnitude}')
