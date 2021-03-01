# SQL -Introduction

This project you find several task to learn program with mysql about this topics:

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requieriments

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
- All your files should end with a new line
- All your SQL queries should have a comment just before
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

# Install MySQL 5,7 on Ubuntu 14.04 LTS

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using EditLine wrapper
$
```

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
  <td> 0-list_databases.sql</td>
  <td>Write a script that lists all databases of your MySQL server.
</td>
</tr>
<tr>
  <td>1</td>
  <td>1-create_database_if_missing.sql</td>
  <td>Write a script that creates the database hbtn_0c_0 in your MySQL server.

- If the database hbtn_0c_0 already exists, your script should not fail
- You are not allowed to use the SELECT or SHOW statements

</td>
</tr>
<tr>
  <td>2</td>
  <td>2-remove_database.sql</td>
  <td>Write a script that deletes the database hbtn_0c_0 in your MySQL server.

    If the database hbtn_0c_0 doesn’t exist, your script should not fail
    You are not allowed to use the SELECT or SHOW statements

</td>
</tr>
<tr>
  <td>3</td>
  <td>3-list_tables.sqle</td>
  <td>Write a script that lists all the tables of a database in your MySQL server.

    The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

</td>
</tr>
<tr>
  <td>4</td>
  <td>4-first_table.sql</td>
  <td>Write a script that creates a table called first_table in the current database in your MySQL server.

    first_table description:
        id INT
        name VARCHAR(256)
    The database name will be passed as an argument of the mysql command
    If the table first_table already exists, your script should not fail
    You are not allowed to use the SELECT or SHOW statements

</td>
</tr>
<tr>
  <td>5</td>
  <td>5-full_table.sql</td>
  <td>Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command
    You are not allowed to use the DESCRIBE or EXPLAIN statements

</td>
</tr>
<tr>
  <td>6</td>
  <td>6-list_values.sql</td>
  <td>Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

    All fields should be printed
    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>7</td>
  <td>7-insert_value.sql</td>
  <td>Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

    New row:
        id = 89
        name = Holberton School
    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>8</td>
  <td>8-count_89.sql</td>
  <td>Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>9</td>
  <td>9-full_creation.sql</td>
  <td>Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

    second_table description:
        id INT
        name VARCHAR(256)
        score INT
    The database name will be passed as an argument to the mysql command
    If the table second_table already exists, your script should not fail
    You are not allowed to use the SELECT and SHOW statements
    Your script should create these records:
        id = 1, name = “John”, score = 10
        id = 2, name = “Alex”, score = 3
        id = 3, name = “Bob”, score = 14
        id = 4, name = “George”, score = 8

</td>
</tr>
<tr>
  <td>10</td>
  <td>10-top_score.sql</td>
  <td>Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    Results should display both the score and the name (in this order)
    Records should be ordered by score (top first)
    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>11</td>
  <td>11-best_score.sql</td>
  <td>Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    Results should display both the score and the name (in this order)
    Records should be ordered by score (top first)
    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>12</td>
  <td>12-no_cheating.sql</td>
  <td>Write a script that updates the score of Bob to 10 in the table second_table.

    You are not allowed to use Bob’s id value, only the name field
    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>13</td>
  <td>13-change_class.sql</td>
  <td>Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>14</td>
  <td>14-average.sql</td>
  <td>Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

    The result column name should be average
    The database name will be passed as an argument of the mysql command

</td>
</tr>
<tr>
  <td>15</td>
  <td>15-groups.sql</td>
  <td>Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

    The result should display:
        the score
        the number of records for this score with the label number
    The list should be sorted by the number of records (descending)
    The database name will be passed as an argument to the mysql command

</td>
</tr>
<tr>
  <td>16</td>
  <td>16-no_link.sql</td>
  <td>Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    Don’t list rows without a name value
    Results should display the score and the name (in this order)
    Records should be listed by descending score
    The database name will be passed as an argument to the mysql command

In this example, new data have been added to the table second_table.

</td>
</tr>
</td>
</tr>
</tbody>
</table>

### \_By Giraluna Gomez - @Giraluna1
