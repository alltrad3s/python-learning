#Fill in the blanks to calculate the area of a triangle of base 5, height 3 and output the result.  Reminder:  the area of a triangle is (base*height)/2.
base = 5
height = 3
area = (base*height)/2

print(area)

#Explicit conversion example
print("Explicit conversion example")

base = 5
height = 3
area = (base*height)/2

print("The area of the triangle is: " + str(area))

#In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string. 
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))

#In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.

bill = 47.28
tip = bill * (15/100)
total = bill + tip
share = total/2 
print("Each person needs to pay: " + str(share))

#Pregunta 2 This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.

numerator = 10
denominator = 10
result = numerator / denominator
print(result)

#Pregunta 3 Combine the variables to display the sentence "How do you like Python so far?" 

word1 = "How "
word2 = "do "
word3 = "you "
word4 = "like "
word5 = "Python "
word6 = "so "
word7 = "far?"

print(word1 + word2 + word3 + word4 + word5 + word6 + word7)

#This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.

print("2 + 2 = " + str(2 + 2))


