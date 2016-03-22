# Week 2

## loops, functions and conditionals

* defining your own functions
* using conditionals: `if ... else`
* using conditionals: `if ... elif ... else`
* using loops: `while`
* using loops: `for`
* using lists

### Homework

* `import turtle` 
	* make the turtle draw a square
	* reading documentation
	* [Make the turtle move around!](https://docs.python.org/3/library/turtle.html)


```python
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()
```