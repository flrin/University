function output = combi(n, k)

  output = n/k;
  for i = 1:(k-1)

    output *= (n-i)/(k-i);

  endfor

end
