A = [1 0 -2; 2 1 3; 0 1 0]
B = [2 1 1; 1 0 -1; 1 1 0]
C = A - B
D = A * B
E = A .* B

x = 0
y = 0

for i = 1:3
  x += A(1, i) + B(i, 2)
  y += A(i, 2) + B(3, i)
endfor

A + A'
C + C'
E + E'

