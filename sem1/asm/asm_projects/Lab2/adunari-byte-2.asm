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
    a db 1
    b db -15
    c db 2
    d db 5
; segmentul de cod
segment code use32 class=code
start:
; ... 
    cbw
    ;mov eax, 0
    mov al, [b]
    add al, [b]
    
    mov ah, [c]
    sub ah, [a]
    
    add al, ah
    add al, [d]
    cbw
    
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
