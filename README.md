
# exprassemble

Generate 8086 code for a given infix expression 

It creates .asm yet it can't print the output 
## Steps

Implemented with stack based algorithm, pseudocode from [cs.arizona.edu](https://www2.cs.arizona.edu/classes/cs127b/fall15/infix.pdf)

1. Read infix expression
2. Tokenize 
3. Infix to postfix
4. Postfix to assembly 
5. Write output 

## Requirements

python3 


## Run 

`python3 exprassemble.py input_file_name`

the output will be in out.asm 

## Assumptions

- The expression is hexadecimal
- It uses +, *, / operations and parantheses
- Given infix expressions are valid. Invalid expressions will raise an exception and print an error log 
- All values and results of operations will fit into 16 bits



