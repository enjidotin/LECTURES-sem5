install.packages("arules")
library("arules")
data("Groceries")
Groceries@itemInfo
rules<-apriori(Groceries,parameter = list(supp = 0.001, conf = 0.9))
inspect(head(rules))
