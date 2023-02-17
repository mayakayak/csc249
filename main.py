# Maya Gilliom
# Feb 7, 2023
# M3 T1: Selection sort

def selection_sort (numbers): 
  for i in (range(len(numbers)-1)):
    index_smallest = i
    
    for j in range(i+1, len(numbers)):
      if numbers[j] < numbers[index_smallest]:
        index_smallest = j
  
    temp = numbers[i] #first iteration: temp = 3
    numbers[i] = numbers[index_smallest] #3 spot becomes 1
    numbers[index_smallest] = temp #1 spot becomes 3
  return numbers

length_of_numbers = int(input("How many integers would you like to sort? "))
numbers = []
for number in range(length_of_numbers):
  numbers.append(int(input("Enter integer: ")))

print(f"before sort {numbers}")
print(f"after sort  {selection_sort(numbers)}")

