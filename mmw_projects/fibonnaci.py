from math import sqrt, pow


def fibonacci(x, *args, operation=None) -> int:
  fib = int((pow((1+sqrt(5))/(2), x)-pow((1-sqrt(5))/(2), x))/sqrt(5))

  match operation:
    case "add":
      sum = fibonacci(x)
      for nums in args:
        sum += fibonacci(nums)
      return sum
    case "subtract":
      dif = fibonacci(x)
      for nums in args:
        dif -= fibonacci(nums)
      return dif
    case "multiply":
      prod = fibonacci(x)
      for nums in args:
        prod *= fibonacci(nums)
      return prod
    case None:
      return fib  

if __name__ == "__main__":
  ans = fibonacci(12)
  print(ans)



 