'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']

print(sorted(my_friends))

# 1B. Comment your code in 1A to convince yourself you understand how it works
# Inside the print statement is the sorted function that simply sorts the list titled my_friends alphabetically. 

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

print(my_account.keys())

# 2B. Comment your code in 2A to convince yourself you understand how it works
# Within the print statement I'm adding .keys to the variable to list the keys without /n which keeps them on the same line.


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

print(my_string.count('wood'))

# 3B. Comment your code in 3A to convince yourself you understand how it works
# I'm printing the variable my_string but using the .count function to add the number of times the substring word wood appears in the string.


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

print(my_list.count('banana'))

# 4B. Comment your code in 4A to convince yourself you understand how it works
# I'm printing the variable my_list but using the .count function to add the number of times the word wood appears in the list.



# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')

print(set(my_list))
# 5B. Comment your code in 5A to convince yourself you understand how it works
# In the print statement I'm using the function set to call each unique string aka fruit in the list one time each.

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

from numpy import random

print(random.rand())




# 6B. Comment your code in 6A to convince yourself you understand how it works


'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
