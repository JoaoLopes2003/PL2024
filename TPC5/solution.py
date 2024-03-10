import ply.lex as lex
import re
import sys

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
)

t_LISTAR = r'LISTAR'
t_SAIR = r'SAIR'

def t_MOEDA(t):
    r'MOEDA\s+(\d+[ec],?\s*)*'
    match = re.match(r'MOEDA\s+((\d+[ec]),?\s*)*', t.value)
    if match:
        moedas = re.finditer(r'(\d+[ec])', t.value)

        euros = 0
        centimos = 0
        for match in moedas:
            if match.group(1)[-1] == 'e':
                euros += int(match.group(1)[:-1])
            else:
                centimos += int(match.group(1)[:-1])
        t.value = str(euros) + 'e' + str(centimos) + 'c'
        return t
    else:
        print("Invalid MOEDA format:", t.value)

def t_SELECIONAR(t):
    r'SELECIONAR\s+\d+'
    match = re.match(r'SELECIONAR\s+(\d+)', t.value)
    if match:
        t.value = match.group(1)
        return t
    else:
        print("Invalid SELECIONAR format:", t.value)

# Define rule to ignore whitespace
t_ignore = ' \t\n'

# Define error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def parse_produtos(file):
    produtos = {}
     
    with open(file, 'r') as f:
        produtos_data = re.finditer(r'^(\d+) ([_\- \wÁÂÕÍáâõí]+) (\d+[ec])(\d+[c])?$', f.read(), re.MULTILINE)
    
        for match in produtos_data:
            if match.group(4):
                produtos[match.group(1)] = (match.group(2), match.group(3) + match.group(4))
            else:
                produtos[match.group(1)] = (match.group(2), match.group(3))
    
    return produtos

def adicionar_montante(saldo, montante):
    valor_antes = re.match('(\d+[ec])((\d+)[c])?', saldo)
    novo_montante = re.match('(\d+[ec])((\d+)[c])?', montante)

    euro1 = 0
    centimos1 = 0
    if valor_antes.group(1)[-1] == 'e':
        euro1 = int(valor_antes.group(1)[:-1])
        if valor_antes.group(2)[-1] != None:
            centimos1 = int(valor_antes.group(3))
    elif valor_antes.group(1)[-1] == 'c':
        centimos1 = int(valor_antes.group(1)[:-1])
    
    euro2 = 0
    centimos2 = 0
    if novo_montante.group(1)[-1] == 'e':
        euro2 = int(novo_montante.group(1)[:-1])
        if novo_montante.group(2)[-1] != None:
            centimos2 = int(novo_montante.group(3))
    elif novo_montante.group(1)[-1] == 'c':
        centimos2 = int(novo_montante.group(1)[:-1])

    return str(euro1 + euro2) + 'e' + str(centimos1 + centimos2) + 'c'

def comprar_produto(produtos, id, saldo):
    if not produtos[id]:
        return -1

    produto_preco = produtos[id][1]

    total = re.match('(\d+[ec])((\d+)[c])?', saldo)
    preco = re.match('(\d+[ec])((\d+)[c])?', produto_preco)

    euro1 = 0
    centimos1 = 0
    if total.group(1)[-1] == 'e':
        euro1 = int(total.group(1)[:-1])
        if total.group(2)[-1] != None:
            centimos1 = int(total.group(3))
    elif total.group(1)[-1] == 'c':
        centimos1 = int(total.group(1)[:-1])
    
    euro2 = 0
    centimos2 = 0
    if preco.group(1)[-1] == 'e':
        euro2 = int(preco.group(1)[:-1])
        if preco.group(2)[-1] != None:
            centimos2 = int(preco.group(3))
    elif preco.group(1)[-1] == 'c':
        centimos2 = int(preco.group(1)[:-1])
    
    if euro1 < euro2:
        return -1
    elif euro1 == euro2 and centimos1 < centimos2:
        return -1
    else:
        centimos = centimos1 - centimos2
        if centimos < 0:
            euros = euro1 - euro2 - 1
            centimos += 100
        else:
            euros = euro1 - euro2

    return str(euros) + 'e' + str(centimos) + 'c'

if __name__ == "__main__":

    # Carregar os produtos para memória
    produtos = parse_produtos(sys.argv[1])
    saldo = "0e0c"

    # Iniciar a máquina de venda
    stop = False
    while not stop:

        data = input("> ")
        lexer.input(data)

        while True:
            tok = lexer.token()
            if not tok:
                break
            elif tok.type == "LISTAR":
                for id, produto in produtos.items():
                    print(f'{id} -> {produto[0]} ({produto[1]})')
            elif tok.type == "MOEDA":
                saldo = adicionar_montante(saldo, tok.value)
                print(f'Saldo = {saldo}')
            elif tok.type == "SELECIONAR":
                troco = comprar_produto(produtos, tok.value, saldo)
                if troco == -1:
                    print("SALDO INSUFICIENTE.")
                else:
                    saldo = troco
                    print(f'Saldo = {troco}')
            elif tok.type == "SAIR":
                stop = True
                if saldo:
                    print(f'O seu troco é {saldo}.')
                else:
                    print("O seu troco é 0.")
                break
        
        print()
