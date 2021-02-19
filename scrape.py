from sgselenium import SgChrome

with SgChrome() as driver:
  driver.get("https://www.rockandbrews.com/locations")

  stuff = driver.find_elements_by_xpath(f"//div[@class = 'col-md-4 col-xs-12 pm-location']")
  for element in stuff:
    e_text = element.text.split("\n")
    print(e_text[0])

print("done")