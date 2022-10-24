{
 "cells": [
  {
   "cell_type": "raw",
   "id": "a6558a1e",
   "metadata": {},
   "source": [
    "1. What exactly is []?\n",
    "The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value."
   ]
  },
  {
   "cell_type": "raw",
   "id": "85264217",
   "metadata": {},
   "source": [
    "2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the\n",
    "third value? (Assume [2, 4, 6, 8, 10] are in spam.)\n",
    "Output:[2, 4, 'hello', 8, 10]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05e9e236",
   "metadata": {},
   "outputs": [],
   "source": [
    "3. What does spam[int(int('3' * 2) // 11)] evaluate to?\n",
    "'d' (Note that '3' * 2 is the string '33', which is passed to int() before being divided by 11. This eventually evaluates to 3. Expressions can be used wherever values are used.)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "41d91b25",
   "metadata": {},
   "source": [
    "4. What is the value of spam[-1]?\n",
    "'d' (Negative indexes count from the end.)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "f12e6bd6",
   "metadata": {},
   "source": [
    "5. What is the value of spam[:2]?Let pretend bacon has the list [3.14,'cat'11,'cat' True] for next three questions\n",
    "['a', 'b']\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "82ad2c43",
   "metadata": {},
   "source": [
    "6. What is the value of bacon.index('cat')?\n",
    "A list of a returned value\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "a4adf156",
   "metadata": {},
   "source": [
    "7. How does bacon.append(99) change the look of the list value in bacon?\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.append(99) # append adds the item at the end of the list\n",
    "bacon"
   ]
  },
  {
   "cell_type": "raw",
   "id": "50af0ed5",
   "metadata": {},
   "source": [
    "8. How does bacon.remove('cat') change the look of the list in bacon?\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.remove('cat') # remove first occurrence of item\n",
    "bacon"
   ]
  },
  {
   "cell_type": "raw",
   "id": "d267d2fa",
   "metadata": {},
   "source": [
    "9. What are the list concatenation and list replication operators?\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "3e2b67ff",
   "metadata": {},
   "source": [
    "10. What is difference between the list methods append() and insert()?\n",
    "append() Appends object to the end of the list\n",
    "insert() Insert object before index"
   ]
  },
  {
   "cell_type": "raw",
   "id": "ceb03983",
   "metadata": {},
   "source": [
    "11. What are the two methods for removing items from a list?\n",
    "#remove(item) - removeds first occurence of a item\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.remove('cat')\n",
    "bacon\n",
    "[3.14, 11, 'cat', True]\n",
    "#pop() - Remove and returns item at index (default last).\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.pop()\n",
    "bacon\n",
    "[3.14, 'cat', 11, 'cat']"
   ]
  },
  {
   "cell_type": "raw",
   "id": "8765c204",
   "metadata": {},
   "source": [
    "12. Describe how list values and string values are identical.\n",
    "Both lists and strings can be passed to len()\n",
    "Have indexes and slices\n",
    "Can be used in for loops\n",
    "Can be concatenated or replicated\n",
    "Can be used with the in and not in operators"
   ]
  },
  {
   "cell_type": "raw",
   "id": "e333680a",
   "metadata": {},
   "source": [
    "13. What the difference between tuples and lists?\n",
    "Lists : are mutable - they can have values added, removed, or changed. lists use the square brackets, [ and ]\n",
    "Tuples : are immutable; they cannot be changed at all. Tuples are written using parentheses, ( and )"
   ]
  },
  {
   "cell_type": "raw",
   "id": "861c808a",
   "metadata": {},
   "source": [
    "14. How do you type a tuple value that only contains the integer 42?\n",
    "tuple = (42,)\n",
    "tuple\n",
    "(42,)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "efd478ce",
   "metadata": {},
   "source": [
    "15. How do you get a list value's tuples form?How do you get a tuple value list form?\n",
    "l1 = [2,3]\n",
    "l = tuple(l1)\n",
    "l\n",
    "(2, 3)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "120726fb",
   "metadata": {},
   "source": [
    "16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they\n",
    "contain?\n",
    "They contain references to list values"
   ]
  },
  {
   "cell_type": "raw",
   "id": "4505f740",
   "metadata": {},
   "source": [
    "17. How do you distinguish between copy.copy() and copy.deepcopy()?\n",
    "The copy.copy() function will do a shallow copy of a list,\n",
    "The copy.deepcopy() function will do a deep copy of a list. only copy.deepcopy() will duplicate any lists inside the list"
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
