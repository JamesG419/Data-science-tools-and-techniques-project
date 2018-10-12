data = read.csv('State Data.csv', header = T, stringsAsFactors = F)

population = as.numeric(data[16,(6:13)])
years = c(2010,2011,2012,2013,2014,2015,2016,2017)

floridaData = data.frame(years = years, population = population)

model = lm(population ~ years, data = floridaData)

prediction2020 = as.numeric(2020 * model$coefficients[2] + model$coefficients[1])
prediction2020 

print(summary(model))


prediction2023 = as.numeric(2023 * model$coefficients[2] + model$coefficients[1])
prediction2023