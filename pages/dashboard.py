from pages.base_page import BasePage


class Dashboard(BasePage):
    mainPage_xpath = "//*[text() = 'Main page']"
    players_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span'
    addPlayerButton_xpath = "//*[@href =  '/en/players/add']"
    scoutsPanelImg_xpath = "//*[contains(@style, 'image')]"
    devTeamButton_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]'
    signOutButton_xpath = "//*[text() = 'Sign out']"
    lastCreatedPlayerButton_xpath = "//*[@href = '/en/players/62f02fa32d2b7461da157b0f/edit']"
    reportsCount_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[3]/div'
    matchesCount_xpath = "//*[text() ='Matches count']"
    playersCount_xpath = "//*[contains(text(),'Players c')]/parent::div"
    eventsCount_xpath = "//*[text() ='Events count']"





