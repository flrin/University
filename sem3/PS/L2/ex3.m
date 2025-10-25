N = 10000
a = 0;
b = 0;
n = 4

for i = 1:N
  v = randperm(n);

  for j = 1:n-1
    if v(j) == 1 && v(j+1) == 2
       a++;
       b++;
    endif

    if v(j) == 2 && v(j+1) == 1
      b++;
    endif
  endfor

endfor

a = a/N
b = b/N
