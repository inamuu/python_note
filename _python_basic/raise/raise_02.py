def func1(x):
    try:
        return 1/x
    except ZeroDivisionError:
        print("零割りが発生しました。")
        raise

def test(x):
    try:
        x = func1(0)
    except:
        print("何らかの例外が発生しました。")
        raise
    else:
        print("この関数では例外は発生しませんでした")

test(10)
