def read_to_array(file):
    result = []
    with open(file) as f:
        for line in f.readlines():
            result.append(line[:-1])

    return result
