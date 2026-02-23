units = int(input("Enter units: "))

bill = 0

if units > 0:

    # First 100 units
    if units > 100:
        bill = bill + (100 * 2)
        units = units - 100
    else:
        bill = bill + (units * 2)
        units = 0

    # Next 100 units
    if units > 0:
        if units > 100:
            bill = bill + (100 * 3)
            units = units - 100
        else:
            bill = bill + (units * 3)
            units = 0

    # Next 300 units
    if units > 0:
        if units > 300:
            bill = bill + (300 * 5)
            units = units - 300
        else:
            bill = bill + (units * 5)
            units = 0

    # Above 500 units
    if units > 0:
        bill = bill + (units * 8)

    bill = bill + 50   # fixed charge

print("Total Bill =", bill)