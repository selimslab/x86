import os 
import sys 
import tokenize 
from tokenize import STRING, NUMBER, NAME, OP, NEWLINE, ENDMARKER





class Symbol:
    LPAREN = "("
    RPAREN = ")"
    PLUS = "+"
    MUL = "*"
    DIV = "/"

class Op:
    ADD = "ADD"
    MUL = "MUL"
    DIV = "DIV"
    PUSH = "PUSH"

class SymbolToOp:
    Symbol.PLUS = Op.ADD
    Symbol.MUL = Op.MUL
    Symbol.DIV = Op.DIV




def write_asm(asm:str)->None:
    out_file = filename + ".asm"
    with os.open(out_file) as f:
        f.write(asm)
    


def postfix_to_assembly(postfix:str)->str:
    asm = []
    for c in postfix:
        print(c)



def tokens_to_postfix(tokens):
    priority = {Symbol.PLUS:1, Symbol.MUL:2, Symbol.DIV:2}

    postfix = ''
    stack = []

    for token in tokens:
        print(token)
        c = token.string
        if token.type is NAME or token.type is NUMBER :
            postfix += c  
        elif token.type is OP:
            if c is Symbol.LPAREN:
                stack.append(c)
            elif c is Symbol.RPAREN:
                operator = stack.pop()
                # pop until a left paren 
                while stack and operator is not Symbol.LPAREN:
                    postfix += operator
                    if not stack:
                        break
                    operator = stack.pop()
            else:
                # pop operators with gte priority
                while stack and priority.get(c,0) <= priority.get(stack[-1],0):
                    postfix += stack.pop()
                stack.append(c)

    while stack:
        postfix += stack.pop()

    return postfix


def token_generator(input_file:str):
    with tokenize.open(input_file) as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            yield token 

def get_input_file():
    if len(sys.argv) == 1:
        raise Exception("please provide input file")
    
    return sys.argv[1]

def main():
    input_file = get_input_file()

    lines = []
    line_tokens = []
    for token in token_generator(input_file):
        if token.type in {NEWLINE, ENDMARKER}:
            lines.append(line_tokens)
            line_tokens = []
        else:
            line_tokens.append(token)

    for line in lines:
        postfix = tokens_to_postfix(line)
        print(postfix)

    print("example.asm was generated.")

if __name__ == "__main__":
    main()
