#Python 2.7
import json
from urllib import urlopen

ip_info = urlopen('http://freegeoip.net/json/').read()

my_ip = json.loads(ip_info)

print "Approx Loaction is:- \n\tLatitude : %f \n\tLongitude :  %f \n\tCountry: %s" % (
my_ip.get('latitude'), my_ip.get('longitude'), my_ip.get('country_name'))
