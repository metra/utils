#include <stdio.h>
#include <time.h>
#define SLEEP_TIME 10000000 /* 10 millis */

/* An inaccurate stopwatch that keeps time
 * to the nearest ten millis.
 */

int main()
{
	struct timespec sleep_time;
	sleep_time.tv_sec = 0;
	sleep_time.tv_nsec = SLEEP_TIME;
	long millis_slept = 0;
	int millis, sec, min;

	while (1) {
		millis = millis_slept % 1000;
		sec = (millis_slept / 1000) % 60;
		min = millis_slept / 1000 / 60;
		printf("\r%d:%d.%d ", min, sec, millis);
		fflush(stdout);
		millis_slept += 10;
		nanosleep(&sleep_time, NULL)
	}

	return 0;
}
