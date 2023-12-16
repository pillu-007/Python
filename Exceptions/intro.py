'''

In any programming language there are 2 types of errors are possible.
1. Syntax Errors
2. Runtime Errors
1. Syntax Errors:
The errors which occurs because of invalid syntax are called syntax errors.

Eg 1:
x=10
if x==10
print("Hello")
SyntaxError: invalid syntax


Eg 2:
print "Hello"
SyntaxError: Missing parentheses in call to 'print'

2. Runtime Errors:
Also known as exceptions.

While executing the program if something goes wrong because of end user input or
programming logic or memory problems etc then we will get Runtime Errors.

Eg: print(10/0) ==>ZeroDivisionError: division by zero

print(10/"ten") ==>TypeError: unsupported operand type(s) for /: 'int' and 'str'


What is Exception:
An unwanted and unexpected event that disturbs normal flow of program is called
exception.

Default Exception Handing in Python:
Whevever an exception occurs PVM will create the corresponding exception object and
will check for handling code. If handling code is not available then Python interpreter
terminates the program abnormally and prints corresponding exception information to
the console.



'''