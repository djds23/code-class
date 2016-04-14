# Bonus!

### On your own, try to make the turtle draw a square.

* `from turtle import *`
* [Make sure to read the documentation](https://docs.python.org/2/library/turtle.html)


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

##### Tip:
You are not expected to just know how to do this. This will take experimentation and time. Try out commands in the python interpreter.
Google is your friend, and make sure to read the documentation. Finally, do not be afraid to ask for help.
