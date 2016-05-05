# Week 4

## Open and Shut Case.

* Review from last week
	* Functions, again
		* What do we use them for? Why are they useful?
	* Lists & Dictionaries
		* Storing data and operating on it
	* Loops
		* Code to operate on sequences of data

#### Getting to the point
In the past few weeks we have been doing most of our work in scripts and the command line. Wouldn't it be useful if you could feed data to your programs?

```python
# You can use the function raw_input to call out to the user for data

# Program pauses & asks me my name
print('Are you Dean?')
user = raw_input('>') 

# What I input is stored as a 
# string in the variable user
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


## [Break for Assignment 1](exercises/week4/assignment_4_1.md)


#### 30 minutes

* opening a file
* reading a file
* `import csv`

```python
import csv

my_file = open('file.csv')
my_table = csv.reader(my_file)
for row in my_table:
1.     print(row)
```
* Project day? What could we not do 4 weeks ago that is now possible?

* writing a file
