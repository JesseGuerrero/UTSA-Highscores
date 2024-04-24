import requests
from bs4 import BeautifulSoup

# URL of the page (modify this according to your needs)
def _getHSValues(userID: str, name: str) -> dict:
    url = f'https://scholar.google.com/citations?user={userID}'

    # Fetch the page
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return {"name": "", "h_index": -1, "citations": -1}

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table by ID
    table = soup.find('table', id='gsc_rsb_st')

    # Check if the table was found
    if not table:
        print("Table not found")
        return {"name": "", "h_index": -1, "citations": -1}

    # Get the first and second `tr` elements
    rows = table.find_all('tr')
    if len(rows) < 2:
        print("Not enough rows in the table")
        return {"name": "", "h_index": -1, "citations": -1}

    # Extract values from the second `td` of the first and second `tr`
    citations = rows[0].find_all('td')[1].text
    hIndex = rows[1].find_all('td')[1].text
    return {"name": name, "h_index": hIndex, "citations": citations}

def getHSInfo(demographic: str):
    hsInfo = []
    with open(f'{demographic}.txt', 'r') as file:
        for line in file:
            user = line.split('-')
            if len(user) == 2:
                hsInfo.append(_getHSValues(user[0], user[1]))
            else:
                print("Line format error:", line)
    return hsInfo


