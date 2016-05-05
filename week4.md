# Week 4

## Open and Shut Case.

* Review from last week
	* Functions, again
		* What do we use them for? Why are they useful?
	* Lists & Dictionaries
		* Storing data and operating on it
	* Loops
		* Code to operate on sequences of data

#### Reviewing the homework
In the past few weeks we have been doing most of our work in scripts and the command line. Wouldn't it be useful if you could feed data to your programs?

```python
# You can use the function raw_input to call out to the user for data

# Program pauses & asks me my name
user = raw_input('Are you Dean?') 

# What I input is stored as a 
#  string in the variable user
if user == 'Dean': 
    print('Oh hey Dean! Whats up!')
else:
    print('Hmmm then what are you doing at his computer?')
```


Now that we can add input, our data does not have to exist in code.

```python
# Make company email addresses 
existing_emails = []

def make_email(full_name):
    # 'Dean Silfen'.split() => ['Dean', 'Silfen']
    full_name_list = full_name.split()
    first_initial = full_name_list[0][0]
    last_name = full_name_list[1]
    email = first_initial + last_name + '@company.email'
    return email.lower()

while True:
    full_name = raw_input('Full Name: ')
    if full_name == 'exit':
        exit()
        
    email = make_email(full_name)
    if email in existing_emails:
        print('Email exists! Employees cannot get one email address!')
    else:
        existing_emails.append(email)
        print('%s is the newest member of our team' % email)
```


#### 20 minutes 

* strings cont...
	* `split`ting up strings
	* [`find`ing things `in` strings](https://docs.python.org/2/library/string.html#string.find)
	* Slicing up strings with indexes

```python
# Splitting string into a list
full_name = 'Dean Silfen'
names = full_name.split()
print(names) #=> ['Dean', 'Silfen']

first_name = names[0]
print(first_name) #=> 'Dean'

# Finding Specific places in a string
dirty_data = 'd. silfen uniq_id:4422              pizza'
start_of_relevant_data = dirty_data.find('uniq_id:') + 8
end_of_relevant_data = start_of_relevant_data + len('uniq_id:') # len tells us the length of a string
useful_information = dirty_data[start_of_relevant_data:end_of_relevant_data]
print(useful_information)


first_initial = first_name[0]
print(first_initial) #=> 'D'

```

## [Break for Assignment 3](exercises/week3/assignment_3_3.md)


#### 30 minutes

* opening a file
* reading a file
* writing a file
* `import csv`

* csv cont... (dictreader/dictwriter)
* Project day? What could we not do 4 weeks ago that is now possible?

