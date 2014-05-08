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

from nose.tools import *
from theano_bpr import BPR
from numpy.random import randint

def test_bpr_train_stores_data():
    bpr = BPR(1, 2, 3)
    bpr.train([
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 2),
    ], batch_size=4)
    assert_equal(bpr._train_users, set([0, 1]))
    assert_equal(bpr._train_items, set([0, 1, 2]))
    assert_equal(bpr._train_dict, {
        0: [ 1, 2 ],
        1: [ 0, 2 ],
    })

def test_bpr_train_and_test():
    bpr = BPR(10, 100, 50)
    train_data = zip(randint(100, size=1000), randint(50, size=1000))
    bpr.train(train_data, batch_size=50)
    assert(bpr.test(train_data) > 0.8)
    test_data = zip(randint(100, size=1000), randint(50, size=1000))
    assert(bpr.test(test_data) > 0.4 and bpr.test(test_data) < 0.6)

def test_bpr_train_no_epochs():
    bpr = BPR(10, 100, 50)
    train_data = zip(randint(100, size=1000), randint(50, size=1000))
    bpr.train(train_data, epochs=0)
    assert(bpr.test(train_data) > 0.4 and bpr.test(train_data) < 0.6)
