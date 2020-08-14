setwd("C:/Users/naman/Desktop/LECTURES/LECTURES-sem5/dm/Experiment 7")
data <- c(2,4,10,12,3,20,30,11,25)
k<-2

c<-0
m1<-3
m2<-4
K1o<-c()
K2o<-c()

while (TRUE){
  K1<-c()
  K2<-c()
  for (val in data) {
    if(abs(val-m1)<=abs(val-m2)){
      K1<-append(K1,val)
    }
    else{
      K2<-append(K2,val)
    }
  }
  m1<-mean(K1)
  m2<-mean(K2)
  
  if(c!=0){
    
    if(K1o==K1 & K2o==K2){
      break
    }
  }
  K1o<-K1
  K2o<-K2
  c<-c+1
}
K1o
K2o
c

