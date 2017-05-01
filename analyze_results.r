library(RcppCNPy)
data = npyLoad("/home/grzegorz/agh/prmiml/graphs/results.bin.npy")
pca  = prcomp(data, center = TRUE)
plot(predict(pca))
