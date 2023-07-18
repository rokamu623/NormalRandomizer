from numpy import random
from matplotlib import pyplot

 
def two_peak_normal(average: float, standard_deviation: float, outlier_exrate: float, outlier_freqency: float, size: int) -> list[int]:
    minority_size: int = int(size * outlier_freqency)
    majority_size: int = size - minority_size

    outputs = list(random.normal(loc=average, scale=standard_deviation, size=majority_size))
    outputs.extend(list(random.normal(loc=average*outlier_exrate, scale=standard_deviation*outlier_freqency, size=minority_size)))

    outputs = [int(_) for _ in outputs]

    return outputs

def normal(average: float, standard_deviation: float, size: int) -> list[int]:
    return list(random.normal(loc=average, scale=standard_deviation, size=size))

def data_histgram(data_list: list[int], num_of_divisions: int):
    hist_tuple = pyplot.hist(data_list, num_of_divisions)
    return list(hist_tuple[0]), list(hist_tuple[1])

def show_histgram(data_list: list[int], num_of_divisions: int):
    pyplot.hist(data_list, num_of_divisions)
    pyplot.show()