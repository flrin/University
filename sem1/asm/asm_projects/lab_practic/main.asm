bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fprintf, scanf, fopen, fclose, printf          ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fprintf msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    file_descriptor resd 1
    file_name db "text.txt", 0
    read_format db "%llx", 0
    fprint_format db "%s", 0
    acces_mode db "w", 0
    letter resb 2
    print_format db "%s", 0
    secret resb 100
    letter_count resb 1

; our code starts here
segment code use32 class=code
    start:
        push acces_mode
        push file_name
        call [fopen]
        add esp, 4 * 2
        
        mov [file_descriptor], eax
        
        push secret
        push read_format
        call [scanf]
        add esp, 4 * 2
        
        mov ebx, 0
        mov esi, secret
        

        
        
        mov esi, secret

        decoding_loop:
            xor eax, eax
            lodsb
            cmp al, 0
            je finnish_word
            
            mov byte[letter], al
            mov byte[letter + 1], 0

            
            push letter
            push fprint_format
            push dword[file_descriptor]
            call [fprintf]
            add esp, 4 * 3
            
            
            xor ecx, ecx
        loop decoding_loop
        finnish_word
    
        push dword[file_descriptor]
        call [fclose]
        add esp, 4
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
