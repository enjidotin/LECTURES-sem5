ls()
setwd("C:/Users/naman/OneDrive/Desktop/LECTURES/dm/Experiment 5")
install.packages("rpart.plot") 
library("rpart") 
library("rpart.plot")
#Read the data 
play_decision <- read.table("DTdata.csv",header=TRUE,sep=",")
play_decision
summary(play_decision)
fit <- rpart(Play ~ Outlook + Temperature + Humidity + Wind, method="class", data=play_decision,control=rpart.control(minsplit=1),parms=list(split="information"))
summary(fit)             
?rpart.plot
rpart.plot(fit, type=5, extra=100)
newdata <-data.frame (Outlook="rainy", Temperature="mild", Humidity="high", Wind=FALSE)
newdata
predict(fit, newdata = list(),type = c("vector", "prob", "class", "matrix"))
predict(fit,newdata=newdata,type="prob")
predict(fit,newdata=newdata,type="class")
predict(fit,newdata=newdata,type="matrix")
predict(fit,newdata=newdata,type="vector")

