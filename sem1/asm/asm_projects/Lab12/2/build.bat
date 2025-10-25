nasm -fobj main.asm
nasm -fobj to_int.asm
alink main.obj to_int.obj -oPE -subsys console -entry start