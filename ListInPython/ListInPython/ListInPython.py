#list allow you to store multiple values
#try to keep one data type in the same lists
guests = ['Adrian','Susan','Chris','Bill'];
#you can create empty list and add values later
#guests = []
#scores[]
#the first value is in position 0
#print the first value 
print(guests[0]);
scores = [78,85,62,49,98];
#print the fourth score
print(scores[3]);
#we call the position of an item in the list index
#in python we can count backwards
#print the last entry in the list
print(guests[-1]);
#print the second to last entry in the list
print(guests[-2]);
#updating lists
print('The first value is ' + guests[0]);

#change the first value in te list to steve
guests[0] = 'Steve'
print("First value is now " + guests[0]);
#You can add a value to a list with append()
guests.append('Adrian');
#Display the list
print(guests);
#also you can remove a value from a list with remove()
guests.append('The grinch');
print(guests);
guests.remove('The grinch');
print(guests);
#or use the del command
guests.append('Troll');
print(guests)
del guests[-1];
print (guests);
#The index function will search the list and return the index of the position where the value was found 
print(guests.index('Chris'));
#Use of looping 
#for steps in range(5):
#    print(guests[steps]);
nbrValueInList = len(guests)
for steps in range(nbrValueInList):
    print(guests[steps]);
#lazy way
#specify the name of your list and variable name to hold each entry as you go through the loop
for currentGuest in guests:
#the variable guest will contain the values as we go through the loop
    print(currentGuest);
#you can also sort the list with the sort function
#sort the names by alphabetical order
guests.sort()
for guests in guests:
    print(guests);