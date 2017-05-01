library(RcppCNPy)
library(plotrix)

data = npyLoad("/home/grzegorz/agh/prmiml/graphs/results.bin.npy")

for (i in 1:4) {
  matrix_data = matrix(data[i,], ncol=1000, byrow=TRUE)
  color2D.matplot(matrix_data)
}

pca  = prcomp(data, center = TRUE)
plot(predict(pca))
