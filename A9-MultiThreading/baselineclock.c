#include<stdio.h>
#include<pthread.h>
#include<time.h>
#include<unistd.h>
#include<stdlib.h>
int secs, mins, hrs;

pthread_mutex_t lock;
	

void *seconds() {
	 pthread_mutex_lock(&lock);
	while(1) {
		
		sleep(1);
		system("clear");
		printf("\nClock\n\n");
		printf("%02d:%02d:%02d\n", hrs, mins, secs);
		
		secs++;
		
	}
	pthread_mutex_unlock(&lock);
}


void *minutes() {
	 pthread_mutex_lock(&lock);
	while(1) {
		if(secs == 60){
			
			secs = 0;
			mins++;	
			
				
		}
	}
	pthread_mutex_unlock(&lock);
}


void *hour() {
	 pthread_mutex_lock(&lock);
	while(1) {

		if(mins == 60){
			
			mins = 0;			
			
			
			hrs++;
		}

	}
	
pthread_mutex_unlock(&lock);
}



int main() {
	pthread_t t1,t2,t3;
	int a, b, c, d;
	
	printf("Enter starting hour: ");
	scanf("%d", &hrs);

	
	printf("Enter starting minute: ");
	scanf("%d", &mins);

	
	printf("Enter starting second: ");
	scanf("%d", &secs);	

	system("clear");
	pthread_mutex_init(&lock, NULL);
	a = pthread_create(&t1, NULL, seconds, NULL);
	b = pthread_create(&t2, NULL, minutes, NULL);
	c = pthread_create(&t3, NULL, hour, NULL);
	
	
	pthread_join(t1, NULL);	
	pthread_join(t2, NULL);
	pthread_join(t3, NULL);
	pthread_mutex_destroy(&lock);
		
	return 0;
}
