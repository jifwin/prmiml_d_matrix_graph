library(RcppCNPy)
library(plotrix)
library(scatterplot3d)

data = npyLoad("/home/grzegorz/agh/prmiml/graphs/results.bin.npy")

for (i in 1:10) {
  matrix_data = matrix(data[i,], ncol=1000, byrow=TRUE)
  color2D.matplot(matrix_data)
}

pca  = prcomp(data, center = TRUE)
plot(predict(pca))

scatterplot3d(pca$x[,1], pca$x[,2], pca$x[,3], main = "PCA 3") 