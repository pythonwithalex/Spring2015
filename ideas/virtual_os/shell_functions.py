import os

def ls():
  files = os.listdir('.')
  for line in zip(files[::2],files[1::2]):
    print ''.join([line[0].ljust(20),line[1].ljust(20)])

if __name__ == '__main__':
  ls()
