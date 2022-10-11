{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc135cca",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. Why are functions advantageous to have in your programs?\n",
    "Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e35b9e0c",
   "metadata": {},
   "source": [
    "2.When does the code in a function execute: when the function is defined or when the function is called?\n",
    "  The code in a function executes when the function is called, not when the function is defined."
   ]
  },
  {
   "cell_type": "raw",
   "id": "cbd0834b",
   "metadata": {},
   "source": [
    "3. What statement creates a function?\n",
    "The def statement defines (that is, creates) a function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf28c217",
   "metadata": {},
   "outputs": [],
   "source": [
    "4.What is the difference between a function and a function call?\n",
    "A function consists of the def statement and the code in its def clause.\n",
    "\n",
    "A function call is what moves the program execution into the function, and the function call evaluates to the function's return value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4744cfb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "How many global scopes are there in a Python program? How many local scopes?\n",
    "There is one global scope, and a local scope is created whenever a function is called."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38d9beec",
   "metadata": {},
   "outputs": [],
   "source": [
    "What happens to variables in a local scope when the function call returns?\n",
    "When a function returns, the local scope is destroyed, and all the variables in it are forgotten."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcc74c5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "What is a return value? Can a return value be part of an expression?\n",
    "A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a8210b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "If a function does not have a return statement, what is the return value of a call to that function?\n",
    "If there is no return statement for a function, its return value is None."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbe2e8ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "How can you force a variable in a function to refer to the global variable?\n",
    "A global statement will force a variable in a function to refer to the global variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89f6e147",
   "metadata": {},
   "outputs": [],
   "source": [
    "What is the data type of None?\n",
    "The data type of None is NoneType."
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
