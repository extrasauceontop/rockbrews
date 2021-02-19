from sgselenium import SgChrome
from bs4 import BeautifulSoup as bs

with SgChrome() as driver:
  driver.get("https://www.rockandbrews.com/locations")
  html = driver.page_source
  soup = bs(html, "html.parser")

  grids = soup.find_all("div", attrs={"class": "col-md-4 col-xs-12 pm-location"})

  for grid in grids:
    name = grid.find("h4").text
    full_address = grid.find("a").text.split("\n")
    address = full_address[0]
    city = full_address[1].split(", ")[0]
    state = full_address[1].split(",")[1].split(" ")[0]
    zipp = full_address[1].split(",")[1].split(" ")[1]
    print(zipp)


