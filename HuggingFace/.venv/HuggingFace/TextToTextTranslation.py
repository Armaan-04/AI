from transformers import T5ForConditionalGeneration, T5Tokenizer

# Use "google/flan-t5-base" instead of just "t5-base"
model_name = 'google/flan-t5-base'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

input_text = "translate English to Spanish: My name is Armaan Alam, and I love football."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids, max_length=50)
translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Translated text:", translated_text)