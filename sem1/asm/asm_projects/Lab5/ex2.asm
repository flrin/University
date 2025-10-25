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
    def_list db '!','@','#','$','%','^','&','*'
    s db '+', '4', '2', 'a', '@', '3', '$', '*'
    len equ $-s
    d resb len
    
; segmentul de cod
segment code use32 class=code
start:
; ... 
    mov esi, 0
    mov ecx, len
    mov ebx, 0
    
    test_while:
        push ecx
        mov ecx, 7
        
        check_all:
            mov al, [def_list + ecx]
            cmp byte[s + esi], al
            jne gasit
            mov al, [s+esi]
            mov [d + ebx], al
            inc ebx
            gasit:
        loop check_all
        
        inc esi
        pop ecx
        
    loop test_while

    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
