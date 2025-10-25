%ifndef _TO_INT_ASM_
%define _TO_INT_ASM_

to_int:
    mov esi, [esp + 4]
    mov al, '-'
    mov edi, esi
    push esi
    scasb
    jnz positive_number
    
    mov edi, esi
    add esi, 1
    
    positive_number:
    mov edx, 0
    cld
    mov ebx, 10
    calc:
        mov eax, 0
        lodsb
        cmp al, 0
        jz finished
        
        sub eax, '0'
        xchg eax, edx
        push edx
        mul ebx
        pop edx
        add edx, eax
        
        xor ecx, ecx
        
    loop calc
    
    finished:
    mov eax, edx
    
    pop esi
    cmp esi, edi
    jnz skip_2compl
    
    not eax
    inc eax
    
    skip_2compl:
    
    ret 4
    
%endif