from execute import BasicExecute
from lexer import BasicLexer
from parser import BasicParser

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    print('Bro Language')
    env = {}

    # tree = parser.parse(lexer.tokenize('x=1'))
    # BasicExecute(tree, env)

    # while True:
    #
    #     try:
    #         text = input('Bro Language > ')
    #
    #     except EOFError:
    #         break
    #
    #     if text:
    #         tree = parser.parse(lexer.tokenize(text))
    #         BasicExecute(tree, env)

    text = ['a=10', 'b=20', 'c=a*b', 'c']

    if text:
        for x in text:
            tree = parser.parse(lexer.tokenize(x))
            BasicExecute(tree, env)
