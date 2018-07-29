

def frequency_calculator(string):
    freq = dict()
    string = string.split(" ")
    for x in string:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    return freq 


