import os

SCRIPTPATH='/tmp'
list = [
  'hoge'
]

def main():
    for i in list:
        try:
            os.chdir(SCRIPTPATH + '/' + i)
            print("\n=== Start script " + i + " ===")
            command = "echo %s" % (i)
            os.system(command)
        except:
            print('Failed execute ' + i)

if __name__ == "__main__": main()