#include <stdlib.h>
#include <string.h>

#define N 30000000

int main() {
    int *x = malloc(N * sizeof(int));
    memset(x, 0, N * sizeof(int));
    return 0;
}