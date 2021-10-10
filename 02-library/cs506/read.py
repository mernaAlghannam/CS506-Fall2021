def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    X = []
    y = []
    f = open(csv_file_path)
    for line in f:
        i = 0
        x_class = []
        for word in line.split(','):
            
            x_class.append(word)
        #adds inner list conaining attr for specif class
        X.append(x_class)
    return X
