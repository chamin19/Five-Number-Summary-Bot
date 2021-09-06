import math

def mean(temp):
    return sum(temp.data_list)/temp.num_of_elements

def median(temp):
    temp.data_list.sort()
    if temp.num_of_elements % 2 != 0:
        return temp.data_list[temp.num_of_elements//2]
    else:
        return (temp.data_list[temp.num_of_elements//2-1] + temp.data_list[temp.num_of_elements//2])/2

def mode(temp): 
    if temp.num_of_elements == 1:
        return temp.data_list
    occurences = {}
    for num in temp.data_list:
        if num in occurences:
            occurences[num] += 1
        else:
            occurences[num] = 1 
    max_freq = max(occurences.values())
    if sum(value==max_freq for value in occurences.values()) == len(occurences):
        return "No mode"
    elif sum(value==max_freq for value in occurences.values()) > 1:
        multiple_modes = [num for num in occurences.keys() if occurences[num] == max_freq]
        return multiple_modes
    return max(occurences, key=occurences.get)  

def sample_variance(temp):
    data_squares = [num*num for num in temp.data_list]
    sum_squared = (sum(temp.data_list))**2
    x = sum(data_squares) - (sum_squared/temp.num_of_elements)
    y = temp.num_of_elements - 1
    return x/y

def standard_deviation(temp):
    return math.sqrt(sample_variance(temp))

#Box model
def quartile_calc(temp, position):
    if position%1 == 0:
        return temp.data_list[int(position)-1]
    else:
        first_num = temp.data_list[math.floor(position)-1]
        second_num = temp.data_list[math.floor(position)]
        return first_num + position%1 * (second_num - first_num)

def first_quartile(temp):
    position = 0.25*(temp.num_of_elements + 1) 
    return quartile_calc(temp,position)

def third_quartile(temp):
    position = 0.75*(temp.num_of_elements + 1) 
    return quartile_calc(temp,position)

def interquartile_range(temp):
    return third_quartile(temp) - first_quartile(temp)

def lower_fence(temp):
    return first_quartile(temp) - 1.5*interquartile_range(temp)

def upper_fence(temp):
    return third_quartile(temp) + 1.5*interquartile_range(temp)

def outliers(temp):
    outliers_list = [num for num in temp.data_list if num<lower_fence(temp) or num>upper_fence(temp)]
    if len(outliers_list) == 0:
        return "No outliers"
    return outliers_list

def minimum(temp):
    return temp.data_list[0]

def maximum(temp):
    return temp.data_list[len(temp.data_list)-1]

def minimum_fence(temp):
    index = None
    if temp.data_list[0] >= lower_fence(temp):
        return temp.data_list[0]
    else:
        for i in range(len(temp.data_list)):
            if temp.data_list[i] < lower_fence(temp):
                index = i
        return temp.data_list[index+1]

def maximum_fence(temp):
    index = None
    if temp.data_list[-1] <= upper_fence(temp):
        return temp.data_list[-1]
    else:
        for i in range(len(temp.data_list)-1,-1,-1):
            if temp.data_list[i] > upper_fence(temp):
                index = i
        return temp.data_list[index-1]