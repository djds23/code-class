# Week 2

## Functions, conditionals and loops

#### 10 minutes

* Review from last week
    * Variables, math and running python
    * The difference between `0`, `"0"` and even `0.0`

Division does strange things

```python
>>> 3/2 # dividing two integers 
1
>>> 3/2.0 # dividing an integer by a float
1.5
```

#### 15 minutes

* Defining your own functions
  * What is a function?
  * Why would you use a function?
  * `return`ing values from functions


```python
def first_function(): 
    print("We are in a function!")
    print("Horray for functions!")

def function_with_arguments(first_argument, second_argument):
    print("You can pass functions arguments")
    print("arguments are variables that are passed into the function")
    print("the first argument is %s" % first_argument)
    print("the second argument is %s" % second_argument)
    return first_argument + " " + second_argument

def square(a):
    return a * a

square_of_two = square(2) #=> 2
```

## [Break for Assignment 1](exercises/week2/assignment_2_1.md)

#### 20 minutes

* Boolean comparisons
	* Boolean operators

Operator | Meaning | Example
--- | :---: | ---
`==`| Equality | `0 == 0 #=> True`
`!=`| Inequality | `0 != 0 #=> True`
`>` | Greater Than | `10 > 0  #=> True`
`<` | Less Than | `10 < 100 #=> True`
`>=` | Greater Than Equal | `100 >= 100 and 1000 >= 100 #=> True`
`<=` | Less Than Equal | `100 <= 100 and 99 <= 100 #=> True`
`and` | Logical and | `True and True #=> True`
`or` | Logical or | `True or False #=> True`
`not` | Logical not | `not False #=> True`

* Using conditionals: `if ... else`
* Using conditionals: `if ... elif ... else`

```python
some_number = 100
if some_number > 0:
    print("Thats some number!")
else:
    print("Stop being so negitive!")

if some_number > 9000:
    print("Over 9000? What!")
elif some_number > 0:
    print("Thats some number!")
else:
    print("Stop being so negitive!")
```


## [Break for Assignment 2](exercises/week2/assignment_2_2.md)

#### 30 minutes

* What are `lists`?
* Using loops: `while`
* Using loops: `for`

```python
def purchase(grocery):
    print('%s was purchased' % grocery)

groceries = ['eggs', 'milk', 'tofu']

for grocery in groceries:
    purchase(grocery)

```	


## [Break for Assignment 3](exercises/week2/assignment_2_3.md)

#### Class notes

* [Check this page for a more comprehensive truth table](http://learnpythonthehardway.org/book/ex27.html)
