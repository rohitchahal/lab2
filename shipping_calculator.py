number = int(input("Enter number of Items: "))

while number < 0 :
    print("Invalid number of Items")
    number = int(input("Enter number of Items: "))

total_shipping_cost = 0
for i in range(number):
    shipping_cost = float(input("Enter shipping cost for Item "))
    total_shipping_cost += shipping_cost

if total_shipping_cost > 100:
    total_shipping_cost = total_shipping_cost * 0.10

print("Total shipping Cost is = $", total_shipping_cost)
