def spy_game(nums):
    a=False
    b=0
    d=0
    c=0
    for i in nums:
        if i==0:
            b=c+1
            for j in nums[b:]:
                if j==0:
                    d=c+1
                    for k in nums[d:]:
                        if k==7:
                            a=True
                            return a
                        else:
                            continue
        else:
            c=c+1

    if a==False:
        return False


print(spy_game([1,0,2,4,0,5,7]))
