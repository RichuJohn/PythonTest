"""sample HelloWorld program"""

def print_hello(name):
    """method to print hello"""
    hello = "Hello World " + name
    print(hello)

print_hello("Richu")
print(print_hello.__doc__)
