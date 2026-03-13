from functools import wraps


def my_decorators(func):
  @wraps(func)
  def wrapper():
    print("Before function runs")
    func()
    print("After function runs")
  return wrapper

@my_decorators
def greet():
  print("Hello, World!")

greet()