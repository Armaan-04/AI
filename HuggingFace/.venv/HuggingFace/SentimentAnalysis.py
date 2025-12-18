from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis" , model = "distilbert-base-uncased-finetuned-sst-2-english")
texts = [
"I love playing and watching cricket!",
"I hate when Virat Kohli misses a century.",
"I love being a footballer."
]
results = sentiment_analyzer(texts)
for result in results:
    print(result)


