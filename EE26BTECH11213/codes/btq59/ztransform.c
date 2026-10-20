// By Jaideep
//  23/09/26


#include <stdio.h>
#include <stdbool.h>
#define MAX_N 15

int main(void) {
    const double threshold = 1.0 / 1024.0; /* 1 / 2^10 */
    double a_rec = 0.0;                    /* Initial condition: a_0 = 0 */
    int least_n = -1;

    printf("%-4s  %-20s  %-20s  %-14s  %-18s\n",
           "n", "a_n (Recurrence)", "a_n (Z-Transform)", "1 - a_n", "Condition < 2^-10");
    printf("----------------------------------------------------------------------------------\n");

    double p = 1.0; /* Stores 2^-n */
    printf("%-4d  %20.10f  %20.10f  %14.10f  %-18s\n",
           0, a_rec, 1.0 - p, 1.0 - a_rec, "False");

    for (int n = 1; n <= MAX_N; n++) {
        /* Recurrence relation: a_n = 0.5 * (1 + a_{n-1}) */
        a_rec = 0.5 * (1.0 + a_rec);

        /* Analytical closed-form: a_n = 1 - 2^-n */
        p *= 0.5;
        double a_closed = 1.0 - p;

        /* Direct positive difference since a_n < 1 for all n >= 0 */
        double err = 1.0 - a_rec;
        bool satisfied = (err < threshold);

        if (satisfied && least_n == -1) {
            least_n = n;
        }

        printf("%-4d  %20.10f  %20.10f  %14.10f  %-18s\n",
               n, a_rec, a_closed, err, satisfied ? "TRUE" : "False");
    }

    printf("----------------------------------------------------------------------------------\n");
    printf("Threshold 1 / 2^10 = %.10f\n", threshold);
    printf("Least integer value of n satisfying 1 - a_n < 1/(2^10): %d\n", least_n);

    return 0;
}