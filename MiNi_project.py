from matplotlib import pyplot as plt
import numpy as np

labels = ('Positive Tweets', 'Negative Tweets', 'Neutral Tweets')
y_pos = np.arange(len(labels))
types_of_tweets = [26.5,14.35,3.142]
plt.bar(y_pos, types_of_tweets, align='center', alpha=0.5)
plt.xticks(y_pos,labels)
plt.show()
