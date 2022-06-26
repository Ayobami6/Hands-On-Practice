import phonenumbers
from numbers import number

from phonenumbers import geocoder
key = ''

trkNumber = phonenumbers.parse(number)

number_location = geocoder.description_for_number(trkNumber, 'en')
print(number_location)

# Get service providers
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

