def postTaxPrice(price):
    ans = int(price * 1.08)
    return ans

print(postTaxPrice(120), "円")
print(postTaxPrice(128), "円")
print(postTaxPrice(980), "円")
