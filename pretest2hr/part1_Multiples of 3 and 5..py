'''
    Multiples of 3 and 5
'''
def multiples(num1, num2, maxNum):
    nums = []
    for i in range(2, maxNum):
        if i % num1 == 0:
            nums.append(i)
        elif i % num2 == 0:
            nums.append(i)
        else:
            pass
    return nums

def sum_multiples(num1, num2, maxNum):
    nums = multiples(num1, num2, maxNum)
    print(nums)
    result = sum(nums)
    return result


if __name__ == "__main__":

    print(sum_multiples(3, 5, 1000))