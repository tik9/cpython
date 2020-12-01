

What data structure is needed to make a recursive procedure?
Question:

Answer:
O Stack
O Array
O Priority list

� Queue

What's the best use for a tree?

Answer:

� Recursion

CO Index records in a data base
� Print spooling

CO Image processing

� Multiplexing datagram


What's the temporary complexity of inserting an element in a balanced tree in the worst case?
 Answer:
O o(n^2)
O o(1)
O O(log n)
O O(n^n)


Given the following pseudo-code:
```
printTree(tree) {
 if (tree.hasLeft) {
  printTree(tree left)

 }

  if (tree.hasRight) {
   printTree(tree.right);

  }

  print(currentNode);
}
What would be the outcome for the following tree?
      10
   5       23
2     7  18   31
    5
```

� 2-5-5-7-10-18-23-31
� 10-5-23-2-7-18-31-5
� 2-5-7-5-18-31-23-10
� 5-2-7-18-31-5-23-10

Answer:

Answer:
If you had to order a very large array stored in a disk that doesn't fit in memory. What algorithm would you use?

O Bubble sort
O Merge sort
O Auick sort

O Heap sort

Answer:

?Find the next number in the sequence: 10, 37, 82,145,226,_ 
� 313
� 319
� 325
� 326
� 327
� 297

?Find the next number in the sequence: 1, 1, 2,-1,1,-2,-1,_
OC 2
O1
O 3
Ou
Oo
C 2

Answer:
Question:

?A scientist creates a colony of bacteria in a dish. This type of bacteria duplicates itself per minute. 
```
If at 9am the experiment started with a single cell and at 9:13 the dish was half-full, at what time will the dish be full
```
Answer:

� 9:14


Answer:
How many triangles are in this shape?

O15
O1
O�6�
O12
� 18


?If Susan finishes her homework, she'll go to the theatre.
Which one of the following statements is correct.

Answer:

oO Susan doesnt go to the theatre, then she didn't finish her homework.
oO If Susan doesn't finish her homework, she won't go to the theatre.
oO If Susan doesn't finish her homework, she will go to the theatre.

oO If Susan goes to the theatre, it means she finished her homework.
oO Susan is going to the theatre

During a single day, how many times do the hour hand and the minute hand of a clock meet at the same place?

Answer:
� 22

?There are 28 couples at a party. Each person shakes hands with every other person, except their own spouse
When the party is over, Mr. Smith asks each attendant how many hands they shook and everyone tells him a different number. How many hands did Mr. Smith shake

Answer:

� 54
Answer:
What character does jQuery use as a shortcut for jQuery?
� The $ Symbol

Question:

What effect does the use of filter() have in thefollowing line? S('div').filter('.nav')

Answer:

oO Removes all the elements �nav� in the page and leaves only the �div�

CO Filters all the �div� elements and returns all those which have the class �nav�
CO Filters all the �div� elements and returns those which have the id �nav�

CO Filters all the �div� elements and returns the first that has the class �nav�
Question:

Answer:
How do you get the first element �span� in the page that has the �green� class?

� $(span, .green, :first�)
� $(first.green span)
� $(span.green:first�)
CO $first(span.green�)

Answer:
What jQuery method should be used to deal with compability problems with other JavaScript libraries due to the use of the $ function?

� noConflictd)


What elements return the following selector?("div#intro .head")

Answer:
� The first element with id="head" contained inside any other div element with class="intro�

� All the elements with id="intro� or class="head"

 
� Allthe elements with Class="head� inside of the first div element with ii

� The first �div#intro element with class="head�
Answer:
What's the name of the library internally used by jQuery that allows the selection of DOM items?(similar to CSS selectors)

O Sizzle
O Selectivizr
� MotorSelector

O Riddle

?Implement a function that receives an array of integers arr and an integer int, which returns the number of occurrences of element int in array arr. For instance, given arr = [2,3,4,3,2,1] and int = 3, the function should return 2.
Answer:
Which one is not a JavaScript Framework?

� JQuery
O Hibernate
oO Prototype

� Dojo

What's the difference between undefined and null?

Answer:

oO There's no difference, they're the same data type
oO Undefined doesn't represent any type

oO Null doesn't represent any type

oO Undefined is a type whereas null is an object
Answer:
Which is not a good practice in JavaScript?

� Use global variables

� Use anonymous functions
O Use JavaScript namespacing
� Use Closures

What does the following code do?
```
function print() {

 var x = "5";

 alert (x+y);
}
 var x = 3;
 var y = 2;

print();

alert(x+y);
```
Answer:

O Gives an error in execution
� Prints 52 and then prints 5
� Prints 5 and then prints 5
� Prints 7 and then prints 5
What's true about functions in JavaScript?

Answer:

oO They all have parameters

oO You can pass a function as an argument in another function
� You can't define a function inside another one


What does "this" represent in the script? <a onclick="javascript:func(this)" >Example</a>

Answer:

CO It represents the node of the element that contains
oO It represents the window object context

CO Itrepresents the context of the node father

CO It represents the context for the current node content
Question:

Which of the following commands is used to connect as an anonymous user to a MySQL
server running in the localhost?

Answer:
© mysql -u anon
O mysal-u ''
O mysql

O mysal-u
Question:

Answer:

Which of the following commands is used to create a database called “abc"?
O CREATE -l abe

© DATABASE /anderson

CO CREATE DATABASE anderson
© mysql -s abe

Question:

Answer:
Which of the following is not a valid “aggregate” function?
© count

© sum
© MIN

© COMPUTE

Question:

Which of the following is a valid MySQL connection?

Answer:
© mysql> mysql -host=server -user=usuario -password=clave

© mysql> mysql -host = server -password —user = nombre

© mysql> mysql-h server-u usuario -p ~defaults-file=C:\my-options.

© mysql> mysql-h server-u usuario -p clave
?The TRUNCATE TABLE clause

Answer:
© Deletes the table

© Checks if the table has a PRIMARY KEY defined
© Deletes all the rows from a table

© Resets the autonumbers field's index
Can the UPDATE and SELECT clause be in a same SQL sentence?

Answer:
O They can be used together, even if a nested query is not used
O No, they cant

O You can if you use a nested query
?A trigger can belong to:

Answer:
© A single table in the database
© All the tables in the database
© More than one table in the database
With SQL, how can all the records from a table "People" be obtained where the value of the column "Name" starts with "a"?

Answer:

© SELECT * FROM People WHERE Name='a’

© SELECT * FROM People WHERE Name LIKE ‘%a!
© SELECT * FROM People WHERE Name LIKE 'a%'
© SELECT * FROM People WHERE Name="%a%'
How do I select all the records from a table called People where "lastname" is alphabetical between (including ends) "Richards" and “Smith’?

  

Answer:
CO SELECT lastname>'Richards' AND lastname«'Smith FROM People

CO SELECT * FROM People WHERE lastname BETWEEN 'Richads' AND ‘Smith’
© SELECT * FROM People WHERE lastname>'Richards’ AND apellido<’Smith’
O B and C are correct

CO Its not possible to do that for text fields
Which of the following statements is false?

Answer:
© MyISAM tables support foreign keys and relationship constraints

© MyISAM and InnoDB tables support compound keys creation

© MyISAM can only block at a table level while InnoDB can block at row level
© MyISAM tables don't support transactions
Question:
What is wrong with the following code?
```
class SomeClass{

 protected $_someMember;

 public function __construct()

 {

  $this->_someMember =1;

 }

 public static function getSomethingStatic(){
  return $this->_someMember * 5;
 }
}
```
 

Answer:
© The variable cannot be protected
© method cannot start with _

CO Sthis cannot be used from static

© $_someMember is a bad name for the variable
Question:

What is the difference between explode() y split()?

Answer:
© split partitions an array in more dimensions and explode partitions an array in more rows

© split does an "split" of a matrix, and explode expands a matrix

O split does a "split" of a string taking a string as an input, while explode partitions an string by a regular expresion

© split does a “split” of a string taking a regular expresion as an input, while explode partitions a string using a string
Question:

Which of the following functions can be used in PHP to determine if the type of a variable is a float?

Answer:
O settype()

CO is_double()

O settype()

O is date()

© A and B are correct
Answer:
What will the following code produce?
```
echo $_SERVER[REMOTE_ADDR}};
```

O Shows the visitor's IP address

O Shows the Web Server's IP address


?You've created a small MySQL database in a website and now the traffic has grown too much.
```
The server is working slowly. Here are some ways to reduce the load

The POSTs that the users do, are never repeated for this website.

Which one will give the LEAST improvement
```
Answer:
© Analyze the queries and add indexes

© Generate static pages in all the available places

© Move the database to another server and connect by TCP/IP
CO Add a cache object like Zend or APC
 

?PHP runs in several platforms, specially Unix. When you run a code developed in a Server Unix and you move it to a Server Windows, which of the following situations is a problem

Answer:

© Calling mail() will fail

© Executing code that calls OLE will fail
© The File Paths will stop working

© A and C are correct
In the following code, what does ""[0-9]+" match?preg_match('/*[0-9]+$/', $variable)
Answer:

O Any character

O A character between 0 and 9

© One or more characters between 0 and 9

© O or more characters between 0 and 9

© Any character between 0 and 9 followed by $
Which is the length of the shorter string that can match with the following regular expression?

preg_match('/*{a-g}+[3-9]"[A-Z]{2,10}$/')

Answer:
© 0 Characters
© 2Characters
© 8 Characters
© (Character
© 4 Characters
Which one of the following was NOT introduced in PHP 7?

Answer:
© Namespaces

© A function to perform integer divisions
© Group return expressions

© Anonymous classes
Which of the following is NOT a valid PHP comparison operator?

 
There's a requirement to send a message to a socket regardless of whether it is connected or not.
In that scenario, which of the following can be used?

Answer:
CO socket_sendto

© socket_send

© socket_send(0)

© socket_send y socket_sendto
© None of the above
If you want to stablish the modify (and access) date of a file, which of the following would you use?

Answer:
O filetime
O touch

CO filectime
O timestamp
Answer:
What does this line of code do?
```
$$variable = "yay";
```

CO Sets $var by reference

CO Sets $$var value

CO Sets a variable named after $var content

CO Sets the content of the "var" variable

If you want to determine if a cookie was previously set up, which of the following would you use?

Answer:
O iscookie()

O isset0)

O seteookie()

CO None of the above
Question:

Answer:


Given the following code, what would the output be?
```

FUNCTION TEST(){
ECHO Hello World!\n";

test();
}
```
© Hello World!

CO Nothing

© Runtime compilation error

CO helio world!
Question:

Answer:


What will be the output of the following code?
```
$var = ‘false’;

if ($var) {

 echo 'thisistrue’;
else {

 echo 'thisisfalse’;
}
```
O this is true
O this is false

© Runtime compilation error
Is there any problem with the following code?
```
class A {}
class B {}

class C extends A, B {}
```
Answer:
© The code is perfect

CO The classes can't be empty

© The class C can't inherit from A and B

© The private and public qualifiers are missing in the class
Given the following code, what would the output be?
```
$a = array(

echo count($a), "\n";
```Answer:

� Be restored using COMMIT
� Can't be restored

� Be restored with ALTER TABLE
� Be restored with a ROLLBLACK

A table that has been deleted with DROP TABLE can:
Answer:

� DISTINCTIVE
� DISTINCT
� DIFFERENT
� UNIQUE

Which SQL reserved word is used to retrieve unique values?
(not repeated)
 

Nombre |Apellido Salario Fecha Nacimiente

Pafsan [pcre sooo] 1704709
|__2|Pablo__|sanchez__�_�|__�5500]__15/09/1984]
| 4|Mariana_iudrez | 2500] 13/11/1981]
|_S[Maria [Calabro [| 8200[ NULL

|_6|Pauia[Sensini_ | 7500] 16/05/1988]
|__7[Romina [vidal | 9900] 05/02/1986]
|__8[Natalia_[Spalafucchetti_[ 1900[ NULL]
|__9Roberto [Cantalapietra | 4300] 26/04/1985

 

Considering the employees table, how would you bring the 3
employees with the highest salary?

Answer:

oO SELECT TOP 3 Employees ORDER BY Salario DESC

oO SELECT TOP 3 * FROM Employees ORDER BY Salario DESC
oO SELECT TOP 3 * FROM Employees ORDER BY Salario

oO SELECT * FROM Employees WHERE Salario >= 7500

oO SELECT TOP 3 FROM Employees ORDER BY Salario DESC
O_Id OrderDate OrderPrice Customer

1 12/11/2008 1000 Hansen
2 23/10/2008 1600 Nilsen
3 02/09/2008 700 Hansen
4 03/09/2008 300 Hansen
5 30/08/2008 2000 Jensen
6 04/10/2008 100 Nilsen
5 01/09/2008 1200 Gates
6 09/10/2008 800 Jobs

5 11/08/2008 2500 Gates
6 17/10/2008 400 Jobs

Given this table, how do we do to obtain the name and
the sum of all their orders only to those clients whose
sum of orders is less than 2000?

Answer:

oO SELECT Customer, SUM(OrderPrice) FROM Orders GROUP BY Customer HAVING SUM(OrderPrice) < 2000
oO SELECT Customer, SUM(OrderPrice) FROM Orders WHERE SUM(OrderPrice) < 2000 GROUP BY Customer
oO SELECT Customer, SUM(OrderPrice) FROM Orders GROUP BY O_Id HAVING SUM(OrderPrice) < 2000

oO SELECT Customer, SUM(OrderPrice) FROM Orders WHERE SUM(OrderPrice) < 2000 GROUP BY O_Id
Tabla Personas
P_Id

LastName

1 Hansen
2 Svendson
3 Pettersen

Tabla Ordenes
O_Id

BWNe

5

OrderNo

77895
44678
22456
24562
34764

FirstName Address

Ola Timoteivn 10
Tove Borgvn 23
Kari Storgt 20
P_Id

3

3

1

1

15

City

Sandnes
Sandnes
Stavanger

Given both tables above, we want to list all the people and their orders. If they don't
have orders, we also want them to show in the list.

Answer:

oO SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo FROM Persons JOIN Orders ON Persons.P_Id=Orders.P_Id

SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo FROM Persons INNER JOIN Orders ON Persons.P_Id=Orders.P_Id

ORDER BY Persons.LastName

SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo FROM Persons RIGHT JOIN Orders ON Persons.P_Id=Orders.P_Id

ORDER BY Persons.LastName

SELECT Persons.LastName, Persons.FirstName, Orders.OrderNo FROM Persons LEFT JOIN Orders ON Persons.P_Id=Orders.P_Id

ORDER BY Persons.LastName
Which of the following statements is false about DELETE FROM?

Answer:

� DELETE FROM can be used to delete the value of a column

� DELETE FROM can be used to delete multiple rows

� DELETE FROM can be used to delete one or more rows

oO DELETE FROM doesn't produce a different result from DELETE (without FROM)
Which of the followings is NOT a difference between TRUNCATE and DELETE?

Answer:

O TRUNCATE is a DDL (data definition language) command and DELETE is a DML (data manupulation language) command
O With DELETE you can specify a WHERE and with TRUNCATE you can't do it

� DELETE removes data only and TRUNCATE removes data and structure

O With TRUNCATE you can't do ROLLBACK of the deleted data in a transaction and with DELETE you can do it.
What's the HAVING clause for?

Answer:

CO Itallows you to select different values

O It allows you to specify a search condition for the aggregate function
O It allows you yo make the JOIN of 2 or more tables

CO t's like the WHERE clause
Answer:

� CONSTRAINTs only for the columns
� CONSTRAINTs only for the tables

� CONSTRAINTs for columns and tables
� None of the above

In SQL it's possible to create:
A current client of BairesDev is having difficulty deploying applications quickly into their production environment. Without knowing all of the details, what would
be an initial solution to propose?

Answer:
oO Present a DevOps Engineer to extend their current team to evaluate their current CI/CD and improve it

� Propose a two-week discovery to analyze their current roadmap and technology ecosystem, look for improvement opportunities
and then propose a team

� A and B only
oO Convert their current platform into a new platform, and propose a new technology stack to support it

� All of the above
 

A potential US client is evaluating nearshore outsourcing with BairesDev. Which of the following is NOT a benefit that nearshore outsourcing in Latin America provides?

Answer:

oO Time zone alignment, to allow real-time communication

oO Competitive rates, approximately 40-50% lower than local hiring markets
oO Awide pool of engineering talent due to broad geographical reach

oO The ability to do follow-the-sun technical support on a 24-hour basis

oO Shorter flights versus Eastern Europe
Answer:


Which of the following companies has the 2nd largest market share in the Cloud platform providers market?
O Microsoft
O Google
� Amazon

� |BM

� Facebook


Answer:
� 20
� 40
� 1500

� 100000

O 6nillion

Approximately, how many programming languages
exist for currently used applications?
How many LinkedIn connections do you think a mid-level IT
Recruiter with 3 years of experience would usually have?

Answer:
� 100
� 200
� 400
� 1000

� 15000
Answer:

� Users

� Customers

O Testers

� Developers

oO Unity department

There is a type of test known as Unit Test
This test is usually performed by...
Answer:

oO Montevideo, Uruguay
oO Florianopolis, Brazil
oO DF, Mexico.

oO La Paz, Bolivia

oO Paramaribo, Suriname

If you had to build a team of 20 bilingual Android

Developers in a single location in order to provide services to
a client in the United States, which of the following locations
would you say is the best to set up the team?
Answer:

O Fixed Price Projects

CO Time & Materials Projects
oO Staff Augmentation Projects
oO Detopropinos Projects

� PHP Projects

In theory, which one of the following types of projects would
be expected to have higher gross margins?
Answer:

O SharePoint
O Jira

� svn

� Outlook
O TaskRabbit

Which of the following tools used currently to manage the
development team tasks backlog is more popular?
What is the gross margin of a project whose revenue is
$6000 a month and cost is $4000 a month?

Answer:
� 66%
� 30%
� 25%

� None of the above

� 150%
What does the concept of business farming mean?

Answer:

� To generate new clients

oO To generate new positions on existing clients
oO That the project's team works overtime

oO To rotate the project's team with some frequency

O To increment the close ratio for new prospects
Which of the following roles would usually be considered the
most commercial role in a Software Company?

Answer:

OC Project Manager

� Senior Architect

� Team Leader

OC Engagement Manager
� Lead Developer
Answer:

oO Gray box testing

� Black box testing
� White box testing
oO Compatibility testing
� Performance testing

There is a Testing method usually used to verify a code,
among other things.
How is this Testing method called?
Question:

Answer:

� on'2)
O on)

oO O(n log n)
oO O(n4n)

What's the temporary complexity of the Merge Sort
algorithm in the worst case?
What method would you use to search a
number in an organized array of numbers

Answer:

C) Lineal Search

C) Fill in a hash table and then search by that hash
C) Fill in a binary tree and then search in the tree
�) Binary Search
What method would you use to search a
number in an organized array of numbers

Answer:

� Lineal Search

CO Fillin a hash table and then search by that hash
CO Fill in a binary tree and then search in the tree
� Binary Search
Assuming that the executing time of an algorithm
has a quadratic growth rate. For an input size of
1000 it has an execution time of 20 ms. Which
would be your estimate time of execution for an
input of size 10000?

Answer:

� 400 ms
� 4000 ms
� 200ms
� 2000 ms
