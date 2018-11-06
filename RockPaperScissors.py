import random
def check(choice):
    dic = ("rock","paper","scissors")
    cpu = random.randint(0,2)
    cpuChoice = dic[cpu]
    if choice == "rock":
        if cpuChoice == "rock":
            print ("Tie")
        if cpuChoice == "paper":
            print ("You lose! Computer chose paper!")
        if cpuChoice == "scissors":
            print ("You win! Computer chose scissors!")
    if choice == "paper":
        if cpuChoice == "rock":
            print ("You win! Computer chose rock!")
        if cpuChoice == "paper":
            print ("Tie")
        if cpuChoice == "scissors":
            print ("You lose! Computer chose scissors!")
    if choice == "scissors":
        if cpuChoice == "rock":
            print ("You lose! Computer chose rock!")
        if cpuChoice == "scissors":
            print ("Tie")
        if cpuChoice == "paper":
            print ("You win! Computer chose paper!")
    process()

def process():
    x = input("Rock? Paper? Or Scissors?")
    check(x)


print ("Welcome to Rock Paper Scissors 2.0")
process()