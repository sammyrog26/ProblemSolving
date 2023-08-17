import argparse
from ipstack import geolookup


def get_location(ip_address, access_key):
    if len(str(ip_address).split(",")) > 1:
        print("Cannot Do Bulk Lookup of IPs")
        return
    ipDetails = geolookup.GeoLookup(access_key)
    print("Authentication Successful\n\n")
    response = ipDetails.get_location(ip_address)
    print("IP_ADDRESS:\t %s" % ip_address)
    print("Country:\t %s" % response.get("country_name"))
    print("Region:\t\t %s" % response.get("region_name"))
    print("City:\t\t %s" % response.get("city"))
    print("City:\t\t %s" % response.get("zip"))

    print("Country Code:\t %s" % response.get("country_code"))
    print("Region Code:\t %s" % response.get("region_code"))
    print("Latitude:\t %s" % response.get("latitude"))
    print("Longitude:\t %s" % response.get("longitude"))


def parse_arguments():
    parser = argparse.ArgumentParser('IP Details')
    parser.add_argument('-i', '--ip-address',
                        dest='ip_address',
                        required=True)
    parser.add_argument('-a', '--access-key',
                        dest='access_key',
                        required=True)
    return parser.parse_args()


if __name__ == "__main__":
    parsed_args = parse_arguments()
    access_key = parsed_args.access_key
    ip_address = parsed_args.ip_address
    get_location(ip_address, access_key)
