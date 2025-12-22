from transformers import AutoModelForSeq2SeqLM , AutoTokenizer

#Load pretrained model and tokenizer
model_name = "facebook/bart-large-cnn" #Example model for summarization
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#Input text to summarize
text = '''Lionel Messi, often hailed as the greatest footballer of all time, is an Argentine
         legend renowned for his extraordinary vision, dribbling, and prolific goal-scoring.
         Over his iconic 17-season career at FC Barcelona, he won 10 La Liga titles and four
         Champions Leagues before moving to PSG and eventually to Inter Miami in the US. On the
         international stage, he cemented his legacy by leading Argentina to a historic triple
         crown: the 2021 Copa América, the 2022 FIFA World Cup, and the 2024 Copa América. Now
         playing in the MLS, he continues to dominate, recently winning the 2025 MLS Cup and securing
         back-to-back league MVP awards. With a record eight Ballon d’Or trophies and over 800 career
         goals, La Pulga remains a global symbol of excellence and perseverance.'''

#Tokenize the input text
inputs = tokenizer.encode("summarize: " + text , return_tensors = "pt" ,max_length=512 , truncation=True) #max_length is the maximum number of tokens in the summary

#Generate the summary
summary_ids = model.generate(inputs , max_length=50, min_length=25 , length_penalty = 2.0 , num_beams = 4 , early_stopping = True)
#length_penalty encourages longer or shorter summarys
#num_beams controls the beam search width , higher values improve quality but slows down frames
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(summary)