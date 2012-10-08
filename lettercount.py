from sys import argv

#Get filename and open file
#Store file in a string
script, file_name = argv

my_file_contents = open(file_name).read()

#Convert the file string to all lower case
lowercase_file = my_file_contents.lower()

# Create an empty list of 26 spaces to use as a counter
counter = []

for i in range(0,26):
    counter.append(0)

    #Shortcut way to do this:
    #     counter = [0] * 26

# Loop through the entire file string
# And increment the counter where appropriate
for current in lowercase_file:
    
    #Convert the character to an ordinal
    #Find the appropriate position in the counter list
    position_to_update = ord(current) - 97    #We should assign the 97 to a variable so it's clear what the 97 stands for

    #If the position is within 0 to 25, means it is an alphabet character
    #Then you update the counter
    if position_to_update >= 0 and position_to_update<=25:
        counter[position_to_update] += 1
    #Else, it is a special character
    #Do not update the counter
    else:
        continue

# Print out the results of the counter on one line at a time
for element in counter:
    print element