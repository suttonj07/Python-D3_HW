# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according 
# to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, 
# condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the 
  # podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, 
# but also contains a special method called boost that will multiply 
# max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2

  def repair(self):
    self.condition = "NewCondition"
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update
# the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)

  def set_max_speed(self, newSpeed):
    self.max_speed(newSpeed)
  
  def flame_jet(self,other):
    other.condition = "trashed"

s = SebulbasPod(10,"perfect", 100)

s.max_speed = 500
s.set_max_speed(500)


# Make sure to answer the following prompts about your coding experience:

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

# It follows OOP by:
# Encapsulation: By bundling attributes and methods within classes.
# Inheritance: By extending the Podracer class.
# Polymorphism: By allowing SebulbasPod objects to interact with other Podracer objects through the flame_jet method.


# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

# For this specific problem, OOP is well-suited because:

# Encapsulation: It naturally groups related data and behaviors together, making the code more modular and easier to manage.
# Inheritance: Allows extending functionality in a clear and logical manner.
# Polymorphism: Makes it easy to define behavior that can operate on different types of objects in a consistent way.

# How in particular did Object Oriented Programming assist in the solving of this problem?

# OOP assisted in solving this problem by providing a clear structure for defining objects with attributes and methods, reusing existing code through inheritance, allowing flexible interactions through polymorphism, and simplifying the interface through abstraction. These features made the solution more modular, maintainable, and scalable.