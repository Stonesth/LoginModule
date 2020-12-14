from Tools import tools_v000 as tools
import os
import time
from os.path import dirname
from selenium.webdriver.common.keys import Keys
import keyboard


# -11 for the name of this project LoginModule
# save_path = dirname(__file__)[ : -11]
save_path = os.path.dirname(os.path.abspath("__file__"))[ : -11]
propertiesFolder_path = save_path + "\\"+ "Properties"



# url = 'http://sx-dll-wlsbt01:7104'
# url = 'http://sx-dll-wlsfou01:7004/'
url = 'http://sx-dll-wlsfop01:7004/'



# Example of used
# username = tools.readProperty(propertiesFolder_path, 'LoginModule_TST', 'username=')
# password = tools.readProperty(propertiesFolder_path, 'LoginModule_TST', 'password=')
# username = tools.readProperty(propertiesFolder_path, 'LoginModule_UAT-FO', 'username=')
# password = tools.readProperty(propertiesFolder_path, 'LoginModule_UAT-FO', 'password=')
username = tools.readProperty(propertiesFolder_path, 'LoginModule_PRD-FO', 'username=')
password = tools.readProperty(propertiesFolder_path, 'LoginModule_PRD-FO', 'password=')


def connectToLoginModuleTST() :
    tools.driver.get(url + '/loginmodule/')

def enterCredentials() :    
    
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.write(username)
    
    # tools.waitLoadingPageByXPATH('/html/body/div[9]/div/div/div[2]/form/div[1]/div[2]/input')
    # username = tools.driver.find_element_by_xpath("/html/body/div[9]/div/div/div[2]/form/div[1]/div[2]/input")
    # username.send_keys(username)

    keyboard.press_and_release('tab')
    keyboard.write(password)
    keyboard.press_and_release('enter')
    
    # tools.waitLoadingPageByXPATH('/html/body/div[9]/div/div/div[2]/form/div[2]/div[2]/input')
    # password = tools.driver.find_element_by_xpath("/html/body/div[9]/div/div/div[2]/form/div[2]/div[2]/input")
    # password.send_keys(password)
    # password.send_keys(Keys.ENTER)

def createContact(DSCLOGIN_value, DSCCOMPLETENAME_value, DSCNAME_value, DSCFIRSTNAME_value, EMAIL_value) :
    tools.waitLoadingPageByID('mid-col-2')
    tools.driver.get(url + '/loginmodule/CreateLDAPUser.do')

    DSCLOGIN = tools.driver.find_element_by_id("DSCLOGIN")
    DSCLOGIN.send_keys(DSCLOGIN_value)

    DSCCOMPLETENAME = tools.driver.find_element_by_id("DSCCOMPLETENAME")
    DSCCOMPLETENAME.send_keys(DSCCOMPLETENAME_value)

    DSCNAME = tools.driver.find_element_by_id("DSCNAME")
    DSCNAME.send_keys(DSCNAME_value)

    DSCFIRSTNAME = tools.driver.find_element_by_id("DSCFIRSTNAME")
    DSCFIRSTNAME.send_keys(DSCFIRSTNAME_value)

    EMAIL = tools.driver.find_element_by_id("EMAIL")
    EMAIL.send_keys(EMAIL_value)
    EMAIL.send_keys(Keys.ENTER)

def linBindaToThisUser(DSCLOGIN_value):
    tools.waitLoadingPageByID('mid-col-2')
    tools.driver.get(url + '/loginmodule/AddGroupToUser.do?DSCLOGIN='+DSCLOGIN_value)

    tools.waitLoadingPageByID('listeAll')
    listeAll = tools.driver.find_element_by_id("listeAll")
    listeAll.click()

    # select binda
    # listeAll = tools.driver.find_element_by_xpath('//*[@id="listeAll"]/option[20]') # TST only
    listeAll = tools.driver.find_element_by_xpath('//select[@id="listeAll"]/option[text()="binda"]')
    listeAll.click()
    
    # Validate
    validate_button = tools.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[2]/form/div[3]/input')
    validate_button.click()

def selectBindaProfil(DSCLOGIN_value, langage_value) :
    tools.waitLoadingPageByID('mid-col-2')
    tools.driver.get(url + '/loginmodule/ModifyBindaUser.do?DSCLOGIN='+DSCLOGIN_value)
    tools.waitLoadingPageByID('mid-col-2')

    # Language
    if langage_value == 'fr' :
        dist_radio_button = tools.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[3]/form/div[8]/select/option[2]')
        dist_radio_button.click()
    else :
        dist_radio_button = tools.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[3]/form/div[8]/select/option[1]')
        dist_radio_button.click()
    
    # Choose the courtier (DIST) Profile 
    dist_radio_button = tools.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[3]/form/table/tbody/tr[5]/td[2]/input')
    dist_radio_button.click()

    # Validate
    validate_button = tools.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[3]/form/div[16]/div[2]/input')
    validate_button.click()

def modifyEmail(DSCLOGIN_value, EMAIL_value):
    tools.waitLoadingPageByID('mid-col-2')
    tools.driver.get(url + '/loginmodule/ModifyLDAPUser.do')

    EMAIL = tools.driver.find_element_by_id("EMAIL")
    EMAIL.clear()
    EMAIL.send_keys(EMAIL_value)
    EMAIL.send_keys(Keys.ENTER)
    

def createAll(DSCLOGIN_value, DSCCOMPLETENAME_value, LANGAGE_value, DSCFIRSTNAME_value, DSCNAME_value, EMAIL_value ) :
    createContact(DSCLOGIN_value, DSCCOMPLETENAME_value, DSCNAME_value, DSCFIRSTNAME_value, 'pierre.thonon@nn.be' )
    linBindaToThisUser(DSCLOGIN_value)
    selectBindaProfil(DSCLOGIN_value, LANGAGE_value)
    modifyEmail(DSCLOGIN_value, EMAIL_value)

tools.openBrowserChrome() 
connectToLoginModuleTST()
enterCredentials()

createAll('0030X00002W7icNQAR', 'Antoni Halpouter', 'fr', 'Antoni', 'Halpouter', 'info@antonihalpouter.be')
createAll('0030X00002W7icOQAR', 'Bénédicte Halpouter', 'fr', 'Bénédicte', 'Halpouter', 'benedicte@halpouter.com')
createAll('0030X00002W7ivjQAB', 'Marie-Laure Marchet', 'fr', 'Marie-Laure', 'Marchet', 'mlmarchet@brservice.be')
createAll('0030X00002W7jhGQAR', 'Christine Van den Boeynants', 'nl', 'Christine', 'Van den Boeynants', 'chrisina.vdb@hotmail.com')
createAll('0030X00002W7jhHQAR', 'Christina Vanden Baeymans', 'nl', 'Christina', 'Vanden Baeymans', 'christina.vandenbaeymans@hotmail.com')
createAll('0030X00002W7ju1QAB', 'Ronald Bogaerts', 'nl', 'Ronald', 'Bogaerts', 'ronald.bogaerts@hotmail.com')
createAll('0030X00002W7ju2QAB', 'Noura Atmani', 'nl', 'Noura', 'Atmani', 'noura196@yahoo.com')
createAll('0030X00002W7juXQAR', 'Tony Stevens', 'nl', 'Tony', 'Stevens', 'tonystevens@daelemans.be')
createAll('0030X00002W7k5lQAB', 'Degauquier & Partners', 'fr', 'Degauquier', '& Partners', 'degauquier@skynet.be')
createAll('0030X00002W7kV8QAJ', 'Charles Gersdorff', 'fr', 'Charles', 'Gersdorff', 'charles.gersdorff@excelandco.be')
createAll('0030X00002W7koMQAR', 'Zakenkantoor Geers B.V.B.A.', 'nl', 'Zakenkantoor', 'Geers B.V.B.A.', 'zakenkantoor.geers@advalvas.be')
createAll('0030X00002W7kowQAB', 'Gestion, Assurances Et Prets (G.A.P.) S.P.R.L.', 'fr', 'Gestion, Assurances Et Prets (G.A.P.)', 'S.P.R.L.', 'eyup.salar@gapcorp.be')
createAll('0030X00002W7kp3QAB', 'Katty Wilmot', 'fr', 'Katty', 'Wilmot', 'info@greenfoxadvice.be')
createAll('0030X00002W7kp6QAB', 'Christian Hardy', 'fr', 'Christian', 'Hardy', 'christian.hardy@outlook.be')
createAll('0030X00002W7ktXQAR', 'Hilde De Maeyer', 'nl', 'Hilde', 'De Maeyer', 'hilde.demaeyer@fintro.be')
createAll('0030X00002W7ktZQAR', 'Nancy De Maeyer', 'nl', 'Nancy', 'De Maeyer', 'nancy.demaeyer@fintro.be')
createAll('0030X00002W7l1rQAB', 'De zaakvoerder', 'nl', 'De', 'zaakvoerder', 'verzekeringen@haskrediet.be')
createAll('0030X00002W7l5QQAR', 'Jean-Marc Hallet', 'fr', 'Jean-Marc', 'Hallet', 'jean-marc@hdassurances.be')
createAll('0030X00002W7lEDQAZ', 'Wendy Van Asbroeck', 'nl', 'Wendy', 'Van Asbroeck', 'w.vanasbroeck@icci.insure')
createAll('0030X00002W7lEEQAZ', 'Dirk Ruysbergh', 'nl', 'Dirk', 'Ruysbergh', 'd.ruysbergh@icci.insure')
createAll('0030X00002W7lHiQAJ', 'Stefaan Vetters', 'nl', 'Stefaan', 'Vetters', 'stefaan@jurimmo.be')
createAll('0030X00002W7lOuQAJ', 'Kristof Bogaert', 'nl', 'Kristof', 'Bogaert', 'kb@infinia.org')
createAll('0030X00002W7lQVQAZ', 'de zaakvoerder', 'nl', 'de', 'zaakvoerder', 'info@itarget.be')
createAll('0030X00002W7llEQAR', 'Frank Volcke', 'nl', 'Frank', 'Volcke', 'frank@kantoorvolckekoekelare.be')
createAll('0030X00002W7lmWQAR', 'Michel De Norman', 'fr', 'Michel', 'De Norman', 'm.denorman@worldonline.be')
createAll('0030X00002W7lsOQAR', 'Jacques Emmanuel Pinte', 'fr', 'Jacques Emmanuel', 'Pinte', 'ldb.jep@gmail.com')
createAll('0030X00002W7ltZQAR', 'Philippe De Jaeger', 'fr', 'Philippe', 'De Jaeger', 'p.dejaeger@lifeandfinance.be')
createAll('0030X00002W7lzgQAB', 'Joachim Vonck', 'nl', 'Joachim', 'Vonck', 'joachim@luxassur.be')
createAll('0030X00002W7mA3QAJ', 'Baudouin Poncelet', 'fr', 'Baudouin', 'Poncelet', 'baudouin.poncelet@maxel.be')
createAll('0030X00002W7mACQAZ', 'Laurence Nève de Mévergnuies', 'fr', 'Laurence', 'Nève de Mévergnuies', 'laurence.neve@maxel.be')
createAll('0030X00002W7mADQAZ', 'Alexandra Staquet', 'fr', 'Alexandra', 'Staquet', 'alexandra.staquet@maxel.be')
createAll('0030X00002W7mAEQAZ', 'Karin Thibaut', 'fr', 'Karin', 'Thibaut', 'karin.thibaut@maxel.be')
createAll('0030X00002W7mAFQAZ', 'Barbara Patigny', 'fr', 'Barbara', 'Patigny', 'barbara.patigny@maxel.be')
createAll('0030X00002W7mAGQAZ', 'Stéphanie De Busscher', 'fr', 'Stéphanie', 'De Busscher', 'stephanie.debusscher@maxel.be')
createAll('0030X00002W7mAIQAZ', 'Graziella Malou', 'fr', 'Graziella', 'Malou', 'graziella.malou@realstoneinvest.be')
createAll('0030X00002W7mMeQAJ', 'Thomas Rondoz', 'fr', 'Thomas', 'Rondoz', 'thomas@newserve.be')
createAll('0030X00002W7mrwQAB', 'Roland Dumortier', 'nl', 'Roland', 'Dumortier', 'r.quidum@hotmail.vom')
createAll('0030X00002W7mwzQAB', 'Annick Perée', 'fr', 'Annick', 'Perée', 'annick.peree@rgf.be')
createAll('0030X00002W7n5LQAR', 'Pieter Schrooyen', 'nl', 'Pieter', 'Schrooyen', 'pieter@groepsds.be')
createAll('0030X00002W7n9OQAR', 'Kristel Philippart', 'fr', 'Kristel', 'Philippart', 'kristel.philippart@sls-bsa.be')
createAll('0030X00002W7n9PQAR', 'Florence Depriester', 'fr', 'Florence', 'Depriester', 'florence.depriester@sls-bsa.be')
createAll('0030X00002W7nBWQAZ', 'César Colmant', 'fr', 'César', 'Colmant', 'cesar.colmant@soyermamet.be')
createAll('0030X00002W7nSqQAJ', 'Anne Van melkebeke', 'fr', 'Anne', 'Van melkebeke', 'a.vanmelkebeke@portima.be')
createAll('0030X00002W7nqEQAR', 'Myriam Mulliez', 'nl', 'Myriam', 'Mulliez', 'myriam@hypotheekservice.be')
createAll('0030X00002W7nxsQAB', 'Benendikte Vandewaetere', 'fr', 'Benendikte', 'Vandewaetere', 'benedikte@kantoorverstraete.be')
createAll('0030X00002W7o21QAB', 'Guy Ramackers', 'fr', 'Guy', 'Ramackers', 'guy.ramackers@wavrefinance.be')
createAll('0030X00002W7o23QAB', 'Pierre Van Lancker', 'fr', 'Pierre', 'Van Lancker', 'pierre.vanlancker.12774@axa-bank.be')
createAll('0030X00002W7o3HQAR', 'Els Berghmans', 'nl', 'Els', 'Berghmans', 'eberghmans@finb.be')
createAll('0030X00002W7oM7QAJ', 'Erwin Viaene', 'nl', 'Erwin', 'Viaene', 'erwin@zev.be')
createAll('0030X00002W7oM8QAJ', 'Ludwig De Caluwe', 'nl', 'Ludwig', 'De Caluwe', 'zakenkantoor.viaene@scarlet.be')
createAll('0030X00002W7oMVQAZ', 'Staf Huys', 'nl', 'Staf', 'Huys', 'staf.huys@nvgoris.be')
createAll('0030X00002W7qeaQAB', 'Stefan Decraene', 'fr', 'Stefan', 'Decraene', 'stefan.decraene@vdl-interass.be')
createAll('0030X00002Zwc5fQAB', 'Jeroen Schepens', 'nl', 'Jeroen', 'Schepens', 'js@vdl-interass.be')
createAll('0030X00002uoalXQAQ', 'Liesbeth Peeraer', 'nl', 'Liesbeth', 'Peeraer', 'liesbeth.peeraer@partner.wilink.be')
createAll('0030X00002uoam6QAA', 'Kelly Kiekens', 'nl', 'Kelly', 'Kiekens', 'kelly.kiekens@partner.wilink.be')
createAll('0030X00002uobtXQAQ', 'Geert Van Laecke', 'nl', 'Geert', 'Van Laecke', 'geert.van.laecke@telenet.be')
createAll('0030X00002uooOEQAY', 'Iwona Pruszynska', 'fr', 'Iwona', 'Pruszynska', 'iwona.pruszynska@incoinsurance.be')
createAll('0030X00002vecojQAA', 'FABRIZIO Mammo', 'fr', 'FABRIZIO', 'Mammo', 'mammoetfils@gmail.com')

