def average(array):
    # your code goes here
    sum=0
    l=list(set(array)) #convert set of element of array to list (type casting)
    for i in range(len(l)):
        sum+=l[i]
    return (sum/len(l))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
