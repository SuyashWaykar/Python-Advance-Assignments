#!/usr/bin/env python
# coding: utf-8

# ### 1. What is the purpose of Python's OOP?

# Ans: In Python, object-oriented programming (OOPs) uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

# ### 2. Where does as inheritance search look for an attribute?
# 

# Ans: Python searches for an attribute in an upward tree of attributes. it first searches for the attribute in its instance and then looks in the class it is generated from, to all super classes listed in its class header.

# ### 3. How do you distinguish between a class object and an instance object?

# Ans: Class is a template for creating objects whereas object is an instance of class. Seperate memory is allocated for each object whenever an object is created but for a class this does not happens. A Class is created once and many objects are created using a class. As Classes have no allocated memory, they can't be manipulated but objects can be manipulated.

# ### 4. What makes the first argument in a class’s method function special?

# Ans: Python Classes usually have three types of methods which are:
# 
#     Instance Methods (object level methods)
# 
#     Class Methods (class level methods)
# 
#     Static Methods (general utility methods)
# 
#     self is the first argument for instance methods. which refers to the object itself.
# 
#     cls is the first argument for class methods which refers to the class itself.

# ### 5. What is the purpose of the init method?

# Ans: init is a reseved method in python classes. It serves the role of a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

# ### 6. What is the process for creating a class instance?

# Ans: To create a class instance, we need to call the class by its name and pass the arguments to the class, which its init method accepts.
# 
# Example:-
# my_name = my_class("vaishnavi","vaishu") Here my_name is an instance of class my_class with attributes "vaishnavi" and "Vaishu".

# ### 7. What is the process for creating a class?

# Ans: class keyword is used to created a class in python. The syntax to create a class in python is class :
# 
# Example: class shop: ➞ this creates a class called shop

# ### 8. How would you define the superclasses of a class?

# Ans: Superclass/Parent class is given as a arugment to the child class
