Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
SyntaxError: multiple statements found while compiling a single statement
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.clear()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.penup()
tao.goto(200,200)
tao.pendown()
for i in range(4):
...     tao.forward(100)
...     tao.left(90)
... 
...     
>>> tao.penup()
>>> tao.goto(-200,-200)
>>> tao.forward(100)
>>> tao.pendown()
>>> tao.foeward(100)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tao.foeward(100)
AttributeError: 'Turtle' object has no attribute 'foeward'. Did you mean: 'forward'?
>>> tao.forward(100)
>>> tao.left(135)
>>> tao.forward(100)
