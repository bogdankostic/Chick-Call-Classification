import pandas as pd

all_files = pd.read_csv('chick_calls_labels.tsv', sep='\t', header=None)
train_set = all_files.sample(frac=0.8)
test_set = all_files.drop(train_set.index).sample(frac=1)

train_set.to_csv('train_labels.tsv', sep='\t', header=None, index=False)
test_set.to_csv('test_labels.tsv', sep='\t', header=None, index=False)