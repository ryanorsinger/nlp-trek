import pandas as pd
import re
import requests
import nltk
from bs4 import BeautifulSoup

def get_episode_name(soup):
    episode_name = soup.p.contents[0].text
    episode_name = episode_name.replace("\n", "")
    episode_name = episode_name.replace("\r", " ")
    return episode_name


def get_dates(soup):
    starting_stardate = soup.p.contents[3].text
    parts = starting_stardate.split("\r\n")
    starting_stardate = " ".join(parts[0:2])
    original_airdate = parts[2].strip()
    return {
        "stardate": starting_stardate, 
        "original_airdate": original_airdate
    }


# TODO: this is_dialog has a slight issue with the first line after the captain's log intro if we split on " \r\n" in the get_episode function
def is_dialog(string):
    """
    Dialog lines start with one or more strings of all capitals and end with
    Returns a boolean if the given string is dialog or not
    """
    return bool(re.search(r'^[A-Z]+:', string))

assert is_dialog("DATA: Difficult? Simply solve the mystery of Farpoint Station.") == True
assert is_dialog('Copyright © 1966, Present. The Star Trek web pages on this site are for') == False
assert is_dialog('\n\n\n\n\n\nThe Next Generation Transcripts - Encounter at Farpoint\n\nEncounter') == False


def get_character(string):
    """
    Takes in a dialog string and returns the 
    """
    return string.split(":")[0]

assert get_character('RIKER: Construction records? ') == "RIKER"
assert get_character("WORF: We've been trying, sir. No response. ") == "WORF"


def get_episode(url):
    response = requests.get(url)

    # Make a soup variable holding the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    content = soup.text
    
    raw_lines = content.split(" \r\n")
    
    df = pd.DataFrame()
    
    # Filter out the dialog lines
    lines = [line for line in raw_lines if is_dialog(line)]
    df["lines"] = lines
    
    # TODO: Troubleshoot why some episode urls don't conform to this pattern and there's an out of index issue
    # dates = get_dates(soup)
    # df["original_airdate"] = dates["original_airdate"].replace("Original Airdate:", "")
    # df["stardate"] = dates["stardate"]
    
    df["episode_name"] = get_episode_name(soup)
    
    return df



def get_all_episode_urls(listing_url):
    response = requests.get(listing_url)
    soup = BeautifulSoup(response.text)
    links = soup.select("a")
    episode_urls = links[:-2]
    urls = [tag["href"] for tag in links]
    
    next_gen = "http://www.chakoteya.net/NextGen/"
    urls = [next_gen + url for url in urls]

    # Last 2 urls are not episode links
    urls = urls[:-2]
    urls
    episodes = []
    for url in urls:
        episode = get_episode(url)
        print(f"Processing episode from {url}")
        print("-----")
        episodes.append(episode)

    all_episodes = pd.concat(episodes)
    return all_episodes

