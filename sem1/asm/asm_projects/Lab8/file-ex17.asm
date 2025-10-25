bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, fopen, fclose, fread, fprintf, scanf         ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fclose msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import scanf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    file_name dd "text17.txt", 0
    acces_mode dd "w", 0
    file_descriptor resd 1
    format db "%d ", 0
    num dd 0
    sformat db "%d", 0
    seven dw 7

; our code starts here
segment code use32 class=code
    start:
        push acces_mode
        push file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
        mov ecx, 1
        loop_1:
            push num
            push sformat
            call [scanf]
            add esp, 4 * 2
            
            cmp [num], word 0
            jz end
                mov eax, [num]
                div word[seven]
                cmp dx, word 0
                jnz skip
                    push dword[num]
                    push format
                    push dword[file_descriptor]
                    call [fprintf]
                    add esp, 4 * 3
            skip:
            inc ecx
        loop loop_1
        end:
        
        
        push dword[file_descriptor]
        call [fclose]
        add esp, 4 * 1
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
