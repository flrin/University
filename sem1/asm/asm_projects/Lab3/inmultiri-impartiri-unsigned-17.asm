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
    b dd 6
    c db 3
    x dq 12

; segmentul de cod
segment code use32 class=code
start:
; ... 

    ;x-(a*a+b)/(a+c/a)
    mov eax, 0
    mov al, [c]
    div byte[a]
    mov ah, 0
    
    add al, [a]
    mov bl, al
    
    mov al, [a]
    mul byte[a]
    add ax, [b]
    
    div bl
    mov bl, al
    
    mov eax, [x]
    mov edx, [x+4]
    
    sub al, bl
    
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
