''' Author: Brock Hemsouvanh
    Date: 2024-02-11
    hemsouvanh_hobbies.py Description: Uses if...else statements to create a weekly list of hobbies.
'''

hobbies = ['composing music', 'coding', 'martial arts', 'animal rights activism', 'home improvement projects']

# Use a for loop to iterate over the list of hobbies and print them to the console window
print("My hobbies include:")
for hobby in hobbies:
    print("- " + hobby)

# Create a list of days (Sunday through Saturday)
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Iterate over the list of days and add an if…else statement
print("\nWeekly Schedule:")
for day in days:
    if day == 'Saturday' or day == 'Sunday':
        print(f"{day}: It's the weekend! Time to enjoy your hobbies.")
    else:
        print(f"{day}: It's a workday. Keep pushing through!")