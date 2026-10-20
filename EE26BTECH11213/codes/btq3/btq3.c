#include <stdio.h>
#include <math.h>

int main() {
    int n = 15; // Number of terms for convergence
    double sum = 0.0;
    double term = 1.0;

    for (int i = 1; i <= n; i++) {
        term /= i; // Calculates 1 / i! iteratively
        sum += term;
    }

    printf("Calculated Sum : %.6f\n", sum);
    printf("Theoretical e-1: %.6f\n", M_E - 1.0); //verifying with actual value

    return 0;
}

