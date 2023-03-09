---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lab 4

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/geosdemo/blob/master/docs/labs/lab4.ipynb)

## Submission instructions

1. Download the notebook from https://geosdemo.gishub.org/labs/lab4
2. Complete the lab questions
3. Restart Kernel and Run All Cells
4. Upload the notebook to your GitHub repository
5. Make sure the notebook has an `Open In Colab` badge. Click on the badge to make sure your notebook can be opened in Colab.
6. Submit the link to the notebook on your GitHub repository to Canvas

```{code-cell}
---
vscode:
  languageId: python
---
from datetime import datetime

now = datetime.now()
print(f"Submitted time: {now}")
```

## Question 1

**Personal Message:** Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 2

**Name Cases:** Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 3

**Famous Quote:** Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

```
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
```

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 4

**Stripping Names:** Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 5

**Names:** Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 6

**Your Own List:** Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 7

**Pizzas:** Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like _I like pepperoni pizza._

```{code-cell}
---
vscode:
  languageId: python
---

```

Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as _I really love pizza!_

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 8

**Animals:** Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

Modify your program to print a statement about each animal, such as _A dog would make a great pet._

```{code-cell}
---
vscode:
  languageId: python
---

```

Add a line at the end of your program stating what these animals have in common. You could print a sentence such as _Any of these animals would make a great pet!_

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 9

**Summing a Hundred:** Make a list of the numbers from one to one hundred, and then use `min()` and `max()` to make sure your list actually starts at one and ends at one hundred. Also, use the sum() function to see how quickly Python can add a hundred numbers.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 10

**Odd Numbers:** Use the third argument of the `range()` function to make a list of the odd numbers from 1 to 20. Use a `for` loop to print each number.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 11

**Threes:** Make a list of the multiples of 3 from 3 to 30. Use a `for` loop to print the numbers in your list.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 12

**Cube Comprehension:** Use a list comprehension to generate a list of the first 10 cubes.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 13

**Slices:** Using one of the programs you wrote in this lab, add several lines to the end of the program that do the following:

Print the message _The first three items in the list are:_. Then use a slice to print the first three items from that program’s list.

```{code-cell}
---
vscode:
  languageId: python
---

```

Print the message _Three items from the middle of the list are:_. Use a slice to print three items from the middle of the list.

```{code-cell}
---
vscode:
  languageId: python
---

```

Print the message _The last three items in the list are:_. Use a slice to print the last three items in the list.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 14

**Buffet:** A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

Use a for loop to print each food the restaurant offers.

```{code-cell}
---
vscode:
  languageId: python
---

```

The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 15

**Alien Colors:** Imagine an alien was just shot down in a game. Create a variable called `alien_color` and assign it a value of `green, yellow,` or `red`.

-   Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
-   Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 16

**Stages of Life:** Write an `if-elif-else` chain that determines a person’s stage of life. Set a value for the variable `age`, and then:

-   If the person is less than 2 years old, print a message that the person is a baby.
-   If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
-   If the person is at least 4 years old but less than 13, print a message that the person is a kid.
-   If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
-   If the person is at least 20 years old but less than 65, print a message that the person is an adult.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 17

**Favorite Fruit:** Make a list of your favorite fruits, and then write a series of independent `if` statements that check for certain fruits in your list.

-   Make a list of your three favorite fruits and call it favorite_fruits.
-   Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 18

**Hello Admin:** Make a list of five or more usernames, including the name `admin`. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

-   If the username is 'admin', print a special greeting, such as _Hello admin, would you like to see a status report?_
-   Otherwise, print a generic greeting, such as _Hello Jaden, thank you for logging in again_.

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 19

**Checking Usernames:** Do the following to create a program that simulates how websites ensure that everyone has a unique username.

-   Make a list of five or more usernames called `current_users`.
-   Make another list of five usernames called `new_users`. Make sure one or two of the new usernames are also in the `current_users` list.
-   Loop through the `new_users` list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
-   Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of `current_users` containing the lowercase versions of all existing users.)

```{code-cell}
---
vscode:
  languageId: python
---

```

## Question 20

**Ordinal Numbers:** Ordinal numbers indicate their position in a list, such as _1st_ or _2nd_. Most ordinal numbers end in _th_, except 1, 2, and 3.

-   Store the numbers 1 through 9 in a list.
-   Loop through the list.
-   Use an `if-elif-else` chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

```{code-cell}
---
vscode:
  languageId: python
---

```
