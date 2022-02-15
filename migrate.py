import pandas as pd
from string import punctuation
from volumemap import volumeMap
words_data = pd.read_csv('WordList.csv')

# strip trailing punctuation from Text
words_data["Text"] = words_data["Text"].str.rstrip(punctuation)

# split DateCreated into Date and Time columns. splitting on T
new = words_data["DateCreated"].str.split("T", n = 1, expand = True)
words_data["Date"] = new[0]
# remove Z from the end of Time column
words_data["Time"] = new[1].str.replace(r'Z', '')
# drop the old DateCreated column
words_data.drop(columns = ["DateCreated"], inplace = True)

# split VolumeId column into author and title columns

# add Author and Title columns
words_data["Author"] = ""
words_data["Title"] = ""

# obtain Author and Title from VolumeId
def obtain(r):
	if r.VolumeId in volumeMap:
		r.Author = volumeMap[r.VolumeId]["Author"]
		r.Title = volumeMap[r.VolumeId]["Title"]
		return r

words_data.apply(obtain, axis=1)

# write to csv
words_data.to_csv('WordListModified.csv', index=False)