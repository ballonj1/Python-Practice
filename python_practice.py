def mult_by_two(arr):
    for num in arr:
        print num * 2

mult_by_two([1,2,3,4])


def unique_items(arr):
  unique = []
  for num in arr:
      if arr.count(num) == 1:
        unique.append(num)
  print unique


unique_items([1,1,1,3,4,4,6])
