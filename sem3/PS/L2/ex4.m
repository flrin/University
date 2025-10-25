N = 10000
chance = 0;

for i = 1:N
  v = randperm(50);
  for j = 1:50
    if v(j) == j
      chance++;
      break;
    endif
  endfor
endfor

chance = N - chance;
chance = chance/N
