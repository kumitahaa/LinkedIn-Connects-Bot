# --------------------------------- Import -------------------------------------
import traceback, time
# import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials
# import undetected_chromedriver as uc
from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from credits_local import EMAIL, PASSWORD
# from credits import EMAIL, PASSWORD



# --------------------------------- Variables Used -------------------------------------
driver = ""
lnbr = "=="*30
connect_count = 0
names_str = """Ali Ahmed Kumail Taha Rehman Asad Naeem Huzaifa"""
names = names_str.split(" ")


# --------------------------------- Initialize -------------------------------------
def init():
    global driver


    options = uc.ChromeOptions()

    driver = uc.Chrome(options=options)
    driver.maximize_window()


# --------------------------------- Open Login Page -------------------------------------
def open_page():
    print(lnbr)
    print("Start OPEN_PAGE of function")
    
    print("Opening Webpage")
    url = f"https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    driver.get(url)

    print("OPENED Webpage...")

    print("End of OPEN_PAGE function")
    print(lnbr)

# --------------------------------- Starts from Here -------------------------------------
def start():
    print(lnbr)
    print("Start START of function")

    login(EMAIL,PASSWORD)
    for name in names:
        search_people(name)
        send_connects()
    
    print("End of START function")
    print(lnbr)

# --------------------------------- Login -------------------------------------
def login(EMAIL, PASSWORD):
    print(lnbr)
    print("Start LOGIN of function")
    try:
        login_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

        login_field.clear()
        login_field.send_keys(EMAIL)

        password_field.clear()
        password_field.send_keys(PASSWORD)

        password_field.send_keys(Keys.ENTER)

        print("Entered Login Data...")

    except Exception as e:
        print(f"Error on Login Field: {e}")
        print("Calling Login Again")
        login(EMAIL, PASSWORD)
        return 0

    # Check if Logged in properly
    try:
        print("Checking Login")
        search_field = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "search-global-typeahead__input")))
        print("We are logged in properly...")
    except:
        print("Can't Find Search Bar, we are not properly Logged-In yet...")
        login(EMAIL, PASSWORD)
        return 0

    print("End of LOGIN function")
    print(lnbr)


# --------------------------------- Search People -------------------------------------
def search_people(name):
    print(lnbr)
    print("Start SEARCH_PEOPLE of function")

    try:
        print("Looking for Search Bar")
        search_field = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "search-global-typeahead__input")))[0]
        print("Found the Search Bar")
        try:
            search_field.click()
            search_field.clear()
            search_field.send_keys(name)
            search_field.send_keys(Keys.ENTER)
            print(f"Searched for {name}")
        except Exception as e:
            print(f"Error on searching within Search Bar.... Error: {e}")
    except Exception as e:
        print(f"Can't Find Search Bar.... Error: {e}")

    print("Loading Time Wait...")
    time.sleep(8)
    
    try:
        driver.execute_script("""
document.getElementsByClassName("artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 search-reusables__filter-pill-button search-reusables__filter-pill-button")[0].click()""")
    except:
        print("Can't Apply PEOPLE Filter")

    print("Loading Time Wait...")
    time.sleep(5)
    
    print("End of SEARCH_PEOPLE function")
    print(lnbr)

# --------------------------------- Send Connects -------------------------------------
def send_connects():
    print(lnbr)
    print("Start SEND_CONNECTS of function")
    
    global connect_count

    try:
        print("Finding Buttons")
        buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "artdeco-button--secondary")))
        print("Found Buttons")
        for button in buttons:
            if "onne" in button.text:
                print("Sending Without Message")
                try:
                    button.click()
                    connect_count += 1
                    print(f"Sent Connect...{connect_count}")
                    check_note()
                except:
                    print("Can't Send Connect Request to this one...")
            elif "essag" in button.text:
                print("Sending WITH Message")
                try:
                    button.click()
                    connect_count += 1
                    print(f"Sent Message Connect...{connect_count}")
                    send_message()
                except:
                    print("Can't Send Message to this one...")
    except:
        print("Can't Find Buttons for connects")
    
    print("End of SEND_CONNECTS function")
    print(lnbr)

# --------------------------------- Check if there is Connect Note -------------------------------------
def check_note():
    print(lnbr)
    print("Start CHECK_NOTE of function")

    try:
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "send-invite-modal")))
        try:
            without_note = WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "artdeco-button__text")))[2]
            without_note.click()
            print("Chose SEND WITHOUT NOTE...")
        except:
            print("Can't Find SEND WITHOUT NOTE Button...")
    except:
        print("SEND NOTE Popup didn't appear...")
    
    print("End of CHECK_NOTE function")
    print(lnbr)

# --------------------------------- Send Message for Connect -------------------------------------
def send_message():
    print(lnbr)
    print("Start SEND_MESSAGE of function")
    
    try:
        send_btn = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "msg-form__send-button artdeco-button artdeco-button--1")))[0]
        send_btn.click()
    except:
        print("Can't Click Send Message Button...")

    print("End of SEND_MESSAGE function")
    print(lnbr)
    
# --------------------------------- Driver of program -------------------------------------
def driver():
    init()
    open_page()
    start()
    print("End of Program...")
    time.sleep(10)
    


# --------------------------------- Function Call andHandling -------------------------------------
try:
    current_date = datetime.now()
    end_date = datetime(2024, 9, 2)  # Year, Month, Day
    if current_date < end_date:
        driver()
    else:
        for i in range(10):
            print("============ ERRROOORRRRRRRRRROOOOORRRRRR ============")
            print("=================== Contact Kumail Taha for the Error.... ===================")
            time.sleep(5)

except Exception as e:
    # exception_occurred = True
    print("==="*30)
    print("==="*30)
    print("ENDING.... EXCEPTION...")
    print("==="*30)
    print("==="*30)
    print(f"Exception occured: {e}")
    traceback.print_exc()
else:
    pass
finally:
    # time.sleep(10)
    
    print("Quitting Now")
    driver.quit()
    