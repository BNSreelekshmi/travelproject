import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

phno = input("Enter the ohone number with country code:")
pn = phonenumbers.parse(phno)
tz = timezone.time_zones_for_number(pn)
print("Time Zone:", str((tz)))
