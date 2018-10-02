# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name=name
        self.bio=bio
        self.age=age



class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name=name
        self.description=description
        self.people=[]


    def assign_president(self, person):
        # your code goes here!
        president=person
        return president

    def recruit_member(self, person):
        # your code goes here!
        self.people.append(person)

    def print_member_list(self):
        # your code goes here!
        counter=1
        for i in self.people:
            if counter==1:
                print("- "+i.name+" ("+str(i.age)+", President) - "+i.bio)
            else:
                print("- "+i.name+" ("+str(i.age)+") - "+i.bio)
            counter = counter+1
        counter=1
