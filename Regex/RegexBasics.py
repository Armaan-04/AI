import re

text = '''The emergency contact for Project Delta-9 is (555) 123-4567, but only after 2:30 PM.
Before then, please dial +1-800-987-6543 and ask for extension #40B. 
We collected $3,875.50 in donations, which is 10% more than the target goal of $3,500.00!
The data set, labeled D@t@_s3t_V1.1_final.xlsx, confirmed that 7 out of 12 variables met the >99.9% criteria.
Remember to use the secure password: P@sswOrd!2025? when accessing the server at http://secure.data.net.'''

pattern = '(\(\d{3}\) \d{3}-\d{4})'
match = re.findall(pattern , text)
print(match)


text2 = "dfdnq;dqw;ewed;qwqf-qed"

pattern2 = '[^;-]'
match2 = re.findall(pattern2 , text2)
print(match2)


text2 = "dfdnq;dqw;ewed;qwqf-qed"

pattern3 = 'labeled [^\n]*'
match3 = re.findall(pattern3 , text)
print(match3)


#re.search -> finds the first occurence

text4 = 'codebasics: you ask lot of questions 😡 12345678912, abc@xyz.com'
text5= 'codebasics: here it is: (123)-567-8912, abc@xyz.com'
text6 = 'codebasics: yes, phone: 12345678912 email: abc@xyz.com'

pattern4 = '\d{11}'
match4 = re.findall(pattern4 , text4)
print(match4)

pattern5 = '\(\d{3}\)-\d{3}-\d{4}'
match5 = re.findall(pattern5 , text5)
print(match5)

pattern6 = '[a-z0-9A-Z_]*@[a-z0-9A-Z]*\.[a-zA-Z]*'
match6 = re.findall(pattern6 , text6 )
print(match6)


text7 = 'codebasics: Hello, I am having an issue with my order # 412889912'
text8='codebasics: I have a problem with my order number 4889912'
text9='codebasics: My order 4129912 is having an issue, I was charged 300$ when online it says 280$'

pattern7 = 'order[^\d]*(\d*)'  #^\d means match everything which is not a digit.
match7 = re.findall(pattern7 , text7)
print(match7)