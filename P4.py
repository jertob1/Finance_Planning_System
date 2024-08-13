from Investor import Investor
from fixed import Fixed
from growth import Growth
import random
fileName = ""
def display_menu():
    
    while True: #Loops forever until a break statement
        print("\nWelcome to the finance planning system") #print out menu information 
        print("Enter an option from the menu")
        print("Enter 1 to exit the system")
        print("Enter 2 to read the database from the file")
        print("Enter 3 to print all records")
        print("Enter 4 to update investment for investors (!! A database should be read before any updates)")
        print("Enter 5 to print the amount made by each investor in a year (!! A database should be read before printing return investments)")


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
            
        elif CMD == "4":
            investmentName = input("Enter the transaction file: ")
            investment_update(investmentName,fileName)

        elif CMD =="5":
            amountMade(fileName)
            
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

def investment_update(tranName,invName):
    #Write inside a new file to prepapre the output of transaction
    NewFile = open("UpdateTrans.txt", "a")
    NewFile.write("Update Summary\n------------------------------------\n")
    NewFile.write("{:<10} {:>15} {:>20}\n".format("Name", "Update amount", "New Investment"))

    #Print statement again for update summary. Unfortunately, cannot simply print the content of the ouput file into IDLE
    #   because assignment asks that all updates should be listed in the same output file
    print("Update Summary\n------------------------------------")
    print("{:<10} {:>15} {:>20}".format("Name", "Update amount", "New Investment"))    

    
    f1 = open(tranName,"r")#open the file for transaction
    Investors, Counter = readFile(invName)#Instantiate Investors and Counter to be used in later loops 


    #Using nested loops as a search algorithm to find matching name of investors who are making a transaction
    for line in f1: #loop through the transaction text
        name,amount=line.split()#split the name and the amount and store into local var
        amount = float(amount)#Need to make amount into float to store later
        for i in range(Counter): #loop through the Investor list
            if Investors[i].get_name() == name: #if the name of the object in Investor equals the name read in transaction.txt
               Investors[i].updateInvestment(amount)#Then, we update the investment using amount and functions from fixed and growth 

               #Prepare string that will be written into new file. Contains name, update amount, and New investment. 
               formatted_string = "{:<10} {:>15} {:>20}\n".format(name, "${:.2f}".format(amount), "${:.2f}".format(Investors[i].get_both()))
               #In the above line, I get the new investment by calling a get function that calls either the fixed or growth investment. I kinda had to cheat my way through it here.
               NewFile.write(formatted_string)#write in file

               print("{:<10} {:>15} {:>20}".format(name, "${:.2f}".format(amount), "${:.2f}".format(Investors[i].get_both())))
               
    NewFile.write("\n")
    NewFile.close()
    f1.close()#close the text file for security

def amountMade(Name):

    Investors, Counter = readFile(Name)#Instantiate list of objects and amount of objects to loop through
    print("{:<10} {:>10} {:>15} {:>15}".format("Name","Rate", "Investment", "Return")) #print headers with formating    

    for i in range(Counter): #loop through # of investors

        if str(type(Investors[i])) == "<class 'fixed.Fixed'>": #if an investor is fixed
            returnInv = Investors[i].GetInvestmentReturn() #Compute his return investement by calling a method on the object from Fixed
            print("{:<10} {:>10} {:>15} {:>15}".format(Investors[i].get_name(),0.0200, "${:.2f}".format(Investors[i].get_fi()), "${:.2f}".format(returnInv)))#print the investor and all required information with formating    
        else: #else if an investor is a growth one
            randomRate = round(random.uniform(-0.1, 0.2),4) #compute a random growth rate between -0.1 and 0.2 with 4 sig fig
            returnInv = Investors[i].GetInvestmentReturn(randomRate) #Compute investor return on investment by calling method on object from Growth
            print("{:<10} {:>10} {:>15} {:>15}".format(Investors[i].get_name(),randomRate, "${:.2f}".format(Investors[i].get_gi()),"${:.2f}".format(returnInv)))#print required investor information with correct formating        
    
#Execute only if module is main
if __name__ == "__main__":
    display_menu()
