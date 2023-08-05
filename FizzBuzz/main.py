for i in range(1, 101):
    ans=""
    if i % 3 == 0:
        ans += "Fizz"
    if i % 5 == 0:
        ans += "Buzz"
    if ans == "":
        ans += str(i)
    print(ans)

print([(lambda n: { 1: n, 6: "Fizz", 10: "Buzz", 0: "FizzBuzz" }[n**4%15])(n+1) for n in range(100)])