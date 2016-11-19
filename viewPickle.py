import pandas as pd
perf = pd.read_pickle('dma.pickle') # read in perf DataFrame
print perf.head(252)

#attempt to print to csv
perf.to_csv('predictionOutput.csv')
