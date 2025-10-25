; The code below will print the message „Ana has 17 apples”
bits 32
global start        

; declare extern functions used by the program
extern exit, printf, scanf     ; add printf as extern function            
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell the assembler that function printf can be found in library msvcrt.dll
import scanf msvcrt.dll
segment data use32 class=data
; char arrays are of type byte
 a dw 2C1Dh 
 b db 7Ah, 3Bh , 12h
				; char strings for C functions must terminate with 0
segment  code use32 class=code
    start:
        mov al, 0x00FF
      
        

        ; exit(0)
        push dword 0      ; push on stack the parameter for exit
        call [exit]       ; call exit to terminate the programme
