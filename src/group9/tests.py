from django.test import TestCase

# Create your tests here.

import requests

file1 = open('myfile.txt', 'w')

url = "https://copilot5.p.rapidapi.com/copilot"
headers = {
		# "x-rapidapi-key": "a1624a25b5msh1f36c4aceaa8785p14227fjsn62184a93f3e1",
        "x-rapidapi-key": "268c5c6764msh8b0e940848158ccp17ce16jsne4595e391148",
		"x-rapidapi-host": "copilot5.p.rapidapi.com",
		"Content-Type": "application/json"
	}
# title = ""
essay = ""

correction = "Please correct my essay, Just give me the correct essay!!\nthis is my essay: \n" + essay


def gpt_questions(message):
	payload = {
		"message": message,
		"conversation_id": None,
		"tone": "BALANCED",
		"markdown": False,
		"photo_url": None
	}
	
	response = requests.post(url, json=payload, headers=headers)
	res = response.json()
	# print(res)
	return str(res['data']['message'])

def clean_result(result):
    lines = result.split('\n')
    new_res = []
    for i in range(len(lines)):
        if "certainly" in lines[i].lower():
            continue 
        if "feel free" in lines[i].lower():
             break
        new_res.append(lines[i])
   
    res = '\n'.join(new_res)
    res = res.strip()
    res = res.replace('"','')
    return res

def recommend_title(title):
    subject_suggestion =  "give me 4 title about " + title + " for essay in this format -> title1: , title2: , title3: \n Be sure to follow the format!!"
    result = gpt_questions(subject_suggestion)
    res = clean_result(result)

    return res
	

def analysis_essay(essay):
    analysis = "Tell me the exact number of mistakes in my essay\n such as Grammar mistake and Spelling mistake or ...\nand specify the exact type of grammars that is incorrect. in this format -> grammar1. Simple present, grammar2. Simple past, grammar3. Present perfect, grammar4. Future simple	and ... \nBe sure to follow the format!!\nthis is my essay: \n" + essay
    result = gpt_questions(analysis)
    res = clean_result(result)
    return res
    



# res = analysis_essay("i have went to the school next day and i have quiz but i am not reading about my quize so i dont what to do")
# print(res)
