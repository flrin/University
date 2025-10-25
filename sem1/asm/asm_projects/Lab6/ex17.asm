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
    s dd 12345678h, 1256ABCDh, 12AB4344h
    len equ ($-s) / 4
    d resw len
    temp resb 4
    
    
; segmentul de cod
segment code use32 class=code
start:
; ... 
    mov eax, 0
    mov esi, s
    mov edi, d
    mov ecx, len
    memo:
        movsw
        add esi, 2
    loop memo

    mov ecx, len
    bubble_1:
        push ecx
        
        mov esi, d
        mov edi, d + 2         
        
        mov ecx, len - 1
        bubble_2:
            cmpsw
            ja switch
            
            sub esi, 2
            sub edi, 2
            mov ax, [edi]
            movsw
            mov [esi - 2], ax
            sub esi, 2
            sub edi, 2
            
            switch:
        loop bubble_2
        pop ecx
    loop bubble_1
    
    mov esi, d
    mov edi, s
    mov ecx, len
    merge:
        movsw
        add edi, 2
    loop merge
    
    

    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
