#include <stdio.h>

int main() {
	unsigned n;
	scanf("%d", &n);
	printf("%d.%d.%d.%d\n", (n >> 24) & 0xFF, (n >> 16) & 0xFF, (n >> 8) & 0xFF, n & 0xFF);
}
