from selenium.webdriver.common.by import By

from nicegui import __version__

from .screen import Screen


def test_dev_mode(screen: Screen) -> None:
    screen.ui_run_kwargs['development'] = True
    screen.open('/')
    screen.selenium.find_element(By.XPATH, f'//script[@src="/_nicegui/{__version__}/static/vue.global.js"]')
    screen.selenium.find_element(By.XPATH, f'//script[@src="/_nicegui/{__version__}/static/quasar.umd.js"]')


def test_prod_mode(screen: Screen):
    screen.ui_run_kwargs['development'] = False
    screen.open('/')
    screen.selenium.find_element(By.XPATH, f'//script[@src="/_nicegui/{__version__}/static/vue.global.prod.js"]')
    screen.selenium.find_element(By.XPATH, f'//script[@src="/_nicegui/{__version__}/static/quasar.umd.prod.js"]')
