PUSH 2

PUSH b

PUSH 1

POP CX
POP AX  
ADD CX
PUSH AX

POP CX
POP AX  
MUL CX
PUSH AX

PUSH 2

POP CX
POP AX  
DIV CX
PUSH AX
INT 20h