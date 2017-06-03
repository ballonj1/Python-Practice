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

def pascals_triangle(n):
    triangle = [[1]]
    while len(triangle) < n + 1:
      triangle.append(next_row(triangle[len(triangle) - 1]))
    print triangle

def next_row(last_row):
  row = [1]
  i = 0
  while i < len(last_row) - 1:
    row.append(sum([last_row[i], last_row[i + 1]]))
    i += 1
  row.append(1)
  return row

pascals_triangle(2)

def next_prime(ary):
    new_arr = []
    for num in ary:
        if prime(num):
            new_arr.append(next_prime_number(num))
        else:
            new_arr.append(num)
    print new_arr


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def next_prime_number(n):
    n += 1
    while not prime(n):
        n += 1
    return n

next_prime([11,13,17])
