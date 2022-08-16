import random

while 1==1:
    # prompt for a question
    question = input("Ask the magic 8 ball a question: (press enter to quit)\n")

    if not question: 
        break
    print(random.choice(("It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again",  "Reply hazy, try again", "My reply is no","My sources say no")),"\n")