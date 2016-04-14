# Exercise 1

Use the template below to write a function that prints the number of in stock brands.

```python
orange_juice = {
    'brand': 'tropicana',
    'juice_type': 'orange',
    'flavor profile': 'bright',
    'cost': 2,
    'servings': 6,
    'in stock': True,
} 

apple_juice = {
    'brand': 'martinellis',
    'juice_type': 'apple',
    'flavor profile': 'tangy',
    'cost': 5,
    'servings': 8,
    'in stock': False,
} 

grape_juice = {
    'brand': 'mott',
    'juice_type': 'grape',
    'flavor profile': 'tart',
    'cost': 3,
    'servings': 4,
    'in stock': True,
} 

juice_stock = [orange_juice, apple_juice, grape_juice]

def in_stock_count(juice_stock):
    # your code here
    return # the number of in stock brands

print(in_stock_count(juice_stock)) #=> 2
```

# Exercise 2

#### Using the same data as above!

Write another function to return a list of the brands in stock

```python

def in_stock_brands(juice_stock):
    # your code here
    return # a list of brands in stock

print(in_stock_brands(juice_stock)) #=> ['mott', 'tropicana']
```


