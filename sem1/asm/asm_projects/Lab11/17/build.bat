nasm -fobj en_main.asm
nasm -fobj str_min.asm
nasm -fobj to_int.asm
alink en_main.obj str_min.obj to_int.obj -oPE -subsys console -entry start