
def multiplyNumbers(givenNumbers):
   
   return givenNumbers*3

givenNumbers = map(multiplyNumbers, [1, 3, 5, 2, 6, 10])

print("Multiplying list elements with 3:")
for element in givenNumbers:
   print(element)