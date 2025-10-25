N = 10000
tens = 0;

for i = 1:N
  v = randi(6, 1, 25);
  count = 0;

  for j = 1:25
    if v(j) == 6
      count++;
    endif
  endfor

    if count >= 10
      tens++;
    endif
  endfor

  tens = tens/N
