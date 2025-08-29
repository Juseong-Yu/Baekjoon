N = int(input())
flight_list = []
for _ in range(N):
    flight = int(input())
    flight_list.append(flight)

max_price = max(flight_list)
min_price = min(flight_list)

price_pay = min_price - max_price / 2 

if price_pay < 0:
    print(0)
else:
    print(int(price_pay))