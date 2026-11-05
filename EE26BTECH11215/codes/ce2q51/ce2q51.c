// By Nehan mohammad
// 05-October-26, Monday, question no: 51

#include <stdio.h>
#include <math.h>

int main() {
    // Given data arrays
    double x[] = {1.0, 2.0, 4.0, 8.0};
    double p[] = {0.3, 0.1, 0.3, 0.3};
    int n = 4;

    double mean = 0.0;
    double mean_sq = 0.0;

    // Calculate mean and mean of squares
    for (int i = 0; i < n; i++) {
        mean += x[i] * p[i];
        mean_sq += (x[i] * x[i]) * p[i];
    }

    // Variance and standard deviation
    double variance = mean_sq - (mean * mean);
    double std_dev = sqrt(variance);

    printf("Mean: %.2f\n", mean);
    printf("Variance: %.2f\n", variance);
    printf("Standard Deviation: %.1f\n", std_dev);

    return 0;
}
