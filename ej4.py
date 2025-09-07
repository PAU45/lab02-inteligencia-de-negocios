install.packages("ggplot2")
library(ggplot2)

iris_data <- read.csv("C:/users/jafro/documents/iris-1.csv")

ggplot(iris_data, aes(x = SepalLengthcm, y = PetalLengthcm, color = Species)) +
  geom_point(size = 3) +
  labs(title = "Gráfico de dispersión: SepalLengthcm vs PetalLengthcm",
       x = "Sepal Length (cm)",
       y = "Petal Length (cm)") +
  theme_minimal()
