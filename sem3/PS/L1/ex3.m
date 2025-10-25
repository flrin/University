x = linspace(0,4,20);
f1 = @(x)x.^2
f2 = @(x)sqrt(x)
f3 = @(x)x

#plot(x, f1(x), x, f2(x), x, f3(x), ':')

fl = @(x, lambda)lambda*e.^(-lambda*x)

plot(x, fl(x, 1/2), "-", x, fl(x, 3), "--", x, fl(x, 7), ":")
