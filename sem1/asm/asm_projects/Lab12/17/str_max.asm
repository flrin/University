bits 32

global _str_max

segment data public data use32
segment code public code use32

_str_max:
    mov ebx, [esp + 4 * 1]
    
    mov ecx, 8
    bubble_1:
        push ecx
        mov esi, ebx
        mov edi, ebx
        inc edi
        bubble_2:
            xchg esi, edi
            lodsb
            cmp al, 0
            je reached_end
            dec esi
            xchg esi, edi
            
            cmpsb
            jae skip_xchg
            
                dec esi
                dec edi
            
                mov al, [esi]
                xchg al, [edi]
                xchg [esi], al
                
                inc esi
                inc edi
            skip_xchg:
            xor ecx, ecx
        loop bubble_2
        reached_end:
        pop ecx
    loop bubble_1
    
    mov eax, ebx
    
    ret

