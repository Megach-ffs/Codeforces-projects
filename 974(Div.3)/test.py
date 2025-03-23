lst = list(map(int, input().split()))

def merge(alist,blist):
    merged = []
    a = len(alist)
    b = len(blist)
    c = 0
    d = 0
    while c < a or d < b:
       
        if d >= b or (c < a and alist[c]<=blist[d]):
            merged.append(alist[c])
            c+=1
        else:
            merged.append(blist[d])
            d+=1

    return merged

def rec(lst):
    lst_sz = len(lst)
    if lst_sz == 1:
        return lst
    a = rec(lst[:lst_sz//2])
    b = rec(lst[lst_sz//2:])
    
    return merge(a,b)


print(rec(lst))