def computepay(h, r):
    try:
        pay = float(h) * float(r)
        if float(h) > 40:
            ot_hours = float(h) - 40
            pay = (40 * float(r))+(ot_hours * (float(r)*1.5))
            return pay
    except:
        print('Please enter a number')

hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")
p = computepay(hrs, rate)
print("Pay", p)