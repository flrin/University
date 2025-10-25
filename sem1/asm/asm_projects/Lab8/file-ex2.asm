bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, fopen, fclose, fread            ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fclose msvcrt.dll
import fread msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    con dd 0
    file_name dd "text2.txt", 0
    acces_mode dd "r", 0
    file_descriptor resd 1
    vowels dd "aeiou", 0
    format db "%d", 0
    text dd 0
    

; our code starts here
segment code use32 class=code
    start:
        push acces_mode
        push file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
        
        push dword[file_descriptor]
        push dword 100
        push dword 1
        push text
        call [fread]
        add esp, 4*4
        
        mov esi, text
        
        mov ecx, eax
        all_chars:
            push ecx
            mov edi, vowels
            lodsb
            mov ecx, 5
            repne scasb
            je continue
                inc dword[con]
            continue: 
            pop ecx
        loop all_chars
        
        
        push dword[con]
        push format
        call [printf]
        add esp, 4 * 2
        
        push dword[file_descriptor]
        call [fclose]
        add esp, 4 * 1
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
