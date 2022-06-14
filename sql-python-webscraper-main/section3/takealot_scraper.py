from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup

url = "https://www.takealot.com/russell-hobbs-2200w-crease-control-iron/PLID34147865"

# configure Chrome Webdriver


def configure_chrome_driver():
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            'section3/utils/chromedriver', options=chrome_options)
        return driver
    except Exception as e:
        print(e)
        return None


def get_data(url):
    try:
        driver = configure_chrome_driver()
        driver.get(url)

        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_class_name("sf-expanded"))

        html_data = driver.page_source
        soup = BeautifulSoup(html_data, 'html.parser')
        price = soup.find(
            'span', {'data-ref': 'buybox-price-main'})

        availability = soup.find(
            'div', {'class': 'cell shrink stock-availability-status'})

        seller = soup.find(
            'div', {'class': 'seller-information'})

        try:
            nextAvailableOfferPrice = soup.find(
                'span', {'class': 'currency plus currency-module_currency_29IIm'})

            nextAvailableOfferStock = soup.find(
                'div', {'class': 'cell shrink stock-availability-status'})

            nextAvailableOfferSeller = soup.find(
                'div', {'class': 'seller-information'})

            nextAvailableOffer = {
                'price': nextAvailableOfferPrice.text,
                'stock': nextAvailableOfferStock.text,
                'seller': nextAvailableOfferSeller.text
            }

        except:
            nextAvailableOffer = None

        data = {
            "Price: ": price.text,
            "Availabiltiy ": availability.text,
            "Seller": seller.text,
            "Next offer": nextAvailableOffer
        }

        driver.quit()
        return data

    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    print(get_data(url))
