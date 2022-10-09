{
 "cells": [
  {
   "cell_type": "raw",
   "id": "3e0167d1",
   "metadata": {},
   "source": [
    "1.What are the two values of the Boolean data type? How do you write them?\n",
    "Python boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. True or False. Generally, it is used to represent the truth values of the expressions. For example, 1==1 is True whereas 2<1 is False. \n",
    "We can evaluate values and variables using the Python bool() function. This method is used to return or convert a value to a Boolean value i.e., True or False, using the standard truth testing procedure. \n",
    "\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "fb72a13e",
   "metadata": {},
   "source": [
    "2.What are the three different types of Boolean operators?\n",
    "A boolean expression is an expression that yields just the two outcomes: true or false.\n",
    "There are three types of boolean operators:\n",
    "\n",
    "The AND operator (&& or \"and\")\n",
    "The OR operator (|| or \"or\")\n",
    "The NOT operator (not)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "051efd32",
   "metadata": {},
   "source": [
    "Make a list of each Boolean operator truth tables (i.e. every possible combination of Boolean\n",
    "values for the operator and what it evaluate ).\n",
    "True and True is True.\n",
    "\n",
    "True and False is False.\n",
    "\n",
    "False and True is False.\n",
    "\n",
    "False and False is False.\n",
    "\n",
    "True or True is True.\n",
    "\n",
    "True or False is True.\n",
    "\n",
    "False or True is True.\n",
    "\n",
    "False or False is False.\n",
    "\n",
    "not True is False.\n",
    "\n",
    "not False is True."
   ]
  },
  {
   "cell_type": "raw",
   "id": "cae30d02",
   "metadata": {},
   "source": [
    "4. What are the values of the following expressions?\n",
    "(5>4) and (3 == 5)\n",
    "not (5 > 4)\n",
    "(5 > 4) or (3 == 5)\n",
    "not ((5 >4) or (3 == 5))\n",
    "(True and True) and (True == False)\n",
    "(not False) or (not True)\n",
    "Output:\n",
    "False\n",
    "False\n",
    "True\n",
    "False\n",
    "False\n",
    "True"
   ]
  },
  {
   "cell_type": "raw",
   "id": "f8202958",
   "metadata": {},
   "source": [
    "5. What are the six comparison operators?\n",
    "Ans . ==, !=, <, >, <=, and >="
   ]
  },
  {
   "cell_type": "raw",
   "id": "ae93e6c4",
   "metadata": {},
   "source": [
    "Q6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.\n",
    "== is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable.\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "d775ceb4",
   "metadata": {},
   "source": [
    "7. Identify the three blocks in this code:\n",
    "spam = 0\n",
    "if spam == 10:\n",
    "print('eggs')\n",
    "if spam>5:\n",
    "print('bacon')\n",
    "else:\n",
    "print('ham')\n",
    "print('spam')\n",
    "print('spam')\n",
    "Output:ham\n",
    "spam\n",
    "spam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12cc5f7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "8.Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints\n",
    "Greetings! if anything else is stored in spam.\n",
    "Code:\n",
    "spam = input()\n",
    "\n",
    "if spam == 1:\n",
    "    print('Hello')\n",
    "elif spam == 2:\n",
    "    print('Howdy')\n",
    "else:\n",
    "    print('Greetings!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "718477e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "9.If your programme is stuck in an endless loop, what keys you’ll press?\n",
    "\n",
    "Ans  If program is stuck in endless loop we will press ctrl+c."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c48a7ab0",
   "metadata": {},
   "outputs": [],
   "source": [
    "10. How can you tell the difference between break and continue?\n",
    "Ans  The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
