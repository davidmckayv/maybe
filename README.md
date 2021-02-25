# maybe
Python decorator that executes the function, **maybe**.

The idea is that some functions should randomly execute.  This is implemented as a standard python decorator but using random.randint as a coin flip to decide whether or not the decorated function executes.

## Example

````
@maybe
def say_hello():
    print("Hello!")


say_hello()
````