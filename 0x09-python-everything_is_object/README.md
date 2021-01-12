#  Python - Everything is object:
This project you find several task to learn program with python. The first part is only questions about Python’s specificity like “What would be the result of…”. The topics are:

- Types objects
- Object and values
- Aliasing
- immutable vs mutable types
- cloning lists
- python tuples: immutable but potentially changing

## **FILES**
<table>
<thead>
<tr>
  <th>TASK</th>
  <th>Files</th>
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
  <td>0-answer.txt</td>
  <td>What function would you use to print the type of an object?

Write the name of the function in the file, without ().
</td>
</tr>
<tr>
  <td>1</td>
  <td>1-answer.txt</td>
  <td>How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().
</td>
</tr>
<tr>
  <td>2</td>
  <td>2-answer.txt</td>
  <td>In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = 100
</td>
</tr>
<tr>
  <td>3</td>
  <td>3-answer.txt</td>
  <td>In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = 89
</td>
</tr>
<tr>
  <td>4</td>
  <td>4-answer.txt</td>
  <td>In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = a
</td>
</tr>
<tr>
  <td>5</td>
  <td>5-answer.txt</td>
  <td>In the following code, do a and b point to the same object? Answer with Yes or No.
    >>> a = 89
    >>> b = a + 1
</td>
</tr>
<tr>
  <td>6</td>
  <td>6-answer.txt</td>
  <td>What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 = s1
    >>> print(s1 == s2)
</td>
</tr>
<tr>
  <td>7</td>
  <td>7-answer.txt</td>
  <td>What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 is s1
    >>> print(s1 is s2)
</td>
</tr>
<tr>
  <td>8</td>
  <td>8-answer.txt</td>
  <td>What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 = "Holberton"
    >>> print(s1 == s2)
</td>
</tr>
<tr>
  <td>9</td>
  <td>9-answer.txt</td>
  <td>What do these 3 lines print?
    >>> s1 = "Holberton"
    >>> s2 = "Holberton"
    >>> print(s1 is s2)
</td>
</tr>
<tr>
  <td>10</td>
  <td>10-answer.txt</td>
  <td>What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3]
    >>> print(l1 == l2)
</td>
</tr>
<tr>
  <td>11</td>
  <td>11-answer.txt</td>
  <td>What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = [1, 2, 3]
    >>> print(l1 is l2)
</td>
</tr>
<tr>
  <td>12</td>
  <td>12-answer.txt</td>
  <td>What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 == l2)
</td>
</tr>
<tr>
  <td>13</td>
  <td>13-answer.txt</td>
  <td>What do these 3 lines print?
    >>> l1 = [1, 2, 3]
    >>> l2 = l1
    >>> print(l1 is l2)
</td>
</tr>
<tr>
  <td>15</td>
  <td>15-answer.txt</td>
  <td>What does this script print?
    l1 = [1, 2, 3]
    l2 = l1
    l1 = l1 + [4]
    print(l2)
</td>
</tr>
<tr>
  <td>16</td>
  <td>16-answer.txt</td>
  <td>What does this script print?
    def increment(n):
    n += 1

    a = 1
    increment(a)
    print(a)
</td>
</tr>
<tr>
  <td>17</td>
  <td>17-answer.txt</td>
  <td>What does this script print?
    def increment(n):
    n.append(4)

    l = [1, 2, 3]
    increment(l)
    print(l)
</td>
</tr>
<tr>
  <td>18</td>
  <td>18-answer.txt</td>
  <td>def assign_value(n, v):
    n = v

    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    assign_value(l1, l2)
    print(l1)
</td>
</tr>
<tr>
  <td>19</td>
  <td>19-copy_list.py</td>
  <td>Write a function def copy_list(l): that returns a copy of a list.

    The input list can contain any type of objects
    Your file should be maximum 3-line long (no documentation needed)
    You are not allowed to import any module
</td>
</tr>
<tr>
  <td>20</td>
  <td>20-answer.txt</td>
  <td>a = ()
    Is a a tuple? Answer with Yes or No.
</td>
</tr>
<tr>
  <td>21</td>
  <td>21-answer.txt</td>
  <td>a = (1, 2)
    Is a a tuple? Answer with Yes or No.
</td>
</tr>
<tr>
  <td>22</td>
  <td>22-answer.txt</td>
  <td>a = (1)
    Is a a tuple? Answer with Yes or No.
</td>
</tr>
<tr>
  <td>23</td>
  <td>23-answer.txt</td>
  <td>a = (1, )
    Is a a tuple? Answer with Yes or No.
</td>
</tr>
<tr>
  <td>24</td>
  <td>24-answer.txt</td>
  <td>What does this script print?
    a = (1)
    b = (1)
    a is b
</td>
</tr>
<tr>
  <td>25</td>
  <td>25-answer.txt</td>
  <td>What does this script print?
    a = (1, 2)
    b = (1, 2)
    a is b
</td>
</tr>
<tr>
  <td>26</td>
  <td>26-answer.txt</td>
  <td>What does this script print?
    a = ()
    b = ()
    a is b
</td>
</tr>
<tr>
  <td>27</td>
  <td>27-answer.txt</td>
  <td>
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
    Will the last line of this script print 139926795932424? Answer with Yes or No.
</td>
</tr>
<tr>
  <td>28</td>
  <td>28-answer.txt</td>
  <td>
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
    Will the last line of this script print 139926795932424? Answer with Yes or No.
</td>
</tr>
<tr>
  <td>29</td>
  <td>blog</td>
  <td>Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

    introduction
    id and type
    mutable objects
    immutable objects
    why does it matter and how differently does Python treat mutable and immutable objects
    how arguments are passed to functions and what does that imply for mutable and immutable objects
</td>
</tr>
<tr>
  <td>30</td>
  <td>106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt</td>
  <td>
guillaume@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
guillaume@ubuntu:/python3$ 
    Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

   - How many string objects are created by the execution of the first line of the script? (106-line1.txt)
   - How many string objects are created by the execution of the second line of the script (106-line2.txt)
   - After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
   - After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
   - How many string objects are created by the execution of the last line of the script (106-line5.txt)
</td>
</tr

</tbody>
</table>

### _By Giraluna Gomez_
### @Giraluna1