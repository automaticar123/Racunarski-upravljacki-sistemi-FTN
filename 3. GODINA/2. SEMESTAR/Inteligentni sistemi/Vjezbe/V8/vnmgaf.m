function err = vnmgaf(x)

    global ulazi izlazi
    
    W1 = x(1:10)';
    B1 = x(11:20)';
    W2 = x(21:30);
    B2 = x(31);
    
    TSE = zeros(length(ulazi), 1);
    
    for i = 1:length(ulazi)
        Y1 = tansig(W1*ulazi(i) + B1);
        Y2 = purelin(W2*Y1 + B2);
        E = izlazi(i) - Y2;
        TSE(i) = E^2 * ulazi(i);
    end 
    
    err = mean(TSE);    
end