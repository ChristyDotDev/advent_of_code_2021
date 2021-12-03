library(dplyr)

input = read.delim("input.txt", header = FALSE)

result <- input %>%
  mutate(increased= ifelse(V1 > lag(V1),1,0) ) %>%
  summarise(total=sum(increased, na.rm=TRUE))

print(result)