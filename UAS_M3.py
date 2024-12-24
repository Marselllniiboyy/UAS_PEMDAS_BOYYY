def cyclic_right_shitf(array,n):
  newArr = array[-(n)%len(array):] + array[:-(n)%len(array)]
  return(newArr)

def main() :
  arr = eval(input())
  try:
    if len(arr) == 0:
      print("No proceed")
      return
  except:
    print("No proceed")
    return
  k =int(input())
  print(cyclic_right_shitf(arr,k))

main()