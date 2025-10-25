bits 32 
global start        

extern exit, scanf, fopen, fprintf, fclose
import exit msvcrt.dll 
import scanf msvcrt.dll   
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll

%include "str_min.asm"
%include "to_int.asm"

segment data use32 class=data
    string resb 100
    read_format db "%s", 0
    file_writing_format db "%x", 0
    file_descriptor resd 1
    acces_mode db 'w', 0
    file_name db "min.txt", 0

segment code use32 class=code
    start:
        push string
        push read_format
        call [scanf]
        add esp, 4 * 2
        
        push acces_mode
        push file_name
        call [fopen]
        add esp, 4 * 2
        mov [file_descriptor], eax
        
        push string
        call str_min
        
        push eax
        call to_int
        
        push eax
        push file_writing_format
        push dword[file_descriptor]
        call [fprintf]
        add esp, 4 * 3
        
        push dword[file_descriptor]
        call [fclose]
        add esp, 4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
