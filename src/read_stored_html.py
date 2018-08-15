def main():
  with open('full_book_list.html') as f:
    print(f.read())

if __name__ == '__main__':
  main()


def gethtml():
  f = open('full_book_list.html').read()
  return f
