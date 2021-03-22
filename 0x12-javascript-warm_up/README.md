<p align="center">
    <img alt="0x12 JavaScript - Warm up" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/480px-Unofficial_JavaScript_logo_2.svg.png" />
</p>
<h1 align="center">
    BINARY TREES PROYECT
</h1>

[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg?style=flat-square)](https://github.com/standard/semistandard)

## 🧐 Learning Objects

- **Why JavaScript programming is amazing**
- **How to run a JavaScript script**
- **How to create variables and constants**
- **What are differences between var, const and let**
- **What are all the data types available in JavaScript**
- **How to use the if, if ... else statements**
- **How to use comments**
- **How to affect values to variables**
- **How to use while and for loops**
- **How to use break and continue statements**
- **What is a function and how do you use functions**
- **What does a function that does not use any return statement return**
- **Scope of variables**
- **What are the arithmetic operators and how to use them**
- **How to manipulate dictionary**
- **How to import a file**

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
  <td>0-javascript_is_amazing.js</td>
  <td>Write a script that prints “JavaScript is amazing”:

    You must create a constant variable called myVar with the value “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var

   </td>
</tr>
<tr>
  <td>1</td>
  <td>1-multi_languages.js</td>
  <td>Write a script that prints 3 lines:

    The first line: “C is fun”
    The second line: “Python is cool”
    The third line: “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var

</td>
</tr>
<tr>
  <td>2</td>
  <td>2-arguments.js</td>
  <td>Write a script that prints a message depending of the number of arguments passed:

    If no arguments are passed to the script, print “No argument”
    If only one argument is passed to the script, print “Argument found”
    Otherwise, print “Arguments found”
    You must use console.log(...) to print all output
    You are not allowed to use var

Reference: process.argv

</td>
</tr>
<tr>
  <td>3</td>
  <td>3-value_argument.js</td>
  <td>Write a script that prints the first argument passed to it:

    If no arguments are passed to the script, print “No argument”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use length

</td>
</tr>
<tr>
  <td>4</td>
  <td>4-concat.js</td>
  <td>Write a script that prints two arguments passed to it, in the following format: “ is ”

    You must use console.log(...) to print all output
    You are not allowed to use var

</td>
</tr>
<tr>
  <td>5</td>
  <td>5-to_integer.js</td>
  <td>Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

    If the argument can’t be converted to an integer, print “Not a number”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use try/catch

</td>
</tr>
<tr>
  <td>6</td>
  <td>6-multi_languages_loop.js</td>
  <td>Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

    The first line: “C is fun”
    The second line: “Python is cool”
    The third line: “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use any if/else statement
    You can use only one console.log
    You must use a loop (while, for, etc.)

</td>
</tr>
<tr>
  <td>7</td>
  <td>7-multi_c.js</td>
  <td>Write a script that prints x times “C is fun”

    Where x is the first argument of the script
    If the first argument can’t be converted to an integer, print “Missing number of occurrences”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You can use only two console.log
    You must use a loop (while, for, etc.)

</td>
</tr>
<tr>
  <td>8</td>
  <td>8-square.js</td>
  <td>Write a script that prints a square

    The first argument is the size of the square
    If the first argument can’t be converted to an integer, print “Missing size”
    You must use the character X to print the square
    You must use console.log(...) to print all output
    You are not allowed to use var
    You must use a loop (while, for, etc.)

</td>
</tr>
<tr>
  <td>9</td>
  <td>9-add.js</td>
  <td>Write a script that prints the addition of 2 integers

    The first argument is the first integer
    The second argument is the second integer
    You have to define a function with this prototype: function add(a, b)
    You must use console.log(...) to print all output
    You are not allowed to use var

</td>
</tr>
<tr>
  <td>10</td>
  <td>10-factorial.js</td>
  <td>Write a script that computes and prints a factorial

    The first argument is integer (argument can be cast as integer) used for computing the factorial
    Factorial of NaN is 1
    You must do it recursively
    You must use a function
    You must use console.log(...) to print all output
    You are not allowed to use var

</td>
</tr>
<tr>
  <td>11</td>
  <td>11-second_biggest.js</td>
  <td>Write a script that searches the second biggest integer in the list of arguments.

    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
    You must use console.log(...) to print all output
    You are not allowed to use var

</td>
</tr>
<tr>
  <td>12</td>
  <td>12-object.js</td>
  <td>Update this script to replace the value 12 with 89:

    You are not allowed to use var

</td>
</tr>
<tr>
  <td>13</td>
  <td>13-add.js</td>
  <td>Write a function that returns the addition of 2 integers.

    The function must be visible from outside
    The name of the function must be add
    You are not allowed to use var

</td>
</tr>

</td>
</tr>
</tbody>
</table>

## _BY_ @Giraluna1
