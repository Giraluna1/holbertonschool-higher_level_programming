#  Inheritance
This project you find several task to learn program with python about topics this topics

- Multiple inheritance
- Magic Methods
- Polymorphism

## **FILES**
<table>
<thead>
<tr>
  <th>TASK</th>
  <th>Directory</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td></td>
  <td> README.md</td>
  <td>...<td>
</tr>
<tr>
  <td>0</td>
  <td>0-lookup.py</td>
  <td>Write a function that returns the list of available attributes and methods of an object:

    Prototype: def lookup(obj):
    Returns a list object
    You are not allowed to import any module
</td>
</tr>
<tr>
  <td>1</td>
  <td>1-my_list.py, tests/1-my_list.txt</td>
  <td>Write a class MyList that inherits from list:

    Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
    You can assume that all the elements of the list will be of type int
    You are not allowed to import any module
</td>
</tr>
<tr>
  <td>2</td>
  <td>2-is_same_class.py</td>
  <td>Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

    Prototype: def is_same_class(obj, a_class):
    You are not allowed to import any module
</td>
</tr>
<tr>
  <td>3</td>
  <td>3-is_kind_of_class.py</td>
  <td>Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

    Prototype: def is_kind_of_class(obj, a_class):
    You are not allowed to import any module
</td>
</tr>
<tr>
  <td>4</td>
  <td>4-inherits_from.py</td>
  <td>Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

    Prototype: def inherits_from(obj, a_class):
    You are not allowed to import any module
</td>
</tr>
<tr>
  <td>5</td>
  <td>5-base_geometry.py</td>
  <td>Write an empty class BaseGeometry.

    You are not allowed to import any module

</td>
</tr>
<tr>
  <td>6</td>
  <td>6-base_geometry.py</td>
  <td>Write a class BaseGeometry (based on 5-base_geometry.py).

    Public instance method: def area(self): that raises an Exception with the message area() is not implemented
    You are not allowed to import any module

</td>
</tr>
<tr>
  <td>7</td>
  <td>7-base_geometry.py, tests/7-base_geometry.txt</td>
  <td>Write a class BaseGeometry (based on 6-base_geometry.py).

    Public instance method: def area(self): that raises an Exception with the message area() is not implemented
    Public instance method: def integer_validator(self, name, value): that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
    You are not allowed to import any module

</td>
</tr>
<tr>
  <td>8</td>
  <td>8-rectangle.py</td>
  <td>Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

    Instantiation with width and height: def __init__(self, width, height):
        width and height must be private. No getter or setter
        width and height must be positive integers, validated by integer_validator
</td>
</tr>
<tr>
  <td>9</td>
  <td>9-rectangle.py</td>
  <td>Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

    Instantiation with width and height: def __init__(self, width, height)::
        width and height must be private. No getter or setter
        width and height must be positive integers validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
</td>
</tr>
<tr>
  <td>10</td>
  <td>10-square.py</td>
  <td>Write a class Square that inherits from Rectangle (9-rectangle.py):

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented
</td>
</tr>
<tr>
  <td>11</td>
  <td>11-square.py</td>
  <td>Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

    Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the square description: [Square] <width>/<height>
</td>
</tr>
</tbody>
</table>

### _By Giraluna Gomez_ @Giraluna1