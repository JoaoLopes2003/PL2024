import ply.lex as lex

reserved_keywords = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE'
}

tokens = (
    'SELECT', 'FROM', 'WHERE',
    'IDENTIFIER',
    'COMPARISON',
    'COMMA',
    'NUMBER',
)

t_COMPARISON = r'>='
t_COMMA = r','

# Define a rule for identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved_keywords.get(t.value.upper(), 'IDENTIFIER')
    return t

# Define a rule for literals
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define rule to ignore whitespace
t_ignore = ' \t\n'

# Define error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
data = "Select id, nome, salario From empregados Where salario >= 820"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)