prime_list = [2]
limit = int(input("Enter a limit : "))
for num in range(3,limit):
  #print(" Iterating number is %s"%num)
  if num <= limit:
    for i in range(2,num):
      if (num % i) == 0:
        print("%s is not a prime number"%num)
        break
      elif num-i == 1 and (num % i) != 0:
        print(" %s is prime number and added to the list"%num)
        prime_list.append(num)


print(prime_list)
