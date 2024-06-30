A_values = [1, 2];
alpha_values = [1, 2];
N = 30;
T = 1;

figure;

plotCounter = 1;

for A = A_values
    for alpha = alpha_values
        [An, Fi] = fseries1(A, alpha, T, N);
        
        subplot(4,2,plotCounter); 
        stem(0:N, An);
        title(['A = ', num2str(A), ', \alpha = ', num2str(alpha)]);
        
        plotCounter = plotCounter + 1;

        subplot(4,2,plotCounter);
        stem(0:N, Fi); 
        title(['A = ', num2str(A), ', \alpha = ', num2str(alpha)]);
        
        plotCounter = plotCounter + 1;
    end
end

