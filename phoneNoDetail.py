import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter Your No. with +__: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)    
car = carrier.name_for_number(phone,"en") #it returns phone company name
reg = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(reg)

