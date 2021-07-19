def func():
  print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")
def myfunc():
  pass


if __name__ == "__main__":
  # Run your script
  myfunc()