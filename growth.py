from Investor import Investor #import Investor class

class Growth(Investor): #create Growth class as a child of investor
    def __init__(self, name, growth_investment=0): #constructor for 2 attributes
        super().__init__(name) #Calling constructor of parent function to pass down name attribute
        self.set_gi(growth_investment) #using set method to initialize growth_investment and to make it a private variable

    #getter-setter methods
    def set_gi(self, growth_investment):
        self.__gi = growth_investment #sets growth investment as a private variable
    def get_gi(self):
        return self.__gi

    #additional get method used for P3.py
    def get_both(self):
        return self.__gi
    
    # Fake out Python to use methods instead of direct assignment
    growth_investment=property(get_gi,set_gi)

    def __str__(self): #Function called when printing a Growth object. Uses correct formating
        return "{:<8} {:<10} {:>13}".format(self.get_name(), "growth","${:.2f}".format(self.get_gi()))

    #Update the Investment amount
    def updateInvestment(self, amount):
        self.set_gi(self.get_gi() + amount) #adds an amount to current investment and sets it as a new investment
        

    #Investment rate return
    def GetInvestmentReturn(self,rate):
        return self.get_gi()*rate


    
#Execute only if module is main
if __name__ == "__main__":
    p = Growth("Miks",1000)


#Test code   
p = Growth("Miks",1000)
print(p)
p.updateInvestment(900)
print(p)
p.set_name("Mike")
print(p)


'''print(p.get_name())
p.set_name("Mike")
p.set_fi(90)
print(p.get_fi())'''



