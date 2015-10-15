import ply.lex as lex
tokens=["ID","OP"]
t_ID = r'[a-z]+'
t_OP = r'\*\*|\*|--|-|\+|<|>'

lexer = lex.lex()
lexer.input("a*b---c**d")
print([(i.value, i.type) for i in lexer])
