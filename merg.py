def merge(left, right):
    lenl=len(left)
    lenr = len(right)
    i = j = 0
    c=0
    result=[]

    while i < lenl and j < lenr:
        if left[i]<=right[j]:
            result.append(left[i])
            c+=1
            i+=1
        else:
            result.append(right[j])
            j+=1
            c+=1
    while i <lenl:
        result.append(left[i])
        c+=1
        i+=1
    while j < lenr:
        result.append(right[j])
        j+=1
        c+=1
    return result

def msort(l):
    count = len(l)
    if count<2:
        return l
    else:
        mid = count//2
        left = msort(l[:mid])
        right = msort(l[mid:])
        return merge(left, right)

print(msort([3,2,4,5,23,5,464,6,325,73,23,46,54,34,5324,25,34,534]))