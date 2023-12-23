# Logo Scraper
This is a webscraper built using python to collect and download logos for various companies from [1000logos](https://1000logos.net/). It uses a combination of **python requests** and **beautiful soup** to collect the top10 logos for the specified categories and downloads their images automatically.

It uses the python threading module to download images for each of the categories simultaneously to make the process much faster. It also uses the session module to set 
pre-defined custom headers ensuring that the scraper is not blocked from the website.

> This project was used to collect data as part of the preparatory stages for the [Logo API](https://github.com/edgarmuyomba/logos-api.git) - A free api used to retrieve various company logos. Check out the live demo [here]()

## Requirements
1. Make sure to create the category folders you want
2. The names of the folders should match the categories listed in [index.py](./index.py)
3. Make sure to specify the default image type while downloading. the default is set to png
4. Make sure to install all listed requirements in the [requirements.txt](./requirements.txt)

## Built using
1. [Requests](https://pypi.org/project/requests/)
2. [Session](https://www.geeksforgeeks.org/session-objects-python-requests/)
3. [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
4. [Threading](https://www.geeksforgeeks.org/multithreading-python-set-1/)

> [!CAUTION]
> The scraper might fail to work as intended due to changes in the website layout. If you're proficient in webscraping using python, feel free to modify the code otherwise regular maintenance updates will be rolled out. 