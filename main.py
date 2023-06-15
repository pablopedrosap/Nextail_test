class Checkout:
    """Checkout system that can scan items and apply pricing rules."""
    def __init__(self, pricing_rules):
        """Initialize a Checkout object with the pricing rules."""
        self.pricing_rules = pricing_rules
        self.cart = {}

    def scan(self, item):
        """Scan an item and add it to the cart."""
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def calculate_total(self):
        """Applying any pricing rules, calculate the total price of the items in the cart."""
        total = 0
        for item, count in self.cart.items():
            if item in self.pricing_rules:
                total += self.pricing_rules[item](count)
            else:
                raise ValueError(f'Pricing rule not found for item: {item}')
        return total
# Pricing rules


def voucher_rule(quantity):
    """Pricing rule for VOUCHER: 2-for-1."""
    return (quantity // 2 + quantity % 2) * 5.00


def tshirt_rule(quantity):
    """Pricing rule for TSHIRT: discount for 3 or more."""
    if quantity >= 3:
        return quantity * 19.00
    else:
        return quantity * 20.00


def pants_rule(quantity):
    """Pricing rule for PANTS: no discount."""
    return quantity * 7.50


pricing_rules = {
    'VOUCHER': voucher_rule,
    'TSHIRT': tshirt_rule,
    'PANTS': pants_rule
}

co = Checkout(pricing_rules)
co.scan('VOUCHER')
co.scan('TSHIRT')
co.scan('PANTS')
print(f'Total:  {co.calculate_total()}€')

