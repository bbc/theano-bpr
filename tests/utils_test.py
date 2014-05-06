from nose.tools import *
from theano_bpr.utils import load_data_from_csv
import os

def test_load_data_from_csv():
    csv = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'data.csv')
    data, user_index, item_index = load_data_from_csv(csv)
    assert_equal(data, [
        (0, 0),
        (1, 1),
        (2, 2),
        (2, 3),
        (2, 1),
        (3, 4),
        (3, 3),
    ])
    assert_equal(user_index, {
      'user_id1': 0,
      'user_id3': 1,
      'user_id7': 2,
      'user_id8': 3,
    })
    assert_equal(item_index, {
      'item_id10': 0,
      'item_id0': 1,
      'item_id53': 2,
      'item_id32': 3,
      'item_id3': 4,
    })

def test_load_data_from_csv_with_initial_mapping():
    csv = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'data.csv')
    data, user_index, item_index = load_data_from_csv(csv, {'user_id7': 0, 'user_id3': 1}, {'item_id53': 0, 'item_id32': 1})
    assert_equal(data, [
        (2, 2),
        (1, 3),
        (0, 0),
        (0, 1),
        (0, 3),
        (3, 4),
        (3, 1),
    ])
    assert_equal(user_index, {
      'user_id7': 0,
      'user_id3': 1,
      'user_id1': 2,
      'user_id8': 3,
    })
    assert_equal(item_index, {
      'item_id53': 0,
      'item_id32': 1,
      'item_id10': 2,
      'item_id0': 3,
      'item_id3': 4,
    })
