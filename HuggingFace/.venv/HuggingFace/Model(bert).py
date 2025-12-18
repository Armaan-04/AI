from transformers  import AutoModel , AutoTokenizer

#Download the model and tokenizer
model_name = 'bert-base-uncased' #downloading a pretrained bert model
model = AutoModel.from_pretrained(model_name) #from_pretrained is a method which downloads the model weights,configuration and tokenizer from the hugging face hub
tokenizer = AutoTokenizer.from_pretrained(model_name)

#Use the model and tokenizer
inputs = tokenizer("Hello , Hugging Face!" , return_tensors="pt")
outputs = model(**inputs)
print(outputs.last_hidden_state.shape) #example output shape

'''output: [1 , 7 , 768]
1 is the batch size
7 is the sequence length (tokenized version of "Hello , Hugging Face!")
768 is the hidden size each token is represented as a 768 dimensional vector standard for Bert's base architecture.'''

