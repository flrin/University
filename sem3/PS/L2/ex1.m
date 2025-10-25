p = 0.5;
N = 10000ex
a = 0;
b = 0;
c = 0;

for i = 1:N
  v = rand(1, 3);
  s = 0;
  for j = 1:3
    s += v(j) < p;
  endfor

  if s == 0
    c++;
  endif

  if s== 1
    a++;
  endif

  if s == 2
    b++;
  endif

endfor


a = a/N
b = b/N
c = c/N
