''' Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. '''
# Python example to check if a class is
# subclass of another
  
class Base(object):
    pass   # Empty Class
  
class Derived(Base):
    pass   # Empty Class
  
# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))
  
d = Derived()
b = Base()
  
# b is not an instance of Derived
print(isinstance(b, Derived))
  
# But d is an instance of Base
print(isinstance(d, Base))