bits 32 ;asamblare și compilare pentru arhitectura de 32 biți
; definim punctul de intrare in programul principal
global start

; declaram functiile externe necesare programului nostru 
extern exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import exit msvcrt.dll  ; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante

; segmentul de date in care se vor defini variabilele 
segment data use32 class=data
; ... 
    a dw 45
    b dw 123
    c dd 0
    
; segmentul de cod
segment code use32 class=code
start:
; ... 

    ;c(0-3) = b(5-8)
    ;c(4-8) = a(0-4)
    ;c(9-15) = a(6-12)
    ;c(16-31) = b(0-15)
    
    and bx, 0
    and ax, 0
    xor ax, [b]
    and ax, 0000_0001_1110_0000b
    shr ax, 5
    or bx, ax
    
    and ax, 0
    xor ax, [a]
    and ax, 0000_0000_0001_1111b
    shl ax, 4
    or bx, ax
    
    and ax, 0
    xor ax, [a]
    and ax, 0001_1111_1100_0000b
    shl ax, 3
    or bx, ax
    
    and eax, 0
    xor ax, [b]
    shl eax, 16
    
    xor [c], eax
    xor [c], bx
    
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
