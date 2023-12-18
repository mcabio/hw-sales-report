"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # Creates an empty list for salespeople
melons_sold = [] # Creates an empty list for melons sold.

f = open('sales-report.txt') # This opens the sales-report.txt file

for line in f: # This for loop iterates over each line in the txt file.
    line = line.rstrip() # This removes the trailing white spaces for each line and turns them into one long string
    entries = line.split('|') # This creates a variable 'entries' that turns the line string into a list,
                              # the index created is based on splitting the string by '|' the vertical line 
    salesperson = entries[0] # This states that the string in the 0 index of entries represents a salesperson
    melons = int(entries[2]) # This states that the string in the 2nd index of entries represents melons and 
                             # since the list contains all strings, the int command turns this index into an integer

    if salesperson in salespeople: # This if statement states if a salesperson is already in the salespeople list
        position = salespeople.index(salesperson) # it finds the position (index) of 
                                                  # that salesperson in the list using index(salesperson).
        melons_sold[position] += melons # Then, it increments the corresponding element 
                                        # in the melons_sold list by the number of melons sold.
        
    else:
        salespeople.append(salesperson) # If the salesperson is not in the list, it adds 
                                        # the salesperson to the salespeople list.
        melons_sold.append(melons) # It also adds the corresponding number of melons sold to the melons_sold list.


for i in range(len(salespeople)): # This code is using a for loop to iterate through each 
                                  # index of the salespeople list and printing the corresponding information 
                                  # about melons sold. This loop iterates through the indices of 
                                  # the salespeople list. range(len(salespeople)) generates a 
                                  # sequence of indices from 0 to len(salespeople) - 1.
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')