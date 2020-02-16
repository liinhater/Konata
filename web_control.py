#Invoke package
from selenium import webdriver

#Open browser
browser = webdriver.Firefox()
browser.get("http://isbn.ncl.edu.tw/NEW_ISBNNet/H30_SearchBooks.php?&Pact=DisplayAll4Simple")

#Use xPath Finder to find xpath
search_category = browser.find_element_by_xpath("/html/body/section/div/div/div[2]/div[2]/"\
	"form[1]/div[1]/div/div[2]/select")
#Filter specific item
search_category.send_keys("ISBN")

search_isbn_num = browser.find_element_by_xpath("//*[@id='FO_SearchValue0']")
search_isbn_num.send_keys("978-986-3125-73-0")

search_icon = browser.find_element_by_xpath("/html/body/section/div/div/div[2]/div[2]/form[1]/div[2]/a")
search_icon.click()
#Note why search icon has to be double push
search_icon = browser.find_element_by_xpath("/html/body/section/div/div/div[2]/div[2]/form[1]/div[2]/a")
search_icon.click()

res = browser.find_element_by_xpath("/html/body/section/div/div/div[2]/div[2]/form[1]"\
	"/div[6]/table/tbody/tr[2]/td[3]/a")
res.click()
