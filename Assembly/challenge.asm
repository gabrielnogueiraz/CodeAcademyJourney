section .data
    number dw 0b0000000000000000  ;
    result dw 0 ;

section .text
global _start

_start:
    mov ax, number ;
    xor cx, cx ;
    xor bx, bx ;

count_vacancies: 
    shr ax, 1 ;
    inc bx ;
    cmp bx, 18 ;
    jne count_vacancies ;

    mov result, cx

finish: 
    jmp finish
