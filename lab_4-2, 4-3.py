"""
Create a Python file named lab_4-2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-2.py
Create a variable called school and set it equal to "Fairfield Prep".
Write a statement that splits "Fairfield" and stores it as first_half, and a similar statement that splits " Prep" and stores it as second_half.
Print each half on its own line, then print the two halves joined together using concatenation.

____________________________________

Create a Python file named lab_4-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a program that contains a conditional similar to that on slide 4 that will compare two strings 
provided by the user and return if the strings are equal, one string is greater than the other, or one string is less than the other.


"""
#author Jon Morris
#lab 4-2
school = "Fairfield Prep"
print (school[0:9])
print (school[10:])

#lab 4-3
word = input ("word?")
if word == "Fairfield Prep":
    print ("Fairfield Prep")
elif word > "Fairfield Prep":
    print (word + "comes after Fairfield PreP")
else:
    print (word)