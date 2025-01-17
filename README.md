# Assignment #1
## Overview
Create a Key Word In Context (KWIC) index for any two chapters of an Icelandic saga
available at www.sagadb.org other than chapters 1 and 2 of Egli&#39;s saga.

# Assignment #2
## Overview
This assignment is to use the software package yacc or equivalent. There are two parts to the
assignment. The assignment is based on a simplified version of the assignment statement in the COBOL
language. In part one you are to design a grammar for a small subset of legal assignment statements in
COBOL. You are to turn in your grammar as a separate file attached to the email you send to turn in the
assignment. In part 2, you are to read a provided file of assignment statements, use Yacc and possible
other code to INTERPRET the assignment statements and then print a list of final values of all of the
identifiers in the program. You may assume that the only identifiers in this subset of COBOL are these 5:
A, B, C, D, and E. You may also assume that there are only two arithmetic operators: addition and
subtraction. Parentheses are allowed worth their usual meaning.

This was done using the [PLY(python lex yacc) library](https://github.com/dabeaz/ply), and python scripting to format tables and sort indices. Instructions to download and configure are found below.

## Additional Files

- README.md - markdown file (edited)

### Program #1
- WrenParkerIndex.py - Python source code for the chapter index'r
- chapters/Chapter1.txt - Chapter 1 of *The Story of Hrafnkell, Frey's Priest*
- chapters/Chapter3.txt - Chapter 3 of *The Story of Hrafnkell, Frey's Priest*
- output/Chapter1.csv - Comma separated value file of the index of chapter 1
- output/Chapter1_sorted.csv - Comma separated value file of the sorted index of chapter 1
- output/Chapter3.csv - Comma separated value file of the index of chapter 3
- output/Chapter3_sorted.csv - Comma separated value file of the sorted index of chapter 3
- example screenshots/Assignment1_example_screenshot1.png - Example screenshot of the terminal output for chapter 3
- example screenshots/Assignment1_example_screenshot2.png - Example screenshot of the terminal output for chapter 3 sorted
- Assignment Documents/assign01-CS410-2020lexkwiciselandicsaga.doc - Given description for Assignment 1

### Program #2
- WrenParkerCalc.py - Python source code for the calculat'r
- grammar.txt - the grammars for the calculator (also can be found in the source code to see how they're used)
- example screenshots/Assignment2_part1.png - Shows the Results of the example given for part 1
- example screenshots/Assignment2_part2.png - Shows the Results of the example given for part 2
- Assignment Documents/CS410programmingassgnment2yaccandCOBOLarithmeticexpressions.odt - Given description for Assignment 2

## Installation Instructions

0. Ensure python 3 and pip are installed
1. Clone the repo
	`$ git clone https://github.com/WrenParker/ply.git`
2. Run the install script in project root
	`py install.py`

## To run Assignment #1
0. Run the WrenParkerIndex.py script
	`py WrenParkerIndex.py`
1. To change the input, modify the input file on lines 88 & 97. Shouldn't be needed as both chapters print out unsorted and sorted in the order of 1, 1sorted, 3, 3sorted.

## To run Assignment #2
0. Run the WrenParkerCalc.py script
	`py WrenParkerCalc.py`
1. Enter in any desired input as described in the assignment 2 document (./Assignment Documents/assign01-CS410-2020lexkwiciselandicsaga.doc)

# Original Project
# PLY (Python Lex-Yacc)

Copyright (C) 2001-2020
David M. Beazley (Dabeaz LLC)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.  
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.  
* Neither the name of the David Beazley or Dabeaz LLC may be used to
  endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Introduction
============

PLY is a 100% Python implementation of the common parsing tools lex
and yacc. Here are a few highlights:

 -  PLY is very closely modeled after traditional lex/yacc.
    If you know how to use these tools in C, you will find PLY
    to be similar.

 -  PLY provides *very* extensive error reporting and diagnostic
    information to assist in parser construction.  The original
    implementation was developed for instructional purposes.  As
    a result, the system tries to identify the most common types
    of errors made by novice users.  

 -  PLY provides full support for empty productions, error recovery,
    precedence specifiers, and moderately ambiguous grammars.

 -  Parsing is based on LR-parsing which is fast, memory efficient,
    better suited to large grammars, and which has a number of nice
    properties when dealing with syntax errors and other parsing problems.
    Currently, PLY builds its parsing tables using the LALR(1)
    algorithm used in yacc.

 -  PLY uses Python introspection features to build lexers and parsers.  
    This greatly simplifies the task of parser construction since it reduces
    the number of files and eliminates the need to run a separate lex/yacc
    tool before running your program.

 -  PLY can be used to build parsers for "real" programming languages.
    Although it is not ultra-fast due to its Python implementation,
    PLY can be used to parse grammars consisting of several hundred
    rules (as might be found for a language like C).  The lexer and LR
    parser are also reasonably efficient when parsing typically
    sized programs.  People have used PLY to build parsers for
    C, C++, ADA, and other real programming languages.

How to Use
==========

PLY consists of two files : lex.py and yacc.py.  These are contained
within the `ply` directory which may also be used as a Python package.
To use PLY, simply copy the `ply` directory to your project and import
lex and yacc from the associated `ply` package.  For example:

```python
from .ply import lex
from .ply import yacc
```

Alternatively, you can copy just the files lex.py and yacc.py
individually and use them as modules however you see fit.  For example:

```python
import lex
import yacc
```

If you wish, you can use the install.py script to install PLY into
virtual environment.

PLY has no third-party dependencies.

The docs/ directory contains complete documentation on how to use
the system.  Documentation available at https://ply.readthedocs.io

The example directory contains several different examples including a
PLY specification for ANSI C as given in K&R 2nd Ed.   

A simple example is found at the end of this document

Requirements
============
PLY requires the use of Python 3.6 or greater.  However, you should
use the latest Python release if possible.  It should work on just
about any platform.  

Note: PLY does not support execution under `python -OO`.  It can be
made to work in that mode, but you'll need to change the programming
interface with a decorator.  See the documentation for details.

Resources
=========

Official Documentation is available at:

* https://ply.readthedocs.io

More information about PLY can be obtained on the PLY webpage at:

* http://www.dabeaz.com/ply

For a detailed overview of parsing theory, consult the excellent
book "Compilers : Principles, Techniques, and Tools" by Aho, Sethi, and
Ullman.  The topics found in "Lex & Yacc" by Levine, Mason, and Brown
may also be useful.

The GitHub page for PLY can be found at:

* https://github.com/dabeaz/ply

Acknowledgments
===============
A special thanks is in order for all of the students in CS326 who
suffered through about 25 different versions of these tools :-).

The CHANGES file acknowledges those who have contributed patches.

Elias Ioup did the first implementation of LALR(1) parsing in PLY-1.x.
Andrew Waters and Markus Schoepflin were instrumental in reporting bugs
and testing a revised LALR(1) implementation for PLY-2.0.

Example
=======

Here is a simple example showing a PLY implementation of a calculator
with variables.

```python
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.
# -----------------------------------------------------------------------------

tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN',
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Precedence rules for the arithmetic operators
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names (for storing variables)
names = { }

def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

def p_error(p):
    print(f"Syntax error at {p.value!r}")

import ply.yacc as yacc
yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    yacc.parse(s)
```

Bug Reports and Patches
=======================
My goal with PLY is to simply have a decent lex/yacc implementation
for Python.  As a general rule, I don't spend huge amounts of time
working on it unless I receive very specific bug reports and/or
patches to fix problems. At this time, PLY is mature software and new
features are no longer being added.  If you think you have found a
bug, please visit the PLY Github page at https://github.com/dabeaz/ply
to report an issue.

Take a Class!
=============

If you'd like to learn more about compiler principles and have a go at
implementing a compiler, come take a course.
https://www.dabeaz.com/compiler.html.

-- Dave
