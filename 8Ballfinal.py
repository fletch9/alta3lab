"""Magic 8 Ball with ASCII text header | eric.fletcher@tlgcohort.com"""

#loads modules for code to function
import http.client #loads HTTP modules for API pull
import sys
import json

 #credit to figlet and termcolor documentation
from termcolor import cprint 
from pyfiglet import figlet_format

#ASCII text generator
cprint(figlet_format('MAGIC 8 BALL!', font='starwars'),
       'yellow', attrs=['bold'])

#connection to API for random answers
conn = http.client.HTTPSConnection("magic-8-ball1.p.rapidapi.com") #credit to magic 8 ball documentation

#API key to access the API
headers = {'X-RapidAPI-Key': "7bf30cb820msh711ff8544fffe8fp1e7edcjsn5a63168314fa",'X-RapidAPI-Host': "magic-8-ball1.p.rapidapi.com"}


#user interface script
def main():
    
    print('')
    print('Hello, I am the Magic 8 Ball, What is your name?')
    name = input()
    print('hello ' + name)

    print('Ask me a question.')
    input()
    print("Hmmm..... Thinking")

#getting response from API site to question

    conn.request("GET", "/my_answer/?question=I%20will%20succeed%20%3F", headers=headers)

    res = conn.getresponse()
    data = res.read()

    answer = (data.decode("utf-8"))
    answer = json.loads(answer) #credit to Chad
    
   
    print (answer["answer"])

main()


