import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import urllib
#import geocoder
import time
from geopy.geocoders import Nominatim
geolocator = Nominatim()

# geocoding api key: AIzaSyAngWcWLW5gyX7fXOiO3bzxCfwhuPS-GWE
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#use this on pythonanywhere
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/remmi11/lovelytics/client_secret.json', scope)

#use this for testing locally
# credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)


gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
worksheet = gc.open("Conference Locations").sheet1

def updateAddress():

    count = 1
    fullList = []
    cities = worksheet.col_values(6)
    states = worksheet.col_values(7)
    countries = worksheet.col_values(8)
    #x = zip(cities, states, countries)
    for x in zip(cities, states, countries):
        cellAddress = 'J%s' % (count)
        valueAddress = x[0] + ', ' + x[1]+ ', ' + x[2]
        worksheet.update_acell(cellAddress, valueAddress)
        count += 1


def geocodeAddresses():

    values_list = worksheet.col_values(10)

    count = 2
    for value in values_list:
        if value != 'City, State, Country':
            print value
            location = geolocator.geocode(value)
            #print location.longitude
            #print location.latitude

            cellLat = 'K%s' % (count)
            #print cellLat
            cellLng = 'L%s' % (count)
            #print cellLng

            # valueLat = latlng[0]
            # print valueLat

            # valueLng = latlng[1]
            # print valueLng

            worksheet.update_acell(cellLat, location.latitude)
            worksheet.update_acell(cellLng, location.longitude)

            #print ""
            count += 1
            #time.sleep(.5)



updateAddress()
geocodeAddresses()