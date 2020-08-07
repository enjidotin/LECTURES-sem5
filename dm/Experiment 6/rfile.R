setwd("C:/Users/naman/Desktop/LECTURES/LECTURES-sem5/dm/Experiment 6")
x <- read.table("sample1.csv",header=TRUE,sep=",")
train <- as.data.frame(x[1:14,])
testd <- as.data.frame(x[15:15,])
train
testd
prob <- table(train$Enrolls)
prob<-prob/14
prob
ageprob <- table(train[,c("Enrolls","Age")])
ageprob <- ageprob/rowSums(ageprob)
ageprob
incomeprob <- table(train[,c("Enrolls","Income")])
incomeprob <- incomeprob/rowSums(incomeprob)
jobsprob <- table(train[,c("Enrolls","Jobsatisfaction")])
jobsprob <- jobsprob/rowSums(jobsprob)
desireprob <- table(train[,c("Enrolls","Desire")])
desireprob <- desireprob/rowSums(desireprob)
incomeprob <- table(train[,c("Enrolls","Income")])
incomeprob <- incomeprob/rowSums(incomeprob)


incomeprob
jobsprob
desireprob

testd
ageyesprob <- ageprob["Yes","<=30"]
ageyesprob
jobsyesprob <- jobsprob["Yes","Yes"]
jobsyesprob
desireyesprob <- desireprob["Yes","Fair"]
desireyesprob
incomeyesprob <- incomeprob["Yes","Medium"]
incomeyesprob

ansyes <- ageyesprob*jobsyesprob*desireyesprob*incomeyesprob
ansyes


agenoprob <- ageprob["No","<=30"]
agenoprob
jobsnoprob <- jobsprob["No","Yes"]
jobsnoprob
desirenoprob <- desireprob["No","Fair"]
desirenoprob
incomeNoprob <- incomeprob["No","Medium"]
incomeNoprob

ansno <- agenoprob*jobsnoprob*desirenoprob*incomeNoprob
ansno
install.packages("e1071") 
library("e1071")
