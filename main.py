def main():
  print("Hello World")

# Ex 1
# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
def find_factors():
  x = 52633

  for i in range(x+1):
    if i == 0:
      continue
    if x % i == 0:
      print(i)

# Ex 2
# Write a function that prints all factors of the given parameter x
def print_factor(x):
  for i in range(x+1):
    if i == 0:
      continue
    if x % i == 0:
      print(i)

# Ex 3
# Write a program that be able to find all factors of the numbers in the list l
def print_factor_for_list():
  l = [52633, 8137, 1024, 999]
  m = min(l)
  for i in range(m+1):
    if i == 0:
      continue
    if l[0] % i == 0 and l[1] % i == 0 and l[2] % i == 0 and l[3] % i == 0:
      print(i)

if __name__ == '__main__':
  print_factor_for_list()

