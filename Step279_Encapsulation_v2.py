#Private:
class Protected:
    def __init__(self):
        self.__privateBonus = 0     #no bonus at first.
    
    def getPrivate(self):
        print(self.__privateBonus)
    
    def setPrivate(self, private):
        self.__privateBonus = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(2000)    #Big two grand bonus, privately added.
obj.getPrivate()


#Protected:
class Protected:
    def __init__(self):
        self._employeeWage = 0

hr = Protected()
hr._employeeWage = 40
print("Hourly Rate: " + str(hr._employeeWage))
