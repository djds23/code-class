# Week 3

## CSVs, extracting data, searching & sorting


* Review from last week
    * Functions, conditionals & booleans
    	* Functions as a way to separate out logic. 
    	* Conditionals with boolean logic allow us to make decisions with our code
   
```python
def is_big_number(number):
    if number > 100: 
        # Numbers greater than 100 are considered 'big'
        big_number = True
    else:
        big_number = False
    return big_number

is_big_number(99)
```

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

## [Break for Assignment 1](exercises/week3/assignment_3_1.md)

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

## [Break for Assignment 2](exercises/week3/assignment_3_2.md)

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
index_of_relevant_data = dirty_data.find('uniq_id:') + 8
end_of_relevant_data = index_of_relevant_data +4
useful_information = dirty_data[index_of_relevant_data:end_of_relevant_data]
print(useful_information)


first_initial = first_name[0]
print(first_initial) #=> 'D'

```

## [Break for Assignment 3](exercises/week3/assignment_3_3.md)


### Homework 
* [Play with turtle!](exercises/week3/turtle.md)
* [Complete through chapter 39](http://learnpythonthehardway.org/book/)
* Bring in an idea of a workflow you would like to automate

