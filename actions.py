# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Sazida Hossain"
my_age = 22
my_bio = ""
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    userinput = input("Would you like to:\n1) Create a new club.\nor:\n2) Browse and join clubs.\nor:\n3) View existing clubs.\nor:\n4) Display members of a club.\nor:\n-1) Close application.\n")
    if int(userinput)==1:
        return "create club"
    elif int(userinput)==2:
        return "join clubs"
    elif int(userinput)==3:
        view_clubs()
        print("\n")
        application()
    elif int(userinput)==4:
        return "view members"
    elif int(userinput)==-1:
        print("Logged out")
    else:
        print("Your input was invalid. Please try again:")
        application()


def create_club():
    # your code goes here!
    userinputx=input("Pick a new name for your awesome new club: ")
    userinputy=input("What is your club about?\n")
    clubx = Club(userinputx,userinputy)
    clubx.recruit_member(myself)
    clubx.assign_president(myself)
    counter=1
    for i in population:
        counter=counter+1
    counterx=1
    print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):")
    for i in population:
        print ("["+str(counterx)+"]"+ i.name)
        counterx=counterx+1
    userinputl=input()
    while(int(userinputl)!=-1):
        if int(userinputl) in range(0,len(population)):
            if int(userinputl)<=counter and population[int(userinputl)-1] not in clubx.people:
                clubx.recruit_member(population[int(userinputl)-1])
            elif population[int(userinputl)-1] in clubx.people:
                print(population[int(userinputl)-1].name+" is already in club")
        else:
            print("Invalid input! Please try again")
        userinputl = input()
    clubs.append(clubx)
    print("Here's your club:")
    print("Club Name: "+clubx.name)
    print("Club Description: "+clubx.description+"\nClub members list:")
    clubx.print_member_list()
    print("\n")
    application()
def view_clubs():
    # your code goes here!
    for i in clubs:
        print("NAME: "+i.name+"\nDescription: "+i.description+"\nMEMBERS:"+str(len(i.people))+"\n")


def view_club_members():
    # your code goes here!
    view_clubs()
    userinputf = input("Please Enter the name of the club whose members you would like to see:\n")
    counter=0
    for i in clubs:
        if i.name.lower()==userinputf.lower():
           x=i
           counter=1
    if counter==1:
        x.print_member_list()
    else:
        print("Please try again:")
        view_club_members()
    print("\n")
    application()
def join_clubs():
    # your code goes here!
    view_clubs()
    print("Enter the name of the club you'd like to join:")
    userinputm=input()
    counter=0
    for i in clubs:
        if i.name.lower()==userinputm.lower():
           x=i
           counter=1
    if counter==1 and myself not in x.people:
        x.people.append(myself)
        print(myself.name + " just joined " + x.name + ".")
    elif counter!=1:
        print("Your input was invalid. Please try again!\n")
        join_clubs()
    elif myself in x.people:
        print("You are already in this club.")
    print("\n")
    application()
def application():
    introduction()
    # your code goes here!

    m=options()
    if m=="create club":
        create_club()
    elif m=="join clubs":
        join_clubs()
    elif m=="view members":
        view_club_members()
