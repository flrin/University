bits 32 ;asamblare și compilare pentru arhitectura de 32 biți
; definim punctul de intrare in programul principal
global start

; declaram functiile externe necesare programului nostru 
extern exit,printf ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import exit msvcrt.dll  ; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante

import printf msvcrt.dll
        
; segmentul de date in care se vor defini variabilele 
segment data use32 class=data
; ... 
    a dw 45
    b db 123
    c dd 0
    
; segmentul de cod
segment code use32 class=code
start:
; ... 

    ;c(0-3) = 1111
    ;c(4-7) = a(0-3)
    ;c(8-13) = 0000
    ;c(14-23) = a(4-13)
    ;c(24-29) = b(2-7)
    ;c(30-31) = 11
    
    ;1101_1110_0000_0000_1000_0000_1101_1111
    
    and ebx, 0
    or bx, 0000_0000_0000_1111b
    
    and ax, 0
    or ax, [a]
    and ax, 0000_0000_0000_1111b
    shl ax, 4
    or bx, ax
    
    and bx, 1100_0000_1111_1111b
    
    and eax, 0
    or ax, [a]
    and ax, 0011_1111_1111_0000b
    shl eax, 10
    or ebx, eax
    
    and eax, 0
    or eax, [b]
    and al, 1111_1100b
    shl eax, 22
    or ebx, eax
    
    or ebx, 0xC0000000
    
    or [c], ebx
   
   
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
