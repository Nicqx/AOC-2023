def read_to_array(file):
    result = []
    with open(file) as f:
        for line in f.readlines():
            if line[-1] == '\n':
                result.append(line[:-1])
            else:
                result.append(line)

    return result
