from sgselenium import SgChrome

with SgChrome() as driver:
  driver.get("https://www.rockandbrews.com/locations")

  stuff = driver.find_element_by_xpath(f"//div[@class = 'pm-location-search-list']").text.strip()

  print(stuff)
print("done")