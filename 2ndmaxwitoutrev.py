def second_max(numbers):
    if len(numbers)<2:
        return "Not enough elements:"
    sorted_num=sorted(numbers)
    return sorted_num[-2]
number_list=[3,8,1,5,7]
result=second_max(number_list)
print("second max :",result)
