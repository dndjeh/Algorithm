def solution(str1, str2):
    arr1 = []
    arr2 = []
    union = 0
    inter = 0

    # for i in range(1,len(str1)):
    #     if (str1[i]>='A' and str1[i]<='Z' or str1[i]>='a' and str1[i]<='z') and (str1[i-1]>='A' and str1[i-1]<='Z' or str1[i-1]>='a' and str1[i-1]<='z' ) :
    #         arr1.append(str1[i-1].lower()+str1[i].lower())

    arr1 = [str1[i-1:i+1].lower() for i in range(1,len(str1)) if not re.findall('[^a-zA-Z]+',str1[i-1:i+1])]


    for i in range(1,len(str2)):
        if (str2[i]>='A' and str2[i]<='Z' or str2[i]>='a' and str2[i]<='z') and (str2[i-1]>='A' and str2[i-1]<='Z' or str2[i-1]>='a' and str2[i-1]<='z' ) :
            arr2.append(str2[i-1].lower()+str2[i].lower())

    for i in set(arr1):
        if i not in arr2:
             union += arr1.count(i)

        elif i in arr2 :
            cnt1 = arr1.count(i)
            cnt2 = arr2.count(i)
            union += max(cnt1, cnt2) 
            inter += min(cnt1, cnt2)

    for i in set(arr2):
        if i not in arr1:
             union += arr2.count(i)

    if union ==0:
        return 65536
    
    return int((inter/union)*65536)

import re
import math

def solution2(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

print(solution('a+aabb','bbbb'))



print()