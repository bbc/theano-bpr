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
    ], batch_size=10)
    assert_equal(bpr._train_users, set([0, 1]))
    assert_equal(bpr._train_items, set([0, 1, 2]))
    assert_equal(bpr._train_dict, {
        0: [ 1, 2 ],
        1: [ 0, 2 ],
    })

def test_bpr_train_and_test():
    bpr = BPR(10, 100, 50)
    train_data = zip(randint(100, size=1000), randint(50, size=1000))
    bpr.train(train_data)
    assert(bpr.test(train_data) > 0.8)
    test_data = zip(randint(100, size=1000), randint(50, size=1000))
    assert(bpr.test(test_data) > 0.4 and bpr.test(test_data) < 0.6)
