import math

def ucln_n_so(daySo):
    
  result = daySo[0]
  for num in daySo[1:]:
    result = math.gcd(result, num)
  return result

def bcnn_n_so(daySo):

  a = 1
  for num in daySo:
    a *= num
  return a // ucln_n_so(daySo)

day = [12, 18, 24]
print("ƯCLN:", ucln_n_so(day))
print("BCNN:", bcnn_n_so(day))