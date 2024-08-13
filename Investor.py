class Investor():
    def __init__(self, name=None): #Constructor with 1 attribute
        self.set_name(name) #setting name as a private attribute
        
    #getter-setter methods
    def set_name(self, name):
        self.__name = name #name is private
    def get_name(self):
        return self.__name #get method for private

    def __str__(self): #Not used often because __str__ of Fixed and Growth are always called
        return self.get_name()

    # Fake out Python to use methods instead of direct assignment
    name=property(get_name,set_name)

'''p = Investor()
print(p)
p.set_name("Mike")
print(p)'''

        
