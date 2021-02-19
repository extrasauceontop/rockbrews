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
    print(address)


