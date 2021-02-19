from sgselenium import SgChrome

with SgChrome() as driver:
  html = driver.get("https://www.rockandbrews.com/locations").page_source

  print(html)
print("done")