class SushiPrice:
  def __init__(self, neta, price):
    self.neta = neta
    self.price = price

  def check_price(self):
    print(f'{neta}は{price}')

sushiprice = SushiPrice()
print(sushiprice.check_price(neta='tako', price='100'))


