# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

from splinter import Browser

location_name = 'Greater Manchester'
price_low = 500000
price_high = 100000
beds_low = 1
beds_high = 3

with Browser("phantomjs") as browser:
    # Optional, but make sure large enough that responsive pages don't
    # hide elements on you...
    browser.driver.set_window_size(1280, 1024)

    # Open the page you want...
    browser.visit("http://www.rightmove.co.uk/")

    # submit the search form...
    browser.fill_form(location_name, form_id='initialSearch', name='searchLocation')
    button = browser.find_by_css("button[name='buy']")
    button.click()
    
    brower.select(name='minPrice', price_low)
    brower.select(name='maxPrice', price_high)
    brower.select(name='minBedrooms', bed_low)
    brower.select(name='maxBedrooms', bed_high)
    button2 = brower.find_by_css("button[id='submit]")
    button2.click()

    # Scrape the data you like...
    links = browser.find_by_css(".search-results .list-group-item")
    for link in links:
        print link['href']

#
# # Read in a page
#html = scraperwiki.scrape("http://www.rightmove.co.uk/")
#
# # Find something on the page using css selectors
#root = lxml.html.fromstring(html)
#root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
