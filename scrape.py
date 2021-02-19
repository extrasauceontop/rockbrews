from sgselenium import SgChrome
from bs4 import BeautifulSoup as bs

with SgChrome() as driver:
  driver.get("https://www.rockandbrews.com/locations")
  html = driver.page_source
  soup = bs(html, "html.parser")

  grids = soup.find_all("div", attrs={"class": "col-md-4 col-xs-12 pm-location"})

  for grid in grids:
    name = grid.find("h4").text

    address = grid.find("span").text


    full_address = grid.find("a").text
    city_state_zipp = full_address.replace(address, "").strip()
    city = city_state_zipp.split(", ")[0]
    state = city_state_zipp.split(", ")[1].split(" ")[0]
    zipp = city_state_zipp.split(", ")[1].split(" ")[1]
    print(city_state_zipp)
    print(zipp)


