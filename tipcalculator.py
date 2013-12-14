print "I am TI-9000, a calculator that helps you decide if you should estimate tip at a restaurant with the quick 'n dirty doubling-the-tax method or if it's better to calculate it out manually."
raw_input("Hit Enter to continue...")

Meal = input("How much do you spend on an average meal? (in dollars)")

Tax = input("How much does your county tax prepared-food? (enter as a decimal)")

Mealwithtax = Meal * (1+Tax)
print "This is your average meal total with tax: $", Mealwithtax
raw_input("Hit Enter to continue...")

print "Now, suppose you've been a proponent of the doubling-tax method of calculating tip."
doubletaxtip = Tax * 2
total1 = Mealwithtax + Meal * doubletaxtip
print "This is what your total bill would come to: $", total1
raw_input("Hit Enter to continue...")

Regulartip = input("What percentage do you see yourself tipping if you always had me in your pocket to do all the work for you every time? (enter as decimal)")
total2 = Mealwithtax + Meal * Regulartip
print "Then this is what your total bill would come to instead: $", total2
raw_input("Hit Enter to continue...")

print "Does this make a big difference over a year, you ask? Let's find out."
raw_input("Hit Enter to continue...")

MealsPerWeek = input("How many times per week on average do you eat out?")
DifferencePerMeal = total1-total2 
DifferencePerYear = DifferencePerMeal * MealsPerWeek * 52
print "You'd be seeing a difference of $" + ("%.2f" % DifferencePerYear) + " per year." 
raw_input("Hit Enter to continue...")

answer = raw_input("Ok, so here's the million dollar question. With this new information, do you think it is worth it to manually calculate tip (yes or no)?")
if answer == "yes":
        print "Good. I'm glad I've been helpful to you. But damn, I would hate to be your server."
elif answer == "no":
        print "Keep doing what you're doing then. Since you probably don't mind, I've taken the liberty to log into your Paypal account to transfer $", DifferencePerYear, "to my father and creator, Jason Chuang. He is applying for a Python bootcamp called Code Fellows and could really use that money for tuition. Thanks!"
