from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import os
import shutil
import time

basic_url = "https://www.finnomena.com"

def part1(table_sticky_div):
    """Collect fund names and links"""
    counter = 0
    names = []
    links = []
    print('\nCollecting fund names and links:-\n')
    anchor_tags = table_sticky_div.find_all('a')
    for a in anchor_tags:
        text = a.text
        link = a['href']
        names.append(text)
        links.append(link)
    return names, links

def part2(div):
    print("\nCollecting other info:- \n")
    try:
        result = []
        div = div.find_all("div", class_="table-scroll-x")

        result_set_string = ''.join(str(item.text) for item in div)
        result = result_set_string.split('\n')
        cleaned_list = [item.strip() for item in result if item.strip() != ""]
        group_size = 4
        grouped_list = [cleaned_list[i:i+group_size] for i in range(0, len(cleaned_list), group_size)]
        # print(grouped_list)
    except Exception:
        print("Div returns None type object, please try again or modify the url")
    return grouped_list


def get_data(table_sticky_div, filter_table_div):
    names, links = part1(table_sticky_div)
    grouped_list = part2(filter_table_div)
    return (names, links, grouped_list)

def dump_data(names, links, grouped_list, file_name):
    # print(len(names), len(grouped_list))
    with open(file_name, 'w', encoding='utf-8') as fl:
        items = []
        try:
            for i, j in zip(range(2, 102), range(1, 102)):
                string = {
                    "fund_name": f"{names[i]}",
                    "return_perc": f"{grouped_list[i-1][1]}",
                    "asset_management": f"{grouped_list[i-1][0]}",
                    "link": f"{basic_url}{links[i]}"
                }
                items.append(string)
                # json.dump(string, fl)
                # fl.write("\n")
            json.dump(items, fl, indent=2)
        except IndexError as e:
            print("This webpage had less than 100 entries")
            json.dump(items, fl, indent=2)

def main(page, size):
    # Set up ChromeDriver path
    chrome_driver_path = '/path/to/chromedriver'
    # chrome_driver_path = './chromedriver'
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run ChromeDriver in headless mode
    chrome_options.add_argument('--no-sandbox')

    # Create a new ChromeDriver instance
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print('Starting browser')
    time.sleep(5)

    # Create new directory for output files
    try:
        print('Creating directory names "output"')
        os.mkdir('output')
    except FileExistsError as e:
        print('Directory "output" already exists\nRemove "output"')
        shutil.rmtree('output')
        print('Successfully removed "output"\nCreating "output" again')
        os.mkdir('output')

    url = f'https://www.finnomena.com/fund/filter?page={page}&size={size}'
    print(f'Initializing request for url - {url}')
    driver.get(url)
    print(f"Collecting data for:-\n PAGE: {page}\n SIZE: {size}")
    print(f'Url looks like:- {url}')
    # Get the page source after dynamic content has loaded
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table_sticky_div = soup.find("div", class_="table-sticky")
    filter_table_div = soup.find("div", class_="filter-table")
    # get data
    names, links, grouped_list = get_data(table_sticky_div, filter_table_div)
    # dump into json file
    file_name = f'output/output{page}.json'
    try:
        dump_data(names, links, grouped_list, file_name)
    except FileNotFoundError as e:
        print('This is not valid file path.\nCreate directory named output on the same level as main.py fil')

    # Close the browser
    driver.quit()
