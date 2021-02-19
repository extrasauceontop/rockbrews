from sgselenium import SgChrome
from bs4 import BeautifulSoup as bs

locator_domains = []
page_urls = []
location_names = []
street_addresses = []
citys = []
states = []
zips = []
country_codes = []
store_numbers = []
phones = []
location_types = []
latitudes = []
longitudes = []
hours_of_operations = []

with SgChrome() as driver:
  driver.get("https://www.rockandbrews.com/locations")
  html = driver.page_source
  soup = bs(html, "html.parser")

  grids = soup.find_all("div", attrs={"class": "col-md-4 col-xs-12 pm-location"})

  for grid in grids:
    locator_domain = "rockandbrews.com"
    page_url = "rockandbrews.com/locations"
    
    name = grid.find("h4").text
    address = grid.find("span").text


    full_address = grid.find("a").text
    city_state_zipp = full_address.replace(address, "").strip()
    
    city = city_state_zipp.split(", ")[0]
    state = city_state_zipp.split(", ")[1].split(" ")[0]
    zipp = city_state_zipp.split(", ")[1].split(" ")[1]

    country_code = "US"

    store_number = "<MISSING>"
    phone = "<MISSING>"
    location_type = "<MISSING>"

    latitude = "<MISSING>"
    longitude = "<MISSING>"

    hour = grid.find("span", attrs={"class": "hours-day"})
    print(hour)




