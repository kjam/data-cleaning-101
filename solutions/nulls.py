rows_filled = 32357 - df[df.temperature.isnull() == True].shape[0] # taken from cell 19
still_missing = df[df.temperature.isnull() == True].shape[0] / df.shape[0]
