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

# Lab 5

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/geosdemo/blob/master/docs/labs/lab5.ipynb)

## Submission instructions

1. Download the notebook from https://geosdemo.gishub.org/labs/lab5
2. Complete the lab questions
3. Restart Kernel and Run All Cells
4. Upload the notebook to your GitHub repository
5. Make sure the notebook has an `Open In Colab` badge. Click on the badge to make sure your notebook can be opened in Colab.
6. Submit the link to the notebook on your GitHub repository to Canvas

```{code-cell} ipython3
from datetime import datetime

now = datetime.now()
print(f"Submitted time: {now}")
```

## Question 1

**Person:** Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

```{code-cell} ipython3

```

## Question 2

**Favorite Numbers:** Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

```{code-cell} ipython3

```

## Question 3

**Glossary:** A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

- Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
- Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

```{code-cell} ipython3

```

## Question 4

**Glossary 2:** Now that you know how to loop through a dictionary, clean up the code from Question 3 by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

```{code-cell} ipython3

```

## Question 5

**Rivers:** Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

- Use a loop to print a sentence about each river, such as _The Nile runs through Egypt._
- Use a loop to print the name of each river included in the dictionary.
- Use a loop to print the name of each country included in the dictionary.

```{code-cell} ipython3

```

## Question 6

**Cities:** Make a dictionary called `cities`. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like `country`, `population`, and `fact`. Print the name of each city and all of the information you have stored about it.

```{code-cell} ipython3

```

## Question 7

**Rental Car:** Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

```{code-cell} ipython3

```

## Question 8

**Restaurant Seating:** Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

```{code-cell} ipython3

```

## Question 9

**Multiples of Ten:** Ask the user for a number, and then report whether the number is a multiple of 10 or not.

```{code-cell} ipython3

```

## Question 10

**Pizza Toppings:** Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

```{code-cell} ipython3

```

## Question 11

**Message:** Write a function called `display_message()` that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

```{code-cell} ipython3

```

## Question 12

**Favorite Book:** Write a function called `favorite_book()` that accepts one parameter, title. The function should print a message, such as `One of my favorite books is Alice in Wonderland`. Call the function, making sure to include a book title as an argument in the function call.

```{code-cell} ipython3

```

## Question 13

**T-Shirt:** Write a function called `make_shirt()` that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

```{code-cell} ipython3

```

## Question 14

**Large Shirts:** Modify the `make_shirt()` function so that shirts are large by default with a message that reads _I love Python_. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

```{code-cell} ipython3

```

## Question 15

**Cities:** Write a function called `describe_city()` that accepts the name of a city and its country. The function should print a simple sentence, such as `Reykjavik is in Iceland`. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

```{code-cell} ipython3

```

## Question 16

**City Names:** Write a function called `city_country()` that takes in the name of a city and its country. The function should return a string formatted like this:

```text
Santiago, Chile
```

Call your function with at least three city-country pairs, and print the values that are returned.

```{code-cell} ipython3

```

## Question 17

**Album:** Write a function called `make_album()` that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

```{code-cell} ipython3

```

## Question 18

**User Albums:** Start with your program from Question 17. Write a `while` loop that allows users to enter an album’s artist and title. Once you have that information, call `make_album()` with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the `while` loop.

```{code-cell} ipython3

```

## Question 19

**Messages:** Make a list containing a series of short text messages. Pass the list to a function called `show_messages()`, which prints each text message.

```{code-cell} ipython3

```

## Question 20

**Sending Messages:** Start with a copy of your program from Question 19. Write a function called `send_messages()` that prints each text message and moves each message to a new list called `sent_messages` as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

```{code-cell} ipython3

```

## Question 21

**Learning Python:** Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase _In Python you can. . .._ Save the file as _learning_python.txt_ in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the _with_ block.

```{code-cell} ipython3

```

## Question 22

**Learning C:** You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:

```text
message = "I really like dogs."
message.replace('dog', 'cat')
'I really like cats.'
```

Read in each line from the file you just created, _learning_python.txt_, and replace the word _Python_ with the name of another language, such as _C_. Print each modified line to the screen.

```{code-cell} ipython3

```

## Question 23

**Guest:** Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

```{code-cell} ipython3

```

## Question 24

**Guest Book:** Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

```{code-cell} ipython3

```

## Question 25

**Programming Poll:** Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

```{code-cell} ipython3

```

## Question 26

**Addition:** One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

```{code-cell} ipython3

```

## Question 27

**Addition Calculator:** Wrap your code from Question 26 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

```{code-cell} ipython3

```

## Question 28

**Cats and Dogs:** Make two files, _cats.txt_ and _dogs.txt_. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a `try-except` block to catch the `FileNotFound` error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the `except` block executes properly.

```{code-cell} ipython3

```

## Question 29

**Silent Cats and Dogs:** Modify your except block in Question 28 to fail silently if either file is missing.

```{code-cell} ipython3

```

## Question 30

**Common Words:** Visit Project Gutenberg (<https://gutenberg.org/>) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer. You can use the `count()` method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:

```{code-cell} ipython3
line = "Row, row, row your boat"
line.count('row')
```

```{code-cell} ipython3
line.lower().count('row')
```

Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.

Write a program that reads the files you found at Project Gutenberg and determines how many times the word `the` appears in each text. This will be an approximation because it will also count words such as `then` and `there`. Try counting `the`, with a space in the string, and see how much lower your count is.

```{code-cell} ipython3

```
