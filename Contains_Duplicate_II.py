nums=[1,2,3,1]
k=2
result=False
last_seen={}
for i,num in enumerate(nums):
    if num in last_seen and i-last_seen[num]<=k:
        result=True
        break
    last_seen[num]=i
print(result)