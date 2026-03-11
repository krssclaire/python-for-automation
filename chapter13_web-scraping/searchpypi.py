'''
# Get search page
import requests, sys, webbrowser, bs4

print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]) + '&o=')
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# From here, this is a deprecated way of opening a browser tab for each result
link_elems = soup.select('.package-snippet')
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)
'''

# Modern way of opening PyPI - Code by ChatGPT
import requests
import webbrowser

package = "requests"

url = f"https://pypi.org/pypi/{package}/json"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    project_url = data["info"]["project_url"] or data["info"]["package_url"]
    print("Opening:", project_url)
    webbrowser.open(project_url)
else:
    print("Package not found.")