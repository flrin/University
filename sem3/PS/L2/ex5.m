N = 10000

two = 0;
three = 0;

for i = 1:N

  p2 = randi(6) * randi(6);
  p3 = p2 * randi(6);

  r = 0;
  while p2 > 0
    r = mod(p2, 10);
    p2 = floor(p2/10);
  endwhile

  if r == 1
    two++;
  endif

  r = 0;
  while p3 > 0
    r = mod(p3, 10);
    p3 = floor(p3/10);
  endwhile

  if r == 1
    three++;
  endif

endfor

two = two/N
three = three/N
