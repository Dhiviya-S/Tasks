def prime(n):
 if n < 2:
  return False
 for i in range(2, int(n ** 0.5) + 1):
  if n % i == 0:
   return False
 return True

a = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in a if prime(num)]
prime_count =len(prime_numbers)
print("Prime Numbers:", prime_numbers)
print("Count of prime numbers:",prime_count)