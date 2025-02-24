def merge_array(arr1,arr2):
    i ,j = 0,0
    merge = []

    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            merge.append(arr1[i])
            i+=1
        else:
            merge.append(arr2[j])
            j+=1

    merge.extend(arr1[i:])
    merge.extend(arr2[j:])

    return merge




n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(merge_array(arr1,arr2))