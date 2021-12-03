# Programming With Python: Files and Exceptions
## Introduction:
In this module we will cover 3 main pieces, working with text files in Binary, structured error handling, and creating advance GitHub pages.  You’ll get a look in to the different ways text files are used an how Binary can effectively be used with them too. Then we’ll look errors in code and how to structure it to help out others who might be using your code down the line. Lastly we’ll dive into some other features of GitHub and how you can use them.
## What Was Learned:
## Working with Text Files
When working with text files, there are many ways to use. Early on we learned that you could read, write, or append the data within a file. Later we learned how to save data to these files and take them back out too. Last week we learned functions which can be used in tandem with text files to create simple codes that save your data and run your script in a more concise manner.	When you want to use data from a text file, you can read the data to utilize it without editing it. If there was no data in a file you read, it will return an error message to you. The Append mode with add data to the file while write will reset the file and add in what you enter.
## Reading Data
There are many ways to read files but one main way is to use a readline() function. It goes through a line of data and then will proceed to the next line. To get through all the lines, a while loop is often used. This ensures all the lines of data will be viewed. After readline() is readlineS(). This reads all the lines in the file and returns a list.
One more option is a for loop. This will go through the data for however long is specified and automatically close the file at the end of the data.
## Combining Reading and Writing
One can combine reading and writing functions into one or in multiple. Either way works equally well, it is the coder’s choice. In this, Data is optional as if in read mode, you wouldn’t want to pass over any data. 
## Binary Files
Binary Files are the 2nd option for storing data in a file, the first is plain text. Binary allows the data to be obscured so that someone couldn’t open it up and view it. It also can condense the data if there’s a large amount of data. To use it, add a “b” after the “a” “r” “w” when working with a file
Code can also be imported form another file using Pickle. This code can be in plain text or in Binary. When obscured, you can’t always tell how many lines are really in the file because of how it is read.
## Lab 7.1
In Lab 7.1, the goal was to save data in Binary for to a file and pull in code from another via Pickle. This took some time as I had to research it a bit to understand what was needed. Once the details were gotten though, it wasn’t difficult to make the code function.
## Structured Error Handling
When a human might be involved in the code, there should be a try-except block as you don’t know what they might do to mess up the code. Try-except blocks are a good way to trap this error when they happen as it becomes easily identifiable where something went wrong for the other user. It has become standard practice to include these.
Exceptions are the built-in class that are used to hold information about an error. These are automatically created by Python when an error is encountered. This help pinpoint the location of the error and help others solve the problem 
One can make more specific exceptions to catch specific errors that might happen. 
There are many base classes built in for exceptions, but one can also make a custom class if they desire. These are helpful when making a particular code that might have uncommon bugs. This why there are often many testers of code to hopefully catch all potential errors.
## Advanced GitHub Pages
GitHub also allows you to make more advance pages on the site to share more information. You’re able to than edit a webpage and add in the content that you want to share. The main thing is that you can add in code samples to show and help explain different concepts. You can even add images on GitHub
## Pickling
One site i liked to learn about Pickling was https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy. They laid out the details well and made it easy to understand what was happening with the examples.
## Structured error handling
I also like the same site for structured error handling. https://docs.python.org/3/tutorial/errors.html. They make it simple to understand the concepts and overall makes it easy.
## Summary
Overall in this module we reviewed what we knew about text files, than we dove into how you can use text files with Binary. Then we did an overview of errors and how to use structure error handling to improve code when put out into the world for others to use. Lastly we looked at Github and the advance features that can be used on there.
