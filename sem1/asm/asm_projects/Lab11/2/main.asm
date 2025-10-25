bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf
import printf msvcrt.dll
import scanf msvcrt.dll         ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

%include "to_int.asm"
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    numbers resb 100
    text resb 10
    read_format db "%s", 0
    print_format db "%d",10,13, 0
    base db 10

; our code starts here
segment code use32 class=code
    start:
        read_numbers:
            push text
            push read_format
            call [scanf]
            add esp, 4 * 2
            
            cmp byte[text], '0'
            jz finish
            
            push text
            call to_int
            
            push eax
            push print_format
            call [printf]
            add esp, 4 * 2
            
            
            mov ecx, 0
        loop read_numbers
    
        finish:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
