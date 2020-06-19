import time
link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_language_add_to_basket(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    basket = len(browser.find_elements_by_css_selector('.btn-add-to-basket'))
    print(basket)
    time.sleep(10)
    assert basket > 0, 'Кнопки не нашлось на сайте((('


