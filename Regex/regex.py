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


