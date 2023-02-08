import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import glob
import time

x = '/home/angus/projects/wyzant/carson'
def main(downloadpath,i):

        downloadpath +='/'+str(i)
        options = Options()
        options.set_preference("browser.download.folderList", 2)
        options.headless = False
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
        options.set_preference("browser.download.dir",downloadpath)

        lower = 56000
        higher= 56500

        length = len(glob.glob(downloadpath +'/*'))

        while higher < 64000:

            driver = selenium.webdriver.Firefox(options=options)
            driver.get(f'https://www.cms.gov/medicare/physician-fee-schedule/search?Y={i}&T=4&HT=2&CT=3&H1={str(lower).zfill(5)}&H2={str(higher).zfill(5)}&M=5')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH,'/html/body/div[2]/div/div/main/div/div[2]/div/div/inner/div[1]/div[2]/div/form/div[2]/input').click()

            try:
                driver.find_element(By.CLASS_NAME,'ds-c-alert__body')
                print(f"HCPCS: {lower}-{higher} no data")
            except NoSuchElementException as exception:
                try:
                    print(f'Downloading {lower}-{higher}')
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    driver.implicitly_wait(10)
                    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/main/div/div[2]/div/div/inner/div[1]/div[1]/div/div/div/div[2]/section[2]/div/div[5]/button[1]')))
                    element.click()
                    while True:
                        curLen = len(glob.glob(downloadpath +'/*'))


                        if curLen > length:
                            Download_name = glob.glob(downloadpath +'/*')[-1].split('/')
                            if (Download_name[7][-3:]) == 'csv':
                                time.sleep(.1)
                                break
                        else:
                            time.sleep(.1)

                finally:
                    length = len(glob.glob(downloadpath +'/*'))
                    print(f'Downloaded HCPCS{lower}-{higher} year {i}')
                    time.sleep(.2)
                    driver.quit()
            finally:
                lower += 500
                higher += 500
                time.sleep(.3)
                driver.quit()


for i in range(25,27):
    main(x,i)
