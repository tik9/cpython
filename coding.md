You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive two-digit integer.

Guaranteed constraints:
10 ≤ n ≤ 99.

[output] integer

The sum of the first and second digits of the input number.

-----------------------------------------------------------------

Implement a function to calculate the average distance between three points in a single plane where the coordinates of these points are (x1, y1), (x2, y2), and (x3, y3).

Note: your answer will be considered correct if its absolute or relative error doesn't exceed 10-5.

Example

For x1 = 1, y1 = 2, x2 = 3, y2 = 4, x3 = 5, and y3 = 6, the output should be averagePlaneDistance(x1, y1, x2, y2, x3, y3) = 3.771236.

Input/Output

[execution time limit] 4 seconds (py3)

[input] float x1

Guaranteed constraints:
-1000 ≤ x1 ≤ 1000.

[input] float y1

Guaranteed constraints:
-1000 ≤ y1 ≤ 1000.

[input] float x2

Guaranteed constraints:
-1000 ≤ x2 ≤ 1000.

[input] float y2

Guaranteed constraints:
-1000 ≤ y2 ≤ 1000.

[input] float x3

Guaranteed constraints:
-1000 ≤ x3 ≤ 1000.

[input] float y3

Guaranteed constraints:
-1000 ≤ y3 ≤ 1000.

[output] float

The average distance between the three given points.

------------------------------
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. For instance: kayak or rotator. Implement a boolean function called isAlmostPalindrome(word) which returns true either if the word is a palindrome or if modifying just one character could make the word to be a palindrome; otherwise it will return false (when two or more characters must be changed to make the word as a palindrome).

For this exercise, it is assumed that all the characters of the word will be received in lower case. It is not required to make any check on the case (upper/lower).

Example

For word = "abccba", the output should be isAlmostPalindrome(word) = true.

It is already a palindrome.

For word = "abccbx", the output should be isAlmostPalindrome(word) = true.

It becomes a palindrome after modifying the character x to a.

For word = "abccfg", the output should be isAlmostPalindrome(word) = false.

There is no way to obtain a palindrome modifying just one character. At least two characters must be changed. For instance, the f to b and the g to a.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string word

A string consisting of lowercase English letters, which should be checked to be an almost palindrome.

Guaranteed constraints:
1 ≤ word.length ≤ 106.

[output] boolean

Whether the string word is an almost palindrome.
----------------------------------
Implement a function that receives an array of positive integers numbers with values between 1 and 5000 and returns the number that most frequently appears in the array. If there are two or more numbers that appear the same number of times, the function should return the lowest number that appears most.

Example

For numbers = [34, 31, 34, 77, 82], the output should be mostPopularNumber(numbers) = 34.
Number 34 appears two times when the rest numbers appear only once.

For numbers = [22, 101, 102, 101, 102, 525, 88], the output should be mostPopularNumber(numbers) = 101.
Both 101 and 102 appear two times, but 101 is lower than 102.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer numbers

Guaranteed constraints:
1 ≤ numbers.length ≤ 105,
1 ≤ numbers[i] ≤ 5000.

[output] integer

The lowest number that appears the most.
-------------------------------------
You are really interested in statistics, and your new project is to gather some information about the users of a big social network. More specifically, you want to know which countries these users are from. Using the social network's API, you managed to collect enough data to compose two tables users and cities, which have the following structures:

users:
id: the unique user ID;
city: the name of the city where this user lives;
cities:
city: a unique city name;
country: the name of the country where this city is located.
Given the tables users and cities, write a select statement that returns two columns id and country consisting of user ids and the countries where they live respectively. If a user's city is missing from the cities table, the country column should contain "unknown" instead.

Return the table sorted by users' ids.

Example

For the following table users

id	city
1	San Francisco
2	Moscow
3	London
4	Washington
5	New York
6	Saint Petersburg
7	Helsinki
and the following table cities

city	country
Moscow	Russia
Saint Petersburg	Russia
San Francisco	USA
Washington	USA
New York	USA
London	England
the output should be

id	country
1	USA
2	Russia
3	England
4	USA
5	USA
6	Russia
7	unknown