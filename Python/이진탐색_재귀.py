
def binary_search(array, target, start, end) :
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    #중간점의 값 보다 찾고자 하는 값이 작은 경우는 왼쪽만 확인
    elif array[mid] > target :
        return binary_search(array,target,start,mid-1)

    #중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽만 확인
    else:
        return binary_search(array,target,mid+1,end)


n,target = list(map(int, input().split()))
array = list(map(int,input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array,target,0,n-1)

if result == None:
    print('원소가 존재하지 않습니다.')

else:
    print(result+1)

'''
[Input]
10 7
1 3 5 7 9 11 13 15 17 19
[Output]
4
[Input]
10 7
1 3 5 6 9 11 13 15 17 19
[Output]
원소가 존재하지 않습니다.
'''