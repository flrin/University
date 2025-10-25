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
    a dw 8
    b dw -15
    c dw 2
    d dw 5
; segmentul de cod
segment code use32 class=code
start:
; ... 
    cwd
    ;mov eax, 0
    mov ax, [a]
    cwd
    add ax, [a]
    
    sub ax, [b]
    
    sub ax, [c]
    
    mov dx, [d]
    add dx, [d]
    sub ax, dx
    cwd
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
