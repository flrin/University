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
    a db 30
    b dw 6
    c dd -9
    d dq 111

; segmentul de cod
segment code use32 class=code
start:
; ... 

    ;(c+b)-a-(d+d)
    
    mov eax, [c]
    add ax, [b]
    
    sub al, [a]
    cbw
    cwde
    cdq
    
    mov ebx, [d]
    mov ecx, [d+4]
    
    add ebx, [d]
    adc ecx, [d+4]
    
    sub edx, ecx
    sbb eax, ebx
    
    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
