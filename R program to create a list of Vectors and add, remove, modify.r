vec1 <- c(1, 2, 3)
vec2 <- c(TRUE, FALSE)
lst = list(vec1, vec2)
vec3 <- c(1 + 3i)
lst[[3]]<- vec3
print ("Original List")
print (lst)
lst[[2]]<-NULL
print ("Modified List")
print (lst)
lst[[2]]<-c("TEACH", "CODING")
print ("Modified List")
print (lst)
