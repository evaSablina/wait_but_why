age = input("What is your current age?")

int_age = int(age)

days = 365 * int_age
weeks = 52 * int_age
months = 12 * int_age

days_main = 90 * 365
weeks_main = 90 * 52
months_main = 90 * 12

print(f"You have {days_main - days} days, {weeks_main - weeks} weeks, and {months_main - months} months left.")



# age = input("What is your current age? ")
#
# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)
#
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")