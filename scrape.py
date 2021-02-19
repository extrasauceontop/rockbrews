from sgselenium import SgChrome

with SgChrome() as driver:
  driver.get("https://www.helegas.com/")

  print("done")