def find_pair_with_multiply(arr,target):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]*arr[j]==target:
        return (arr[i], arr[j])
      if arr[j]*arr[i]==target:
        return (arr[j], arr[i])
  return "No proceed"

arr = eval(input())
target = int(input())
print(find_pair_with_multiply(arr,target))