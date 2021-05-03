# Goal: in this script, I am analyzing the difference user behavior of members and casuals
# 1. By day in the week: would one group tend to 
# 2. By distance


# Install packages (only need to do it once)
#install.packages("readxl")
#install.packages('tidyverse')
#install.packages("ggplot2")


# read in libraries
library(readxl)
library(tidyverse)
library(ggplot2)

# read in dataset
data_april <- read_excel("C:/Users/hungd/Documents/Bike data with ride length/1. April 2020-divvy-tripdata.xlsx")
head(data_april) # check the first few rows of the dataset

# Part 1: By day in the weeksS
# EDA: exploratory data analysis
## 0. check for abnormalities: Missing values
nrow(data_april_new)
nrow(na.omit(data_april_new$end_station_name))
sum(is.na(data_april$end_station_name))
# choose to drop. fill, or leave it there

## 1. Summary statistics
summary(data_april) #get max,min,quantile,mean,median
str(data_april$ride_length) #look at the structure/format of column ride_length

data_april_new <- data_april%>%
  mutate(time_difference_minute=(ended_at-started_at)/60) #creating a new column time_difference_minute

data_april_new2s<-data_april_new%>%
  group_by(member_casual,day_of_week)%>%
  summarise(n=n()) # create a dataset for plotting

## 2. graphs
plot1 <- ggplot(data_april_new2,aes(x=day_of_week,y=n,fill=member_casual))+
  geom_bar(stat="summary")
