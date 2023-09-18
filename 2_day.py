print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? "))
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? ")) * .01

each_persons_bill = "{:.2f}".format((bill_total/number_of_people) + ((bill_total/number_of_people) * (tip_percentage)))

print(f"Each person should pay: ${each_persons_bill}")