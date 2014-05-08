#!/usr/bin/env python

# theano-bpr
#
# Copyright (c) 2014 British Broadcasting Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from theano_bpr.utils import load_data_from_csv
from theano_bpr import BPR
import sys

if len(sys.argv) != 3:
    print "Usage: ./example.py training_data.csv testing_data.csv"
    sys.exit(1)

# Loading train data
train_data, users_to_index, items_to_index = load_data_from_csv(sys.argv[1])
# Loading test data
test_data, users_to_index, items_to_index = load_data_from_csv(sys.argv[2], users_to_index, items_to_index)

# Initialising BPR model, 10 latent factors
bpr = BPR(10, len(users_to_index.keys()), len(items_to_index.keys()))
# Training model, 10 epochs
bpr.train(train_data, epochs=30)
# Testing model
print bpr.test(test_data)
