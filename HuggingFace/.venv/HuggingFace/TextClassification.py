from transformers import pipeline

#Load the spam detection pipeline
spam_classifier = pipeline("text-classification" , model = "philschmid/distilbert-base-multilingual-cased-sentiment")

texts = ["Congrats! you've won a 500 INR amazon gift card. Click here to claim now." ,
         "Hi Armaan , let's have a meeting tomorrow at 12pm." ,
         "URGENT: your gmail account has been compromised.Click here to secure it."]

results = spam_classifier(texts)

label_mapping = {'negative':'SPAM' , 'neutral' : 'NOT SPAM' , 'positive' : 'NOT SPAM'}

for result in results:
    label = label_mapping[result['label']] #Map the label
    score = result['score']
    print(f"Label: {label} , Confidence: {score:.4f}")