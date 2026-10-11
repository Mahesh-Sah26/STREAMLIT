numbers=[3,1,5,8,2,3,3,2,2,2]
def calc_mean(numbers):
    sum=0
    for number in numbers:
        sum+=number
    return f"Mean={(sum/len(numbers)):.2f}"
print(calc_mean(numbers))

def calc_median(numbers):
    numbers=sorted(numbers)
    print(numbers)
    term=int((len(numbers)+1)/2)
    if len(numbers)%2==0:
        median=(numbers[term-1]+numbers[term])/2
    else:
        median=numbers[term-1]
    return f"Median={median}"

print(calc_median(numbers))

def calc_mode(numbers):
    occurence=0
    mode_value=None
    for number in numbers:
        count_value=numbers.count(number)
        if count_value>occurence:
            occurence=count_value
            mode_value=number
    return f"Mode={mode_value}"

print(calc_mode(numbers))

def calc_percentile(numbers,p):
    numbers=sorted(numbers)
    print(numbers)
    term=p*(len(numbers)+1)/100
    lower=int(term)
    fraction=term-int(term)
    if term<=1:
        return numbers[0]
    
    if term>=len(numbers):
       return numbers[-1]
    
    percentile=numbers[lower-1]+fraction*(numbers[lower]-numbers[lower-1])
    return percentile

p=int(input("Enter percentile: "))
print(f"{p} Percentile = {calc_percentile(numbers,p)}")

def calc_quartile(numbers,q):
    numbers=sorted(numbers)
    n=len(numbers)
    term=(q*(n+1))/4
    print(term)
    lower=int(term)
    print(lower)
    fraction=term-lower
    print(fraction)
    if term<=1:
        return numbers[0]
    if term>n:
        return numbers[-1]
    
    quartile=numbers[lower-1]+(fraction*(numbers[lower]-numbers[lower-1]))
    return quartile

q=int(input("Enter Quartile as 1, 2 or 3: "))
print(f"{q} Quartile = {calc_quartile(numbers,q)}")
