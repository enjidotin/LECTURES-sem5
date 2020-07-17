setwd("C:/Users/naman/Desktop/LECTURES/LECTURES-sem5/dm/Experiment 3")
df<- read.csv("customer.csv", stringsAsFactors = FALSE)
str(df)
summary(df)

install.packages("Hmisc")
require(Hmisc)
describe(df)
df$MonthlyCharges
is.na(df$MonthlyCharges)
sum(is.na(df$MonthlyCharges))
install.packages("tidyr") #for pipe operator
library(tidyr)
install.packages("dplyr") #for distinct function
library(dplyr)
df %>% distinct(MonthlyCharges)
df %>% summarise(n= n_distinct(MonthlyCharges))
df <- df %>% mutate(MonthlyCharges =replace(MonthlyCharges,is.na(MonthlyCharges),median(MonthlyCharges,na.rm = TRUE)))
is.na(df$TotalCharges) #detects only single null value
df%>% summarise(n=sum(is.na(TotalCharges)))
  
df %>% distinct(PaymentMethod)
df <- df %>%
  mutate(TotalCharges = replace(TotalCharges, (TotalCharges == "na"||TotalCharges == "N/A"), NA))
df%>% summarise(n=sum(is.na(TotalCharges)))
df$TotalCharges
df <- df %>%
  mutate(TotalCharges = replace(TotalCharges, TotalCharges == "na", NA)) %>%
  mutate(TotalCharges = replace(TotalCharges, TotalCharges == "N/A", NA))
df$TotalCharges<- as.numeric(df$TotalCharges)
df$TotalCharges
str(df)
df<-df %>% mutate_all(~ifelse(is.na(.x), mean(.x, na.rm = TRUE), .x))
df$PaymentMethod
df%>% summarise(n=sum(is.null(df$PaymentMethod)))
df <- df %>%
  mutate(PaymentMethod = replace(PaymentMethod, PaymentMethod == "--", NA)) %>%
  mutate(PaymentMethod = replace(PaymentMethod, PaymentMethod == "", 'unavailabe'))
df <- df %>%
  mutate(PercentChanges =(MonthlyCharges/TotalCharges)*100 )
df
