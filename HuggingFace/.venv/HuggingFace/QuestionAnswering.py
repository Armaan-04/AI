from transformers import AutoModelForQuestionAnswering , AutoTokenizer

model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

context = '''Lionel Messi, often hailed as the greatest footballer of all time, is an Argentine
         legend renowned for his extraordinary vision, dribbling, and prolific goal-scoring.
         Over his iconic 17-season career at FC Barcelona, he won 10 La Liga titles and four
         Champions Leagues before moving to PSG and eventually to Inter Miami in the US. On the
         international stage, he cemented his legacy by leading Argentina to a historic triple
         crown: the 2021 Copa América, the 2022 FIFA World Cup, and the 2024 Copa América. Now
         playing in the MLS, he continues to dominate, recently winning the 2025 MLS Cup and securing
         back-to-back league MVP awards. With a record eight Ballon d’Or trophies and over 800 career
         goals, La Pulga remains a global symbol of excellence and perseverance.'''

question = "How many Ballon d'Or trophies did Lionel Messi win?"

inputs = tokenizer(question , context , return_tensors="pt")
outputs = model(**inputs)

#Extract the start and end scores
start_scores = outputs.start_logits
end_scores = outputs.end_logits

#Get the most likely start and end positions
start_index = start_scores.argmax()
end_index = end_scores.argmax()

#Convert token IDs back to words
answer_tokens = inputs["input_ids"][0][start_index : end_index + 1]
answer = tokenizer.decode(answer_tokens , skip_special_tokens=True)

print(f"Answer: {answer}")
