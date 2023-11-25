n = length(belexarhivaBELEX15);

targets = zeros(2, n-11);
inputs = zeros(6, n-11);

for i = n:-1:11
    % Postavljanje targeta
    if belexarhivaBELEX15(i, 3) > 0
        targets(:, i-10) = [1, 0];
    else
        targets(:, i-10) = [0, 1];
    end
    
    % Postavljanje inputa
    
    % Simple 10-day moving average, weighted 10-day moving average, Stohastic K 
    sma = 0;
    wma = 0;
    k = 1;
    stoc_max = belexarhivaBELEX15(i-1, 5);
    stoc_min = belexarhivaBELEX15(i-1, 6);
    for j = i-10:i-1
        sma = sma + belexarhivaBELEX15(j, 2);
        wma = wma + k*belexarhivaBELEX15(j, 2);
        k = k + 1;
        if belexarhivaBELEX15(j, 6) < stoc_min
            stoc_min = belexarhivaBELEX15(j, 6);
        end
        if belexarhivaBELEX15(j, 5) > stoc_max
            stoc_max = belexarhivaBELEX15(j, 5);
        end
    end
    inputs(1, i-10) = sma / 10;
    inputs(2, i-10) = wma / 55;
    inputs(3, i-10) = (belexarhivaBELEX15(i-1, 5) - stoc_min) * 100 / (stoc_max - stoc_min);
    % Momentum
    inputs(4, i-10) = belexarhivaBELEX15(i-1, 2) - belexarhivaBELEX15(i-2, 2); 
    % Larry William's R
    inputs(5, i-10) = (stoc_max - belexarhivaBELEX15(i-1, 5)) * 100 / (stoc_max - stoc_min);
    % ADO
    inputs(6, i-10) = (stoc_max - belexarhivaBELEX15(i-2, 5)) / (stoc_max - stoc_min);
end


