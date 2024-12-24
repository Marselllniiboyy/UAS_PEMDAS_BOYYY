arr = eval(input())
targett = int(input())

def find_pair_with_div(arr,target):
  for i in range(len(arr)):
    for j in range(len(arr)):
      if (arr[i]/arr[j]) == target:
        return (arr[i], arr[j])
      if (arr[j]/arr[i]) == target:
        return (arr[i], arr[j])
  return "No proceed"

print(find_pair_with_div(arr,targett))