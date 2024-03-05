import decimal

width = 5
precision = 3
value = decimal.Decimal("42.12345")
print(f"output:{value:{width}.{precision}f}")
# 'output:     42.1'
