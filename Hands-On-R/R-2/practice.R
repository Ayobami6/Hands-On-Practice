# Importing the libraries 
library(janitor)
library(skimr)
library(tidyverse)
# setting working directory 
getwd()

setwd("/cloud/project/Course 7/Week 3")
getwd()
# reading in the dataset 
data_ <- read_csv('hotel_bookings.csv')

# viewing the top 5 rows of the dataframe 
head(data_)

#checking the structure 
str(data_)

# having a glimpse at the dataframe 
glimpse(data_)

# checking the cloumn names 
colnames(data_)

# sorting the leadtime in descendind order
new_d <- arrange(data_, desc(lead_time))

# using maximum and minimum function 
max(data_$lead_time)
min(data_$lead_time)

# Getting the mean for the lead_time 
mean(data_$lead_time)

# Filtering the dataset 
new_data_ <- filter(data_, data_$hotel == 'City Hotel')

# Permforming analysis 
analyzed_data <- data_ %>% 
  group_by(hotel) %>% 
  summarize(avg_lead_time=mean(lead_time),
            min_lead_time=min(lead_time),
            max_lead_time=max(lead_time))
# Plotting the average lead_time for the two hotels 

ggplot(analyzed_data, aes(x=hotel,
                          y=avg_lead_time)) +
  geom_bar(stat = 'identity') # using identity stat to be able to visualize the variables x and y

  
