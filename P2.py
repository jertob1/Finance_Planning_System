from Investor import Investor
from fixed import Fixed
from growth import Growth

fileName = ""
def display_menu():
    
    while True: #Loops forever until a break statement
        print("\nWelcome to the finance planning system") #print out menu information 
        print("Enter an option from the menu")
        print("Enter 1 to exit the system")
        print("Enter 2 to read the database from the file")
        print("Enter 3 to print all records")

        CMD = input("Enter the option: ") #Prompts for user input.

        #Series of if statement for all the possible user inputs
        if CMD == "1":
            print("Exiting")
            break
        
        elif CMD == "2":
            fileName = input("Enter file name containing investor information: ") #prompts user for filename
            readFile(fileName) #The function readFile is called with the argument of the file that was just inputted
        elif CMD == "3":
            printAccounts(fileName)
        else:
            print("Wrong input, try again")
            

def readFile(Name):
   
    f1 = open(Name,"r") #instantiate f1 as a file, with the name passed, in read mode
    Investors =[] #Initialize a list to store objects 
    NumberofInvestor = 0 #initialize an int to count the # of object in list
    for line in f1: #loop through the amount of lines in the file
        name,typ,fixed,growth=line.split() #split through all the elements in the file and intialize them as variables

        if typ == "fixed": #if the type of investor is fixed"
            Investors.append(Fixed(name,float(fixed))) #Append an instance of a 'Fixed' object with the name and investment amount into the list of objects
        elif typ == "growth": #Same is done if the type of investor is growth, yet by creating a growth object
            Investors.append(Growth(name,float(growth)))

        NumberofInvestor +=1 #Number of investor increases by 1
        
    f1.close()#close the text file for security
    
    return Investors, NumberofInvestor #Return the list of objects and the amount of objects in the list

def printAccounts(Name):
    
    Investors, Counter = readFile(Name)#Using the list of objects and the amount of objects in the list as return values from the function readFiles
                                       #Hence, readFile has the same argument as the user input for the file previously
    print("Printing all records.........\n")
    print("{:<8} {:<10} {:>10}".format("Name", "type", "investment($)")) #Print the header of the collumns with formatting

    for i in range(Counter): #Looping through the range of Counter which tells us how many objects there are in the list
        print(Investors[i]) #We can just print each object from the list because this calls their respective __str__ functions
    
#Execute only if module is main
if __name__ == "__main__":
    display_menu()
