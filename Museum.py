# ---- Reading input ----
# Use these EXACT prompt strings so your program matches the required format.
# How many times you read, and in what order, is up to you.

adults = 0
children = 0
seniors = 0

day = int(input("Enter day (1-8): "))
if day == 8:
    day_type = "holiday"
elif day == 6 or day == 7:
    day_type = "weekend"
else:
    day_type = "weekday"

while(True):
    age = int(input("Enter age (-1 to stop): "))
    if age == -1:
        break
    else:
        if age < 13:
            children += 1
        elif age < 60:
            adults += 1
        else:
            seniors += 1

total_people = children + adults + seniors


# ---- Your program ----
# Read the input and work everything out here. How you structure and order
# the steps is up to you.
groups = adults//5
rem = adults%5

# Pricing
if day_type == "holiday":
    price_children = 50.00 * children
    price_seniors = 60.00 * seniors
    price_adults = (75.00 * groups * 5) + (100.00 * rem)

elif day_type == "weekend":
    price_children = 40.00 * children
    price_seniors = 50.00 * seniors
    price_adults = (65.00 * groups * 5) + (80.00 * rem)

else:  # weekday
    price_children = 30.00 * children
    price_seniors = 40.00 * seniors
    price_adults = (35.00 * groups * 5) + (60.00 * rem)

subtotal = price_children + price_seniors + price_adults

# Discounts
discount = 0.0
if ((day_type == "holiday" or day_type == "weekend") and (groups > 0)):
    discount = subtotal * 0.10

# Service fee
service_fee = 0.0
if (day_type == "weekday" and total_people < 3):
    service_fee = 0.00
else:
    service_fee = total_people * 5.00
    if service_fee > 30.00:
        service_fee = 30.00
    #or min(30.00, total_people * 5.00)

# ---- Output ----
# Replace each ??? with the value you computed. Keep every label, space, and
# the "{:.2f}" formatting exactly as shown — your output is compared exactly.

print("Day type:", day_type)
print("Children:", children)
print("Adults:", adults)
print("Seniors:", seniors)
print("Total people:", total_people)
print("Groups formed:", groups)
print("Discount:", "{:.2f}".format(discount))
print("Service fee:", "{:.2f}".format(service_fee))
print("Total cost:", "{:.2f}".format(subtotal - discount + service_fee))
