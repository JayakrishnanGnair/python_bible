known_users = ["Jay","Ais","Ana","Kris"]
print(len(known_users))
while True:
    print("Hi!!My name is travis")
    name = input("What is your name?").strip().capitalize()
    if(name in(known_users)):
        print("Hello {}!".format(name))
        remove  = input("Would you like to be removed(Y/N)?").strip().lower()
        if remove =="y":
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("Good!!! I didn't want you to leave anyway.")
    else:
        print("Hmmm!! I don't think I have met you yet {}".format(name))
        add_name = input("Would you like to be added to the system(y/n)?").strip().lower()
        if add_name == "y":
            known_users.append(name.capitalize())
            print(known_users)
        elif add_name == "n":
            print("No worries!! see you around!!")
            

            
        
        
        

    
    
    
    
