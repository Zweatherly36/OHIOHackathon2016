import pandas as pd #import the panda type
perf = pd.read_pickle('dma.pickle') # read in perf DataFrame
print perf.head() #prints to console first 252 lines (one year of trading)

#Prints the panda to a csv file
perf.to_csv('predictionOutput.csv')
