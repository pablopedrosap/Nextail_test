class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.cart = []

    def scan(self, item):
        self.cart.append(item)

    def calculate_total(self):
        total = 0
        voucher_count = self.cart.count('VOUCHER')
        tshirt_count = self.cart.count('TSHIRT')
        pants_count = self.cart.count('PANTS')

        # Apply 2-for-1 special on VOUCHER
        total += (voucher_count // 2 + voucher_count % 2) * self.pricing_rules['VOUCHER']

        # Apply discount on TSHIRT
        if tshirt_count >= 3:
            total += tshirt_count * 19
        else:
            total += tshirt_count * self.pricing_rules['TSHIRT']

        # Add PANTS items to total
        total += pants_count * self.pricing_rules['PANTS']

        return total


pricing_rules = {
    'VOUCHER': 5,
    'TSHIRT': 20,
    'PANTS': 7.5
}

checkout = Checkout(pricing_rules)
while True:
    product = input('Select voucher/tshirt/pants or 999 to finish order: ').upper()
    if product == '999':
        break
    else:
        checkout.scan(product)

print(checkout.calculate_total())
