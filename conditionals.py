#n Python uppercase letters are alphabetically sorted before lowercase letters. So the test below will result in "True"
print("cat" > "Cat")

#The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?
def is_positive(number):
  if number > 0:
    return True
  else:
    return False

is_positive(-5)
is_positive(0)
is_positive(13)

#So how come we have these two return statements, one below the other, without an else statement? The trick is that when a return statement is executed, 
# the function exits so that the code that follows doesn't get executed. This means that if the number is even, 
# the computer will reach the return true statement and exit the function. Anything that comes after that will only be executed if the condition in the if statement was false.
def is_even(number):
    if number % 2 == 0:
        return True 
    return False

# The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

#Practice Quiz
#What's the value of this Python expression: (2**2) == 4?
#True

#Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

#What’s the output of this code if number equals 10?
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

  #Answer 2

#Question 4
#Is "A dog" smaller or larger than "A mouse"? Is 9999+8888 smaller or larger than 100*100? Replace the plus sign in the following code to let Python check it for you and then answer.
print("A dog" > "A mouse")
print(9999+8888 > 100*100)
#"A dog" is smaller than "A mouse" and 9999+8888 is larger than 100*100

#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. 
# A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, 
# can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks + 1)
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192