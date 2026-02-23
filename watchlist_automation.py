from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"              #Replace with your browser location    
chromedriver_path = r"D:\Python_Bots\ABC\chromedriver.exe"                                      #Replace with your Chromedrive location       
profile_path = r"D:\Python_Bots\ABC\brave_selenium_profile"                                     #Replace with your Selenum profile          

options = Options()
options.binary_location = brave_path
options.add_argument(fr'user-data-dir={profile_path}')

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

    # --- Step 1: Go to Industry Page (you're already logged in)
industry_urls = [
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/major-banks/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/information-technology-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/oil-refining-marketing/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/finance-rental-leasing/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/wireless-telecommunications/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/regional-banks/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/pharmaceuticals-major/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/motor-vehicles/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electric-utilities/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/life-health-insurance/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electrical-products/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/household-personal-care/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/steel/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/engineering-construction/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/construction-materials/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/industrial-specialties/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/real-estate-development/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/auto-parts-oem/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/aerospace-defense/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/tobacco/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/chemicals-specialty/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/other-metals-minerals/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/industrial-machinery/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/hospital-nursing-management/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/alternative-power-generation/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/air-freight-couriers/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/trucks-construction-farm-machinery/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/financial-conglomerates/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/wholesale-distributors/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/other-transportation/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/packaged-software/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/chemicals-agricultural/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/miscellaneous-commercial-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/other-consumer-specialties/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/specialty-stores/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/investment-banks-brokers/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/metal-fabrication/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/apparel-footwear-retail/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/gas-distributors/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/internet-software-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/food-specialty-candy/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/investment-managers/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/pharmaceuticals-other/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/multi-line-insurance/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/agricultural-commodities-milling/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/hotels-resorts-cruise-lines/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/food-major-diversified/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/coal/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/beverages-alcoholic/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/aluminum/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/airlines/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/integrated-oil/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electronic-production-equipment/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/miscellaneous-manufacturing/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/data-processing-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/apparel-footwear/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/automotive-aftermarket/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/specialty-insurance/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electronic-equipment-instruments/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/textiles/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/beverages-non-alcoholic/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/semiconductors/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/major-telecommunications/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/industrial-conglomerates/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/internet-retail/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/chemicals-major-diversified/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/restaurants/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/real-estate-investment-trusts/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/other-consumer-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/medical-nursing-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/building-products/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/home-furnishings/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electronics-appliances/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/broadcasting/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/railroads/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/movies-entertainment/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/homebuilding/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/containers-packaging/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/telecommunications-equipment/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/food-meat-fish-dairy/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electronics-distributors/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/marine-shipping/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/medical-specialties/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/office-equipment-supplies/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/forest-products/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/trucking/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/pulp-paper/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/specialty-telecommunications/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electronic-components/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/consumer-sundries/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/financial-publishing-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/computer-peripherals/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/drugstore-chains/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/electronics-appliance-stores/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/biotechnology/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/publishing-newspapers/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/personnel-services/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/oilfield-services-equipment/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/catalog-specialty-distribution/",
    "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/environmental-services/"
]

wait = WebDriverWait(driver, 30)

try:
    for idx, industry_url in enumerate(industry_urls):
        print(f"\nProcessing {industry_url} ({idx+1}/{len(industry_urls)})")

        try:
            driver.get(industry_url)
            time.sleep(8)  # Let the page load, avoid being too aggressive

            # Debug screenshot at start of page
            driver.save_screenshot(f"debug_{idx+1}_pageload.png")

            # --- Wait for table and select all rows ---
            stock_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr')))
            stock_rows = stock_rows[2:]  # Skip first two rows

            if not stock_rows:
                print(f"No stock rows found for {industry_url}")
                continue

            # Select all stocks: click first, then Shift+click last
            actions = ActionChains(driver)
            actions.move_to_element(stock_rows[0]).click().perform()
            actions.key_down(Keys.SHIFT).click(stock_rows[-1]).key_up(Keys.SHIFT).perform()
            time.sleep(1)

            # --- Right-click to open context menu ---
            actions = ActionChains(driver)
            actions.context_click(stock_rows[0]).perform()

            # --- Hover "Add selected to Watchlist" ---
            add_watchlist = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Add selected to Watchlist')]"))
            )
            actions = ActionChains(driver)
            actions.move_to_element(add_watchlist).perform()
            time.sleep(1)

            # --- Click "Create new list" ---
            create_new_list = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Create new list')]"))
            )
            create_new_list.click()

            # --- Name the list and save ---
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.main-B02UUUN3')))
            modal = driver.find_element(By.CSS_SELECTOR, '.main-B02UUUN3')

            list_name = industry_url.strip('/').split('/')[-1]
            input_box = modal.find_element(By.CSS_SELECTOR, "input.input-RUSovanF")
            input_box.clear()
            input_box.send_keys(list_name)
            time.sleep(0.7)  # Let the input register

            save_btn = modal.find_element(By.CSS_SELECTOR, "button[name='save']")
            wait.until(lambda d: save_btn.is_enabled())
            save_btn.click()
            print(f"Created watchlist: {list_name}")

            time.sleep(2)  # Let modal close before next iteration

        except (TimeoutException, WebDriverException) as e:
            print(f"Timeout/WebDriver error on {industry_url}: {e}")
            # Save screenshot for failed page
            driver.save_screenshot(f"error_{idx+1}.png")
            continue
        except Exception as e:
            print(f"General error on {industry_url}: {e}")
            driver.save_screenshot(f"error_{idx+1}_exception.png")
            continue

finally:

    driver.quit()
