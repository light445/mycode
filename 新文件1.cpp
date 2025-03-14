#include <stdio.h>

main() {
	int i = 1, num1 = 0, num2 = 0;

	while (i <= 10) {
		if (i % 2 == 0) {
			num1 += i;
		} else {
			num2 += i;
		}
		i++;


	}
	printf("%d\n", num1);
	printf("%d", num2);
}