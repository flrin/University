bits 32

global start

extern printf,scanf,fprintf,fread,exit, fopen, fclose

import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import fread msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    filename db "text.txt", 0
    number_read_format db "%d", 0
    string_read_format db "%s", 0
    string_write_format db "%s",13, 10, 0
    acces_mode db "w", 0
    file_descriptor resd 1
    n resb 1
    string resb 10
    
segment code use32 class=code
    start:
    push acces_mode
    push filename
    call [fopen]
    add esp, 4 * 2
    
    mov [file_descriptor], eax
    
    push n
    push number_read_format
    call [scanf]
    add esp, 4 * 2
    
    read_loop:        
        push string
        push string_read_format
        call [scanf]
        add esp, 4 * 2
        
        cmp byte[string], "#"
        je exit_loop
        
        mov al, 0
        mov ebx, 0
        mov ecx, 100
        mov edi, string
        count_letters:
            scasb 
            je exit_count
            inc ebx
        loop count_letters
        
        exit_count:
        
        cmp bl, byte[n]
        jb word_too_small
        
            mov esi, string
            add ebx, string
            sub ebx, 1
            mov edi, ebx
            cmpsb
            jne not_same
                
                push string
                push string_write_format
                push dword[file_descriptor]
                call [fprintf]
                add esp, 4 * 3
                
        word_too_small:
        not_same:
        mov ecx, 0
    loop read_loop
    
    exit_loop:
    
    push dword[file_descriptor]
    call [fclose]
    add esp, 4
    
    push dword 0
    call [exit]