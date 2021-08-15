class Pen(object):
        def __init__(self,length,color,brand,inkAmount):
            self.length = length
            self.color = color
            self.brand = brand 
            self.inkAmount = inkAmount


        def printPenProperties(self):   
         print(self.inkAmount)
         print(self.length)
         print(self.color)
         print(self.brand)
         if( self.inkAmount < 20 ):
          print("\n","The ink amount is very low... time to refill!")
         else:
          print("\n", "You can continue to use the pen!")  

        def write(self):
            print("Write using ur pen!")


Octane = Pen(45,"red","cello",50) 
print(Octane.write())
print(Octane.printPenProperties())

       

