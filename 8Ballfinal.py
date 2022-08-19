import http.client
import random
import sys
import json

 #credit to figlet and termcolor documentation
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('MAGIC 8 BALL!', font='starwars'),
       'yellow', attrs=['bold'])
conn = http.client.HTTPSConnection("magic-8-ball1.p.rapidapi.com") #credit to magic 8 ball documentation

headers = {'X-RapidAPI-Key': "7bf30cb820msh711ff8544fffe8fp1e7edcjsn5a63168314fa",'X-RapidAPI-Host': "magic-8-ball1.p.rapidapi.com"}

def main():
    
    print('')
    print('Hello World, I am the Magic 8 Ball, What is your name?')
    name = input()
    print('hello ' + name)

    print('Ask me a question.')
    input()

    conn.request("GET", "/my_answer/?question=I%20will%20succeed%20%3F", headers=headers)

    res = conn.getresponse()
    data = res.read()

    answer = (data.decode("utf-8"))
    answer = json.loads(answer) #credit to Chad
    
    print("Hmmm..... Thinking")
    print (answer["answer"])

main()


