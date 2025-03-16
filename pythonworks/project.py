import sys
import os
# Check the availability of these come colors 
Colors =  ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]


def AddColor(AmendData):
    #AmendData = input("Insert new color")
    if(AmendData != " "):
        if AmendData in Colors:
            print(f"{AmendData } already exists!")
        CertainToAdd = input(f"Do you want to add {AmendData} to the Database? Y/N > ")
        if(CertainToAdd.upper() == "Y"):
            Colors.append(AmendData)
            print("\n")
            print(f" Color {AmendData} added Successfully!\n")
            print("Choose option 4 to see updated Database!") 
        else:
            print(f"Adding color {AmendData} was unsuccessful!")
            

def AddGenColor():
    AmendData = input("Insert new color > ")
    if(AmendData != " "):
        CertainToAdd = input(f"Do you want to add {AmendData} to the Database? Y/N > ")
        if(CertainToAdd.upper() == "Y"):
            Colors.append(AmendData)
            print(f" Color {AmendData} added Successfully !")
        else:
            print(f"Adding color {AmendData} was unsuccessful!")


def DeleteColor():
    Delete_Data = input("Type color to delete > ")
    if(Delete_Data != " "):
        if(Delete_Data in Colors):
            CertainToDelete = input(f"Do you want to delete {Delete_Data}? Y/N? > " )            
            if(CertainToDelete.upper() == "Y"):
                Colors.remove(Delete_Data) 
                print(f"Deleted Color {Delete_Data} successfully!")
            else:
                print(f"Deleting Color {Delete_Data} unsuccessful")
        else:
            print(f"No color Name \"{Delete_Data}\" found in Data!")


def DeleteAllColors():
    DeleteAll = input("Are you sure you want to delete all Database? Y/N >")
    if(DeleteAll.upper() == "Y"):
        UserPassword = input("Enter Password >")
        if(UserPassword == Password):
            for allcolors in Colors:
                Colors.clear()
                print(f"Deleted {allcolors} successfully!")
        else:
            print("Incorrect password!\n Failed to Delete Data!")
            print("Contact Admin to make changes!")
            
         

Password = None
Tries = 0

while(Password == None):
    print("\n")
    print("*" * 4 + "WELCOME TO THE COLOR DATABASE" + "*"*4)
    print("\n")
#Setting password
    DataBasePassword = input("Set Database password > ")
    ConfirmPassword = input("Confirm password >")

    if((DataBasePassword == ConfirmPassword)):
        Password = DataBasePassword
        print("Password set successfully!")
    else:
        print("password missmatch!\n Re-enter password to continue")
        print
    



while (Tries < 4):
    UserInitiate = int(input("""
                             choose an option below;

            1. Search for Color > 
            2. Add color to Database > 
            3. Delete Color from Database > 
            4. Display DataBase > 
            5. To quit the application >        
    """))
    match UserInitiate:
        case 1:
            Take_color = input("Search for color > ")
            Condition = Take_color.strip() in Colors
            print(Condition)
            if (Condition):
                print(f"The color {Take_color} is present!")
            else:
                print(f"The color {Take_color} is not in the Database!")
                WantoAdd = input(f"Will you want to add {Take_color} To the DataBase? Y/N > ")
                if(WantoAdd.upper() == "Y"):
                      AddColor(Take_color)
    #CASE 2 FOR ADDING COLOR TO DATABASE
        case 2:
            AddGenColor()
     #CASE 3 FOR DELETING DATA FROM THE DATA BASE
        case 3:
            whichDelete = int(input("""
                          1. Delete a color
                          2. Delete all color Data
                            """))
            if(whichDelete == 1):
                DeleteColor()
            elif(whichDelete == 2):
                DeleteAllColors()
            else:
                print("input unmatched!")     
     #CASE 4 FOR DISPLAYING ALL DATA BASE CONTENT
        case 4:
            print(f"The database has a total of {len(Colors)} items which are;")
            print(Colors)
        case 5:
            CertaintoQuit = input("Are you sure you want to quit? Y/N > ")
            if(CertaintoQuit.upper() == "Y"):
                print("Thanks for using the Color Database")
                os._exit(0)
                sys.exit()
            else:
                print("You are still in the Database!")
        case _:
                print("Invalid input! please try again")
                #CASE 1 FOR SEARCHING THROUGH FOR A COLOR
           
        
    
    
