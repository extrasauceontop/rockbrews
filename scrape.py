from sgselenium import SgChrome

with SgChrome() as driver:
  driver.get("https://www.rockandbrews.com/locations")

  stuff = driver.find_element("body")

  print(stuff)
print("done")