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

from collections import defaultdict

def load_data_from_csv(csv, users_to_i = {}, items_to_i = {}):
    """
      Loads data from a CSV file located at `csv` 
      where each line is of the form:

        user_id_1, item_id_1
        ...
        user_id_n, item_id_n

      Initial mappings from user and item identifiers
      to integers can be passed using `users_to_i`
      and `items_to_i` respectively.

      This function will return a data array consisting
      of (user, item) tuples, a mapping from user ids to integers
      and a mapping from item ids to integers.
    """
    data = []
    if len(users_to_i.values()) > 0:
        u = max(users_to_i.values()) + 1
    else:
        u = 0
    if len(items_to_i.values()) > 0:
        i = max(items_to_i.values()) + 1
    else:
        i = 0
    with open(csv) as f:
        for line in f.readlines():
            user, item = line.strip().split(',')
            if not users_to_i.has_key(user):
                users_to_i[user] = u
                u += 1
            if not items_to_i.has_key(item):
                items_to_i[item] = i
                i += 1
            data.append((users_to_i[user], items_to_i[item]))
    return data, users_to_i, items_to_i
