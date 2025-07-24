from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#Инициализация драйвера
driver = webdriver.Chrome()
driver.maximize_window()

try:
    #Используем бинг, так как с yahoo проблемы
    driver.get("https://www2.bing.com/")

    # Передаём selenide в поиск
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("selenide" + Keys.RETURN)

    #Проверяем первый результат
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.b_algo h2 a"))
    )
    first_result_href = first_result.get_attribute("href")
    assert "selenide.org" in first_result_href.lower(), f"First result ({first_result_href}) is not selenide.org"

    #По умолчанию в хроме изображения
    # открываются в новом окне
    #Поэтому храним текущее окно
    main_window = driver.current_window_handle

    # Переход на вкладку изображений
    images_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='images']"))
    )

    ActionChains(driver).key_down(Keys.CONTROL).click(images_tab).key_up(Keys.CONTROL).perform()

    # Переключаемся на новую вкладку
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])

    # Проверяем ссылку в первом изображении
    try:
        first_image_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.img_cont, a.iusc"))
        )
        parent_link = first_image_container.get_attribute("href")
    except:
        first_image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.mimg, img.rms_img"))
        )
        parent_link = first_image.find_element(By.XPATH, "./ancestor::a").get_attribute("href")

    print("Parent link found:", parent_link)
    assert parent_link and "selenide.org" in parent_link.lower(), f"Image parent link ({parent_link}) is not from selenide.org"

    # Возвращаемся на основное окно
    driver.close()
    driver.switch_to.window(main_window)

    # Проверяем,что первый результат тот же
    new_first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.b_algo h2 a"))
    )
    assert new_first_result.get_attribute(
        "href") == first_result_href, "First result changed after returning from images"

    print("Done successfully")

finally:
    time.sleep(2)
    driver.quit()