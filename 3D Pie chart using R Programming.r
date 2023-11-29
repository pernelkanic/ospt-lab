library(plotrix)
geeks <- c(23, 56, 20, 63)
labels <- c("Mumbai", "Pune", "Chennai", "Bangalore")
piepercent<- round(100 * geeks / sum(geeks), 1)
pie3D(geeks, labels = piepercent,
 main = "City pie chart", col = rainbow(length(geeks)))
legend("topright", c("Mumbai", "Pune", "Chennai", "Bangalore"),
 cex = 0.5, fill = rainbow(length(geeks)))