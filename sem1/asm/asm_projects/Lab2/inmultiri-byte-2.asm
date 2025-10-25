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
    b db 3
    c db 2
    d dw 5
    
; segmentul de cod
segment code use32 class=code
start:
; ... 
    mov eax, 0
    mov edx, 0
    
    mov al, [b]
    mul byte[c]
    mov bx, ax
    
    mov ax, 0
    
    mov al, [a]
    mul byte[a]
    add ax, [d]
    mul word[d]
    
   div bx
   
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
