## Author: Adam Warsing ajw6150@psu.edu
## Collaborator: Stanley Wang szw5739@psu.edu
## Collaborator: Jack Shields jcs6783@psu.edu
## Section: 010R
## Breakout Room: 15

def sum_n(n):
  if n <= 0:
    return 0
  else:
    return n + sum_n(n-1)
def print_n(string,num):
  if num == 0:
    return 0
  else:
    return print_n(string,num-1)


def run():
  num = int(input("Enter an int: "))
  print("sum is {}".format(sum_n(num)))
  string = input("Enter a string: ")
  print("{}".format(print_n(string,num)))


if __name__ == "__main__":
  run()
