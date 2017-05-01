library(RcppCNPy)
data = npyLoad("results.bin.npy")
pca  = prcomp(data, center = TRUE)
plot(predict(pca))
