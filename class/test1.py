class OpsTest:
  i = 'hoge'
  def __init__(self, name):
    self.name = name

r = OpsTest(name='hoge')
print(r.i)
print(r.name)

