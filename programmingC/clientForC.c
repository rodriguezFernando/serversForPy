#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <string.h>
#include <arpa/inet.h>

#define SERV_PORT 8080
int main()
{
  int id, s;
  char *buf = "String test";
  char servip[] = "192.168.1.126";
  id = socket(AF_INET,SOCK_DGRAM,0);
  
  struct sockaddr_in servaddr;
  memset((void *)&servaddr, 0, sizeof(servaddr));
  servaddr.sin_family = AF_INET;
  servaddr.sin_port = htons(SERV_PORT);
  inet_pton(AF_INET,servip, &servaddr.sin_addr); 
  bind(id, (struct sockaddr *) &servaddr, sizeof(servaddr));


  s = sendto(id,(const char *)buf,strlen(buf),0,(struct sockaddr *) &servaddr,sizeof(servaddr));
    
    
}
    
  