import pandas as pd
import matplotlib.pyplot as plt

# create DataFrame
df = pd.read_csv("data/data.csv")

# plot the data
df.plot(kind='hist')
plt.show()



