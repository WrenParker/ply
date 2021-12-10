# -----------------------------------------------------------------------------
# Modified calc.py
#
# Modified code from 'examples' of the main ply project
# found at : https://github.com/dabeaz/ply/blob/master/example/calc/calc.py
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, "../..")

tokens = (
    'NAME', 'NUMBER', 'ADD', 'SUBTRACT', 'FROM', 'TO', 'GIVING'
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens

t_NAME = r'(A|B|C|D|E)'

t_ADD = r'add'
t_SUBTRACT = r'subtract'
t_FROM = r'from'
t_TO = r'to'
t_GIVING = r'giving'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
)

# dictionary of names
names = {}

def p_statement_assign(p):
    '''statement : NAME '=' expression
                 | expression GIVING NAME'''
    if p[2] == '=':
        names[p[1]] = p[3]
    elif p[2] == 'giving':
        names[p[3]] = p[1]


def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]



def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_add(p):
    "expression : ADD expression TO expression"
    p[0] = p[2] + p[4]

def p_expression_subtract(p):
    "expression : SUBTRACT expression FROM expression"
    p[0] =  p[4] - p[2]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
