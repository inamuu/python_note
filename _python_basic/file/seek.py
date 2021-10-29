def main():
  with open('test.txt', 'r') as f:
    print(f.tell())
    f.seek(3)
    print(f.read(4))

main()
