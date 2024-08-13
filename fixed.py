from Investor import Investor #import Investor class

class Fixed(Investor): #create Fixed class as a child of investor
    def __init__(self, name, fixed_investment=0): #constructor with 2 attributes
        super().__init__(name) #Passing the name from Investor
        self.set_fi(fixed_investment) #Initializing attribute using set method

    #getter-setter methods
    def set_fi(self, fixed_investment):
        self.__fi = fixed_investment
    def get_fi(self):
        return self.__fi #using the investment as a private variable

    #additional get method used for P3.py
    def get_both(self):
        return self.__fi
    
    # Fake out Python to use methods instead of direct assignment
    fixed_investment=property(get_fi,set_fi)

    def __str__(self): #Function called when printing an object. Uses correct formating
        return "{:<8} {:<10} {:>13}".format(self.get_name(), "fixed","${:.2f}".format(self.get_fi()))

    #Update the Investment amount
    def updateInvestment(self, amount):
        return self.set_fi(self.get_fi()+amount)

    #Investment rate return
    def GetInvestmentReturn(self,rate = 0.02): #Yearly fixed rate for Belfius Local bank in Belgium
        return self.get_fi()*rate



#Execute only if module is main
if __name__ == "__main__":
    p = Fixed("Miks",1000)

#Test Code
'''p = Fixed("Miks",1000)
#print(type(p))'''
'''print(p.GetInvestmentReturn())'''
'''print(p)
print(p.updateInvestment(900))
print(p)'''


'''print(p.get_name())
p.set_name("Mike")
p.set_fi(90)
print(p.get_fi())'''



