import numpy as np

dupe_dict = {}

for dupepair, confidence in dupes:
    dupe_dict[dupepair[0]] = {'pair': dupepair, 'confidence': confidence[0]}
    dupe_dict[dupepair[1]] = {'pair': dupepair, 'confidence': confidence[0]}

customers['duplicate_pair'] = customers.index.map(lambda i: dupe_dict[i].get('pair')
                                                  if i in dupe_dict else np.nan)
customers['confidence'] = customers.index.map(lambda i: dupe_dict[i].get('confidence')
                                              if i in dupe_dict else np.nan)
