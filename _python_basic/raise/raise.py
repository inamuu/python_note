def main():
  try:
    raise NameError("name")
  except NameError:
    print('name error--')
    raise


main()
