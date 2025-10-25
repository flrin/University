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
    a db 8
    b db 6
    c db -3
    d dd 2
    e dq -12

; segmentul de cod
segment code use32 class=code
start:
; ... 

    ;2/(a+b*c-9)+e-d
 
    mov al, [b]
    imul byte[c]
    add ax, [a]
    sub ax, 9
    
    mov bx, ax
    mov ax, 2
    idiv bx
    cwde
    
    add eax, [e]
    cdq
    add edx, [e+4]
    
    sub eax, [d]
    
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
