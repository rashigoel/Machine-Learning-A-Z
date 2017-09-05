#Importing dataset
dataset = read.csv("Data.csv")

#For missing Age values 
dataset$Age = ifelse(is.na(dataset$Age),
              ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
              dataset$Age)


#For missing Salary values 
dataset$Salary = ifelse(is.na(dataset$Salary),
                 ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                 dataset$Salary)