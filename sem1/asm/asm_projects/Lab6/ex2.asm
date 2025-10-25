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
    s dw 1432h, 8675h, 0ADBCh
    len equ ($-s) / 2
    base dw 16
    d resd len
    temp resb 4
    
    
; segmentul de cod
segment code use32 class=code
start:
; ... 
    push d
    mov ecx, len
    mov esi, s
    
    main_loop:
        push ecx
        lodsw
        mov edi, temp
        mov ecx, 4
        store_loop:
            mov edx, 0
            DIV word[base]
            push eax
            mov al, dl
            stosb 
            pop eax
        loop store_loop
        
        push esi
        
        mov ecx, 4
        bubble1:
            mov esi, temp
            mov edi, temp + 1
        
            push ecx
            mov ecx, 3
            
            bubble2:
                cmpsb
                jl switch_t
                dec esi
                dec edi
                mov al, [edi]
                movsb
                mov [esi - 1], al
                
                switch_t:
            loop bubble2
            pop ecx
        loop bubble1
        
        mov esi, temp
        mov ebx, 0
        mov ecx, 4
        merge:
            shl eax, 8
            lodsb
            add bl, al
            
        loop merge
        
        pop esi
        pop ecx
        pop edi
        stosd
        push edi
        
    loop main_loop

    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
