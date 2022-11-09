# Railroad Locomotive Web Scraper

_Created in September 2022_

A small web scraping project that intakes a railroad company owner's reporting mark (e.g. `NS`, `BNSF`, ...) and a locomotive number.

The program then scrapes http://www.rrpicturearchives.net/ to find that locomotive, searching through pages using a divide-and-conquer algorithm to reduce the average searching time (especially for locos with higher numbers). It returns the locomotive model as well as any associated notes.

I made this program as a way to demonstrate the `bs4` and `requests` python libs (you can install both via pip). It also demonstrates that I'm too obsessed with trains lol.

## Demonstration

![image](https://i.imgur.com/Rh0Hnvt.gif)

## Notes

There is a 1.5 second timeout between scrapes to avoid overloading the website's servers.
