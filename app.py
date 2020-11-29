from tkinter import * # gui
from tkinter import messagebox #Needed for exit function.
from selenium import webdriver  # driver
from selenium.webdriver.common.keys import Keys
from functools import partial # function works when pressed
import time # time module

PATH = "C:\Program Files (x86)\chromedriver.exe"

def visit_url(ur):
    driver = webdriver.Chrome(PATH)
    text = ur.get() #stringvar to string
    driver.get(text)

def buyItem(url):
    driver = webdriver.Chrome(PATH)
    text = url.get() #stringvar to string
    driver.get(text)
    order(driver,myFirstName,myLastName,myEmail, myPassword)

def order(driver,myFirstName,myLastName,myEmail, myPassword):
    addToCart = '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span'
    checkOut = '//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]'
    username = '//*[@id="sign-in-email"]'
    password = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[2]/div/div[1]/label/div[2]/div/input'
    continueWithAccount = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[5]/button/span'
    firstContinue = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span'
    firstName ='//*[@id="people[0].firstName"]'
    lastName = '//*[@id="people[0].lastName"]'
    email = '//*[@id="people[0].email"]'
    confirmInfo = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/form/div/div[3]/div/div/button[1]/span'
    reviewOrder = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button/span/span'
    confirmOrder = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button/span'

    #Add Item To Cart And To Checkout 
    clickAddToCartButton(addToCart, driver)
    time.sleep(1)
    clickButton(checkOut, driver)
    time.sleep(1)
    enterData(username, myEmail.get(), driver)
    enterData(password, myPassword.get(), driver)
    clickButton(continueWithAccount, driver)
    time.sleep(1)

    #Signs up to Walmart Account
    clickButton(firstContinue, driver)
    enterData(firstName, myFirstName.get(), driver)
    enterData(lastName, myLastName.get(), driver)
    enterData(email, myEmail.get(), driver)
    clickButton(confirmInfo, driver)

    #ORDER
    clickButton(reviewOrder)
    clickButton(confirmOrder)

def clickAddToCartButton(xpath,driver):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(5)
        driver.refresh();
        clickAddToCartButton(xpath, driver)

def clickButton(xpath ,driver):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(1)
        clickButton(xpath, driver)

def enterData(field,data ,driver):
    try:
        driver.find_element_by_xpath(field).send_keys(data)
        pass
    except Exception:
        time.sleep(1)
        enterData(field,data, driver)

#Window variables
root = Tk()
root.title('PS5 bot')
root.geometry("800x600")

# form
lableName = Label(root, text="First Name: ")
lableName.grid(column = 0, row = 10, pady=10)
myFirstName = StringVar()
nameEntered = Entry(root, width=25, textvariable = myFirstName)
nameEntered.grid(column = 1, row = 10, pady=10)

lableLast = Label(root, text="Last Name: ")
lableLast.grid(column = 0, row = 15 ,pady=10)
myLastName = StringVar()
lastEntered = Entry(root, width=25, textvariable = myLastName)
lastEntered.grid(column = 1, row = 15,padx=10, pady=10)

lableMail = Label(root, text="Email Address: ")
lableMail.grid(column = 0, row =20,padx=10, pady=10)
myEmail = StringVar()
mailEntered = Entry(root, width=30, textvariable = myEmail)
mailEntered.grid(column = 1, row = 20,padx=10, pady=10)

lablePassword = Label(root, text="Password: ")
lablePassword.grid(column = 0, row = 25 ,pady=10)
myPassword = StringVar()
passwordEntered = Entry(root, width=25, textvariable = myPassword)
passwordEntered.grid(column = 1, row = 25,padx=10, pady=10)

lableURL = Label(root, text="URL: ")
lableURL.grid(column = 0, row = 30 ,pady=10)
myURL = StringVar()
URLEntered = Entry(root, width=25, textvariable = myURL)
URLEntered.grid(column = 1, row = 30,padx=10, pady=10)

visit = Button(root, text="Visit Item", bg="blue", fg="white", command=partial(visit_url,myURL))
visit.grid(column = 0, row = 40)
buy = Button(root, text="Buy Item", bg="blue", fg="white", command=partial(buyItem,myURL))
buy.grid(column = 1, row = 40)

root.mainloop()