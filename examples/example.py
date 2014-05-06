from theano_bpr.utils import load_data_from_csv
from theano_bpr import BPR

# Loading train data
train_data, users_to_index, items_to_index = load_data_from_csv('week/training.csv')
# Loading test data
test_data, users_to_index, items_to_index = load_data_from_csv('week/testing.csv', users_to_index, items_to_index)

# Initialising BPR model
bpr = BPR(10, len(users_to_index.keys()), len(items_to_index.keys()))
# Training model
bpr.train(train_data, epochs=1)
# Testing model
print bpr.test(test_data)
