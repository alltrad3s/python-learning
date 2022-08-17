#Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
def print_seconds(hours, minutes, seconds):
    print(3600*hours+60*minutes+seconds)

print_seconds(1,2,3)

#Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

#Updated Code
def month_days(month, days):
    print(str(month) + " has " + str(days) + " days.")

month_days("June", 30)
month_days("July", 31)

#This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6?
def rectangle_area(base, height):
	area = base*height  # the area is base*height
	print("The area is " + str(area))

rectangle_area(5,6)