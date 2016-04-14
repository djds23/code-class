# Week 3

## CSVs, extracting data, searching & sorting


* Review from last week
    * Functions, conditionals & booleans
    * creating functions, passing arguments and returning values


#### 30 minutes

* What are `lists`?
* Accessing particular indexes

```python
my_list = [1, 2, 3]
first_element = my_list[0] # Indexes start at zero!
second_element = my_list[1]
last_element = my_list[2]


# we can add items to lists with `.append`
my_list.append(4) 
print(my_list) #=> [1, 2, 3, 4]

last_element = my_list[-1] # Negitive indexes to access elements from the right side of the list
```

* Using loops: `while`
* Using loops: `for`

```python
def purchase(grocery):
    print('%s was purchased' % grocery)

groceries = ['eggs', 'milk', 'tofu', 'orange_juice']

for grocery in groceries:
    purchase(grocery)

```	

## [Break for Assignment 1](exercises/week2/assignment_3_1.md)

#### 10 minutes

* using `dict`ionaries 
	* key - value store


```python

orange_juice = {
    'brand': 'tropicana',
    'juice_type': 'orange',
    'flavor profile': 'bright',
    'cost': 2,
    'servings': 6,
    'in stock': True,
} 
# Now we can hold data in a collection to represent
# a real world item. In reality, life is not made
# up of stand alone values, we need the full context
# to tell a story.

print(orange_juice['brand']) #=> 'tropicana'
print(orange_juice['cost']) #=> 2


# we can add items to dicts like so
orange_juice['delicious'] = True

print(orange_juice['delicious']) #=> True
```

## [Break for Assignment 2](exercises/week2/assignment_3_1.md)

#### 20 minutes 

* strings cont...
	* `split`ting up strings
	* `find`ing things `in` strings
	* first and last names from strings '123123 some@email.whatever John Doe'


#### 30 minutes

* opening a file
* reading a file
* writing a file
* `import csv`


### Homework 

* write a script to read a csv file and print out every line with a valid email

