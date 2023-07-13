from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Установите путь к драйверу Chrome, если необходимо
# chrome_driver_path = "путь_к_драйверу"

# Инициализация Chrome WebDriver с помощью Selenium
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск браузера в фоновом режиме
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
# Открытие страницы Яндекс.Карт Новосибирска
city = "Новосибирск"
search_query = "Кафе"
url = f"https://yandex.ru/maps/?text={search_query}"
driver.get(url)

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-form-view__input")))

# Получение HTML-содержимого страницы
html = driver.page_source

# Закрытие WebDriver
driver.quit()

# Обработка HTML-содержимого с помощью BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Найдем список результатов поиска
results = soup.find_all("ul", class_="search-list-view__list")

# Выводим информацию о каждом результате
for result in results:
    titles = result.find_all("div", class_="search-business-snippet-view__title")
    addresses = result.find_all("div", class_="search-business-snippet-view__address")
    ratings = result.find_all("span", class_= "business-rating-badge-view__rating-text _size_m")
    awards = result.find_all("div", class_= "business-header-awards-view__award-text")

    for title, address, rating, award in zip(titles, addresses, ratings, awards):
        print("Название:", title.text.strip())
        print("Адрес:", address.text.strip())
        print("Рейтинг:", rating.text.strip())
        print("Награда:", award.text.strip())
        print("------------------------")
