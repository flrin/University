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
    s1 db 1, 3, 6, 2, 3, 7
    len equ $-s1
    s2 db 6, 3, 8, 1, 2, 5
    d resb len
    
; segmentul de cod
segment code use32 class=code
start:
; ... 
    mov esi, 0
    mov ecx, len
    
    main_loop:
        mov al, byte[s1 + esi]
        cmp al, byte[s2 + esi]
        
        jle second_bigger
        ;first bigger
        mov al, byte[s1+esi]
        
        jmp first_bigger
        second_bigger:
        ;second bigger
        mov al, byte[s2+esi]
        first_bigger:
        
        mov byte[d+esi], al
        inc esi
    loop main_loop

    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
