import random

while 1==1:
    # prompt for a question
    question = input("Ask the magic 8 ball a question: (press enter to quit)\n")

    if not question: 
        break
    print(random.choice(("It is certain", "Outlook good", "You may rely on it", "ehh ask again", "Concentrate and ask again",  "Reply hazy, try again sucker", "My reply is no way","My sources say no")),"\n")