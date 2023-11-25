global ulazi izlazi

ulazi = transpose(5.*rand(200, 1));
izlazi = ulazi + sin(ulazi);

[x, f] = ga(@vnmgaf, 31, gaoptimset('PlotFcn', @gaplotbestf, 'PopInitRange', [0;5], 'EliteCount', 10, 'HybridFcn', @fminsearch));

W1 = x(1:10)';
B1 = x(11:20)';
W2 = x(21:30);
B2 = x(31);

predicted = zeros(1, length(ulazi));

for i = 1:length(ulazi)
    Y1 = tansig(W1*ulazi(i) + B1);
    Y2 = purelin(W2*Y1 + B2);
    predicted(i) = Y2;
end

plot(ulazi, izlazi, 'b.', ulazi, predicted,' go')

