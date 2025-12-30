import requests

def get_location(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    
    return {
        "IP Address": data["ip"],
        "City": data["city"],
        "Region": data["region"],
        "Country": data["country"],
        "Location": data["loc"]
    }

# Example usage
ip_address = "00331-10000-00001-AA817"
location_data = get_location(ip_address)
print(location_data)