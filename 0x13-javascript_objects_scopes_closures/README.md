<p align="center">
    <img alt="0x12 JavaScript - Warm up" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/480px-Unofficial_JavaScript_logo_2.svg.png" />
</p>
<h1 align="center">
    JavaScript - Objects, Scopes and Closures
</h1>

[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg?style=flat-square)](https://github.com/standard/semistandard)

## 🧐 Learning Objects

- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What this means
- What undefined means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## 🛠 TOOLS

Any text editor

# Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

# Install semi-standard

```
$ sudo npm install semistandard --global
```

## 📝 FILES

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
  <td>0-rectangle.js</td>
  <td>WWrite an empty class Rectangle that defines a rectangle:

    You must use the class notation for defining your class

   </td>
</tr>
<tr>
  <td>1</td>
  <td>1-rectangle.js</td>
  <td>Write a class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h

</td>
</tr>
<tr>
  <td>2</td>
  <td>2-rectangle.js</td>
  <td>Write a class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object

</td>
</tr>
<tr>
  <td>3</td>
  <td>3-rectangle.js</td>
  <td>Write a class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments: w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
    Create an instance method called print() that prints the rectangle using the character X

</td>
</tr>
<tr>
  <td>4</td>
  <td>4-rectangle.js/td>
  <td>Write a class Rectangle that defines a rectangle:

    You must use the class notation for defining your class
    The constructor must take 2 arguments: w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
    Create an instance method called print() that prints the rectangle using the character X
    Create an instance method called rotate() that exchanges the width and the height of the rectangle
    Create an instance method called double() that multiples the width and the height of the rectangle by 2

</td>
</tr>
<tr>
  <td>5</td>
  <td>5-square.js</td>
  <td>Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

    You must use the class notation for defining your class and extends
    The constructor must take 1 argument: size
    The constructor of Rectangle must be called (by using super())

</td>
</tr>
<tr>
  <td>6</td>
  <td>6-square.js</td>
  <td>Write a class Square that defines a square and inherits from Square of 5-square.js:

    You must use the class notation for defining your class and extends
    Create an instance method called charPrint(c) that prints the rectangle using the character c
        If c is undefined, use the character X

</td>
</tr>
<tr>
  <td>7</td>
  <td>7-occurrences.js</td>
  <td>Write a function that returns the number of occurrences in a list:

    Prototype: exports.nbOccurences = function (list, searchElement)

</td>
</tr>
<tr>
  <td>8</td>
  <td>8-esrever.js</td>
  <td>Write a function that returns the reversed version of a list:

    Prototype: exports.esrever = function (list)
    You are not allow to use the built-in method reverse

</td>
</tr>
<tr>
  <td>9</td>
  <td>9-logme.js</td>
  <td>Write a function that prints the number of arguments already printed and the new argument value. (see example below)

    Prototype: exports.logMe = function (item)
    Output format: <number arguments already printed>: <current argument value>

</td>
</tr>
<tr>
  <td>10</td>
  <td>10-converter.js</td>
  <td>Write a function that converts a number from base 10 to another base passed as argument:

    Prototype: exports.converter = function (base)
    You are not allowed to import any file
    You are not allowed to declare any new variable (var, let, etc..)

</td>
</tr>

</td>
</tr>
</tbody>
</table>

## _BY_ @Giraluna1
