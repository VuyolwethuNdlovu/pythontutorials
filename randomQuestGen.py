"""

Random Question Generator Tutorial
Created by Vuyolwethu Ndlovu
"""

# We import random to access the pre-written functions that allows to generate random numbers
import random


def startGenerator(userStart):

    # This function loops through the lists of questions and picks 20 random questions

    if userStart == "yes":
        print("Yay")

        for x in range (0,20):
            n = random.randint(0,limit)
            print(questions[n])


            # The user can exit this loop if they say no which will trigger the function
            # def terminateNextQuestion that stops the porgram

            userNext = input("Do you wish to go to the next question")
            termianteNextQuestion(userNext)

        # When all 20 questions have been printed, the program will end
        print("end of program")
        exit()






def termianteNextQuestion(userNext):
    if userNext == "no":
        print("end of program")
        exit()




questions= ["What is your full name?", "What does your name mean?",
                "If you had to change your first name, what would you change it to?",
                "Where are you from?", "Where were you born?", "Where did you grow up?"
                , "What are your best characteristics?", "Which of your parents are you more like?",
                "What is your biggest accomplishment?", "What is your biggest fear?", "What inspires you?"
                , "What is the most important thing in your life?"
                , "What has required the most courage of you in your life so far?"
                , "Who’s your favorite person in the world?", "What is your favorite music genre?"
                , "What is your favorite childhood memory?", "What is your favorite song?"
                , "What is your favorite holiday destination?"
                , "What is your favorite way to pass time?"
                , "What is your all-time favorite town or city? Why?"
                , "What is your favorite social media channel?"
                , "Where’s your favorite place to take an out-of-town guest?"
                , "What was your favorite subject in High School?"
                , "What was your favorite TV show when you were a child?"
                , "Are you high maintenance?", "Are you more inclined to “build your own empire” or unleash the potential of others?",
                "Are you a fan of any sports team?", "Are you a good cook?"
                , "If you had more courage what would you do differently in your life now?"
                , "If you could eliminate one weakness or limitation in your life, what would it be?"
                , "Who has left the most impact on your life?", "Who is the best teacher you’ve ever had?"
                , "Who is the first person you call when something exciting happens?"
                , "Can you dance?", "Do you have a catchphrase?","Do you have a tattoo?",
                "Do you have a whole lot of acquaintances or just a few very close friends? Why?",
                "Who sent the last text message you received?","Who was your first Celebrity crush?",
                "What is something that amazes you?", "What is at the top of your bucket list?",
                "What scares you about aging?","How has your birth order/characteristics of siblings affected you?",
                "Would you ever consider living abroad?", "What is the worst grade you got on a test?",
                "What is the first movie you remember seeing?","What is the first thing you do when you get home?",
                "What kind of books do you like to read?","What is the last book you read?",
                "What piece of technology can you not live without?"]

# the variable limit stores the amount of elements in the list
limit= len(questions)

userStart = input("Do you wish to start?")

# this call to the function startGenerator will start the generation of questions
startGenerator(userStart)


# print(limit)





