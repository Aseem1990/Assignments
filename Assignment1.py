#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*:Operator
'hello':string
-87.8:Integer(Value)
-:Operator
/:Operator
+:Operator
6:Operator2. What is the difference between string and variable?
String is any value that can be alphabet or collection of aplhabet written inside quotes '' or double quotes "" .
Variable is an entity which stores data which is just like a storage data.A variable can store a string.Hence we can say that a string is a subset of a variable.*
3. Describe three different data types.
There are totally 6 different types of data types with 6 subtypes .
The numeric data type consists of int,float,complex number
There are dictionary,boolean,set,tuples and sequence types as well.
Sequencetype consists of strings.tuples and list.4.4. What is an expression made up of? What do all expressions do?
In programming language terminology, an “expression” is a combination of values and functions that are combined and interpreted by the compiler to create a new value, as opposed to a “statement” which is just a standalone unit of execution and doesn't return anything5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?
An expression evaluates to a single value. A statement does not.6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
Output:We need to assign another value in bacon 7. What should the values of the following two terms be?
spam' + 'spamspam'
 'spam' * 3
spamspamspam
Output:spamspamspamWhy is eggs a valid variable name while 100 is invalid?
Variable names cannot begin with a number.9. What three functions can be used to get the integer, floating-point number, or string
version of a value?
The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.10. Why does this expression cause an error? How can you fix it?
 'I have eaten ' + 99 + ' burritos.'
 The expression causes an error because 99 is an integer, and only strings can be concatenated to other strings with the + operator. The correct way is I have eaten ' + str(99) + ' burritos.'.