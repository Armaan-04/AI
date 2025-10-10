import re

text1 = '''Born	Elon Reeve Musk
June 28, 1971 (age 54)
Pretoria, South Africa
Citizenship	
South Africa
Canada
United States
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)'''

pattern1 = 'age (\d+)' # + means one or more of that character
match1 = re.findall(pattern1 , text1)
print(match1)

pattern2 = 'Born(.*)'  # * means zero or more characters
match2 = re.findall(pattern2 , text1)
output = match2[0].strip() #[0] giving access to the first element of the string
print(output)

pattern3 = 'Born.*\n(.*)\(age'
match3 = re.findall(pattern3 , text1)
print(match3)

pattern4 = '\(age.*\n(.*)'
match4 = re.findall(pattern4 , text1)
print(match4)

def get_pattern_match(pattern, text):
    matches = re.findall(pattern , text)
    if matches:
        return matches[0]
    
def get_personal_information(text1):
    age = get_pattern_match('age (\d+)' , text1)
    full_name = get_pattern_match('Born(.*)' , text1)
    birth_date = get_pattern_match('Born.*\n(.*)\(age' , text1)
    birth_place = get_pattern_match('\(age.*\n(.*)' , text1)

    return {
        'age': int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()     
    }
    
print(get_personal_information(text1))