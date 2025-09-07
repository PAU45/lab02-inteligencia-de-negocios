install.packages("ggplot2")
library(ggplot2)

iris_data <- read.csv("Iris-1.csv")

ggplot(iris_data, aes(x = SepalLengthCm, y = PetalLengthCm, color = Species)) +
  geom_point(size = 3) +
  labs(
    title = "Gráfico de dispersión: SepalLength vs PetalLength",
    x = "Sepal Length (cm)",
    y = "Petal Length (cm)"
  ) +
  theme_minimal()
