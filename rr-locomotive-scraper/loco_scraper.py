import math
import requests
import os
import time
from bs4 import BeautifulSoup

def strip_element(str):
    '''
    Takes a page element, extracts the text out of it and strips it of unneeded whitespace

    Params:
        str: An element of a ResultsSet array

    Returns:
        (str): The text of the element with no extra whitespace
    '''
    return str.get_text().strip()

def main():
    query_owner = ''
    while query_owner == '':
        query_owner = input('Enter the reporting mark of the company of this loco > ').upper()

    query_num = ''
    while query_num == '':
        query_num = input('Enter the number of this loco > ')

    page = requests.get('http://www.rrpicturearchives.net/locoList.aspx?id=' + query_owner + '&Page=1') # fetch the first page to get the last page
    soup = BeautifulSoup(page.text, 'html.parser') # returns HTML that is easier to work with

    max_page = soup.find_all('span', {"id":"ctl00_ContentPlaceHolder1_Pager_TotalPages"})[0].get_text()

    done = False

    if int(max_page) == 0:
        os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal (makes it look nicer!)
        print('This operator does not exist.')
        done = True

    item_index = -2 # this is basically what cell of each row we are looking at (0 - 4)
    # there are two 'td' fields that aren't in the main table, so skip those two.

    lower_page_bound = 1
    upper_page_bound = int(max_page)

    while not done: # keep searching through pages till we either find the item or can't
        os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal (makes it look nicer!)
        search_page = math.floor((lower_page_bound + upper_page_bound) / 2)
        print('Searching page ' + str(search_page) + ' of ' + str(max_page) + '... (lower: ' + str(lower_page_bound) + ' upper: ' + str(upper_page_bound) + ')')

        page = requests.get('http://www.rrpicturearchives.net/locoList.aspx?id=' + query_owner + '&Page=' + str(search_page))
        soup = BeautifulSoup(page.text, 'html.parser') # gets HTML

        entries = soup.find_all('td', {"class":"DefText"}) # get all entries on this page's table

        for entry in range(len(entries)):
            this_item = strip_element(entries[entry]).replace('\xa0', ' ')
            if item_index != 0:
                item_index += 1
                if item_index > 4:
                    item_index = 0
                continue
            if (query_owner in this_item) and item_index == 0:
                separated = this_item.split(' ')
                if len(separated) != 2:
                    continue
                try:
                    if int(separated[1]) == int(query_num):
                        relevant_data = entries[entry:entry+3]
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Found ' + strip_element(relevant_data[0]) + ' on page ' + str(search_page))
                        print('This loco is a(n) ' + strip_element(relevant_data[2]))
                        if strip_element(relevant_data[1]) != '':
                            print('Notes: ' + strip_element(relevant_data[1]))
                        done = True
                        break
                    elif int(separated[1]) > int(query_num):
                        if upper_page_bound == lower_page_bound:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Couldn\'t find ' + query_owner + ' ' + query_num)
                            done = True
                            break
                        upper_page_bound = search_page
                    elif int(separated[1]) < int(query_num):
                        if upper_page_bound == lower_page_bound:
                            # os.system('cls' if os.name == 'nt' else 'clear')
                            print('Couldn\'t find ' + query_owner + ' ' + query_num)
                            done = True
                            break
                        lower_page_bound = search_page
                except ValueError:
                    continue
            else:
                continue

            item_index += 1
            if item_index > 4:
                item_index = 0
        
        if done:
            break

        time.sleep(1.5)

    input('\nPress enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')   

main()
