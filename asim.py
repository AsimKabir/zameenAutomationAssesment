import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def applyFiltersOnHomePage():
    driver = webdriver.Chrome('./webDrivers/chromedriver')
    url = "https://www.airbnb.com/"
    # url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    driver.get(url)
    driver.maximize_window()
    # Now entering location Rome, Italy on Home page
    ele_EnterLocation = driver.find_element_by_xpath("//*[@id='bigsearch-query-detached-query']") # Rome, Italy Location element 
    ele_EnterLocation.send_keys("Rome, Italy")
        # element = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div/div/div")
        # element.send_keys("Rome, Italy")
    time.sleep(3)
    # Now Clicking on the In date on home page
    ele_EnterDateField = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div[1]") # CheckIn field element
    ele_EnterDateField.click()
    time.sleep(3)
    # Now entering Check In date on home page
    ele_EnterCheckInDate = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div/div/div") # CheckIn date element
    ele_EnterCheckInDate.click()
    time.sleep(1)
    # Now entering CheckOut date on home page
    ele_EnterCheckOutDate = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[4]/section/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[7]/div/div/div") # Check out date element
    ele_EnterCheckOutDate.click()
    time.sleep(1)
    # Now clicking on the guest field of home page
    ele_GuestField = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div") # Guest Field Element
    ele_GuestField.click()
    time.sleep(1)

    # Now adding adults as guests on home page
    ele_AdultGuest = driver.find_element_by_xpath("//*[@id='stepper-adults']/button[2]") # Adult guests alement on home page
    ele_AdultGuest.click()
    time.sleep(1)
    ele_AdultGuest.click()
    time.sleep(1)
    # Now entering child Guest on home page
    ele_ChildGuest = driver.find_element_by_xpath("//*[@id='stepper-children']/button[2]") # Child guest element on home page
    ele_ChildGuest.click()
    time.sleep(2)

    # Now clicking on the element Search Button
    ele_SearchField = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[4]/button") # Button search element on home page
    ele_SearchField.click()
    time.sleep(5)
    return driver



def VerifyAppliedFiltersAreCorrect():

    driver = applyFiltersOnHomePage()
    print("PASSEEDD ASIM")

    ########################   Getting Filters from Container without Opening code starts here ##################################################### 
    # Now Getting text of location without opening FIlters on top Header
    ele_location = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]/div/button[1]/div") # top Header location filter element
    location_Text = ele_location.text
    print(location_Text)
    time.sleep(3)
    ## Now Getting text of Date Range without opening FIlters on top Header
    ele_Date = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]/div/button[2]/div") # Top Header Date Range text element
    date_Text = ele_Date.text
    print(date_Text)
    time.sleep(3)
    # Now Getting text of Guests without opening FIlters on top Header
    ele_Guests = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]/div/button[3]/div[1]") # Top Header Guests test element
    guests_Text = ele_Guests.text
    print(guests_Text)
    time.sleep(3)

    ########################   Getting Filters from Container without Opening code Enda here ##################################################### 

    ################################### Getting Filters from Container by Opening code Starts #######################################################################################################################################    

    # Clicking on the top Header filter to open and get filters details
    ele_DetailContainer = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[1]") #clicking on filter of Detailed Container element
    ele_DetailContainer.click()
    time.sleep(2)    

        
    # Now getting Location by Opening Container
    ele_DetailContainer_Location = driver.find_element_by_xpath("//*[@id='bigsearch-query-detached-query']") # Detailed Container location element after opening
    ele_DetailContainer_Location_Text = ele_DetailContainer_Location.get_attribute("value")
    print("by opening --->  ", ele_DetailContainer_Location_Text)
    # time.sleep(2)        

    # Now getting CheckIn Date by Opening Container
    ele_DetailContainer_Date_Checkin = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div[1]/div/div[2]") # Detailed Container location Date CheckIn by Opening
    ele_DetailContainer_Date_Checkin_Text = ele_DetailContainer_Date_Checkin.text
    print("by opening --->  ",ele_DetailContainer_Date_Checkin_Text)
    # time.sleep(2)        

    # Now getting CheckOut Date by Opening Container
    ele_DetailContainer_Date_Checkout = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[3]/div[1]/div/div[2]") # Detailed Container location Date Checkout by Opening
    ele_DetailContainer_Date_Checkout_Text = ele_DetailContainer_Date_Checkout.text
    print("by opening --->  ",ele_DetailContainer_Date_Checkout_Text)
    time.sleep(2)        
    # Now getting Guests by Opening Container
    ele_DetailContainer_Guest = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[1]/div/div[2]") # Detailed Container Guests element
    ele_DetailContainer_Guest_Text = ele_DetailContainer_Guest.text
    print("by opening --->  ",ele_DetailContainer_Guest_Text)
    time.sleep(1)
    ####################################### Getting Filters from Container by Opening code Ends ############################################################################################################################



def VerifyPropertiesCanAccommodateNumberOfGuests ():
    # driver = applyFiltersOnHomePage()
    
    driver = webdriver.Chrome('./webDrivers/chromedriver')
    driver.get("https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=filter_change&gps_lat=31.4573521&gps_lng=74.3000763")
    driver.maximize_window()
    time.sleep(3)
    ele_AllFilterDetailsWithPropertyCards = driver.find_element_by_xpath("//div[@class='_kqh46o' and @style='margin-top: 9px;']")

    print(len(ele_AllFilterDetailsWithPropertyCards))

    for x in ele_AllFilterDetailsWithPropertyCards:
        print(x.text , "\n")

    print("Asim ----> PASSED")

def VerifyDetailedPageMatchesExtraFilters ():
    # driver = applyFiltersOnHomePage()
    driver = webdriver.Chrome('./webDrivers/chromedriver')
    url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    driver.get(url1)
    driver.maximize_window()

    # Now clicking on option More Filters to open the more filters pop-up
    ele_MoreFilters = driver.find_element_by_xpath("//*[@id='menuItemButton-dynamicMoreFilters']/button") # More filters pop-op opening element
    ele_MoreFilters.click()
    time.sleep(1)

    # Now Locating Element to add number of beds
    ele_Bedrooms = driver.find_element_by_xpath("//*[@id='filterItem-rooms_and_beds-stepper-min_bedrooms-0']/button[2]") # Bedroom element on morefilter pop-up
        
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(0.5)
    ele_Bedrooms.click()
    time.sleep(2)

    # Now findind element Pool 
    ele_Pool = driver.find_element_by_xpath("//*[@id='filterItem-facilities-checkbox-amenities-7']") # pool element on more filters pop-up
    #Scrooling to pool item 
    ele_Pool.location_once_scrolled_into_view
    # ele_PoolValue = ele_Pool.get_attribute("value")
    # print(ele_PoolValue)
    ele_Pool.click()
    time.sleep(2)

    # Finding button Show Stays on more filters pop-up
    ele_ShowStays = driver.find_element_by_xpath("/html/body/div[11]/section/div/div/footer/button") # Button show stays button Element 
    ele_ShowStays.click()
    time.sleep(10)

    ###############  Starts -->  Trying to write Code to verify the "results matches atleat the filtered number of beds ################################## 

    # text = "8 guests . 3 bedrooms . 4 beds . 1 bath"
    # t = text
    # parts = t.split(" . ")
    # print(" ---->   ",parts[0])
    # print(" ---->   ",parts[1])
    # print(" ---->   ",parts[2])
    # print(" ---->   ",parts[3])

    # guestParts = parts[0]
    # gbedroomParts = parts[1]
    # bedParts = parts[2]
    #     # bathParts = parts[3]


    #     # print("\n\n -------========0000000-------------------\n\n") 
        
    # splitGuestNum = guestParts.split(" ")
    # print(splitGuestNum[0])

    # if int(splitGuestNum[0]) > 3 :
    # print("Guests are OKAAAYYYYYYYYYYYY")
    # else:
    # print("FFFFFAAAAAAAIIIIILLLLLLEEEEEEEDDDDDDDDD")

    # ele_OpenDetailOfProperty = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/a")
    # ele_OpenDetailOfProperty.click()


    ###############   END --> Trying to write Code to verify the "results matches atleat the filtered number of beds ##################################

    ############### Starts --> Opening detail of first property and verify pool is available on new page ###############################################
    window_before = driver.window_handles[0]

    # Opening detail of first property on new page
    ele_link = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/a")
    time.sleep(3)
    ele_link.click()
    window_after = driver.window_handles[1]
    time.sleep(3)
    # Navigates the driver to the new opened page
    driver.switch_to_window(window_after)
    time.sleep(3)
    # print(ele_link.get_attribute("href"))
    print(driver.current_url)
    time.sleep(2)

    # find element "Show all Aminites"
    ele_AllAminites = driver.find_element_by_xpath("//*[@id='site-content']/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div[3]/a") # button Show all aminites""
    ele_AllAminites.click()
    time.sleep(3)

    # Opeing The pop-up Amenites
    ele_PoolUnderFacilities = driver.find_element_by_xpath("/html/body/div[11]/section/div/div/div[3]/div/div/section/div[2]/div[3]/div[4]/div")
    # Getting text Pool on the Aminites pop-up
    ele_PoolUnderFacilitiesText = ele_PoolUnderFacilities.text
    print(" --->   ",ele_PoolUnderFacilitiesText)
    time.sleep(10)

    ############### Ends --> Opening detail of first property and verify pool is available on new page ###############################################

def test_VerifyPropertyDisplayedOnMapCorrectly ():
    # # driver = applyFiltersOnHomePage()
    # driver = webdriver.Chrome('./webDrivers/chromedriver')
    # url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-16&checkout=2021-01-23&adults=2&children=1&source=structured_search_input_header&search_type=unknown&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&map_toggle=true"
    # driver.get(url1)
    # driver.maximize_window()
    # time.sleep(5)
    # print("FINE ASIMMM")
    # ele_to_hover_over =driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]")
    # hover = ActionChains(driver).move_to_element(ele_to_hover_over)
    # hover.perform()

    ########################## Getting data to compare with the property on the map ############################
    driver = webdriver.Chrome('./webDrivers/chromedriver')
    url1 = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&checkin=2021-01-17&checkout=2021-01-24&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click&min_bedrooms=5&amenities%5B%5D=7&query=Rome%2C%20Italy"
    driver.get(url1)
    driver.maximize_window()
    time.sleep(5)


    ele_PropertyName = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div")
    propertyNameText = ele_PropertyName.text
    print(propertyNameText)

    ele_PropertyLocation = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]")
    propertyLocationText = ele_PropertyLocation.text
    print(propertyLocationText)

    ele_PropertyRating = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[5]/div[1]/span/span[2]")
    propertyRatingText = ele_PropertyRating.text
    print(propertyRatingText)

    ele_PropertyReviews = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[5]/div[1]/span/span[3]")
    propertyReviewsText = ele_PropertyReviews.text
    print(propertyReviewsText)

    ele_PropertyPrice = driver.find_element_by_xpath("//*[@id='ExploreLayoutController']/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[5]/div[2]/div/div[1]/span/span")
    propertyPriceText = ele_PropertyPrice.text
    print(propertyPriceText)
    ############################################################################################################ 
    print("\n ------------ \n Reached End of Page \n ---------------\n")
    time.sleep(100)
