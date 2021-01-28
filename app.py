#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, flash, redirect, render_template, \
     request, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.color import Color
import time


chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')

chrome_options.add_argument("--no-sandbox"); 
chrome_options.add_argument("--disable-dev-shm-usage"); 
chrome_options.add_argument("--aggressive-cache-discard"); 
chrome_options.add_argument("--disable-cache"); 
chrome_options.add_argument("--disable-application-cache"); 
chrome_options.add_argument("--disable-offline-load-stale-cache"); 
chrome_options.add_argument("--disk-cache-size=0");
chrome_options.add_argument("--headless"); 
chrome_options.add_argument("--disable-gpu"); 
chrome_options.add_argument("--dns-prefetch-disable"); 
chrome_options.add_argument("--no-proxy-server"); 
chrome_options.add_argument("--log-level=3");
chrome_options.add_argument("--silent");
chrome_options.add_argument("--disable-browser-side-navigation");
chrome_options.add_argument('--ignore-certificate-errors')


chrome_options.add_argument('user-agent=[user-agent string]') # es ar wavSalo



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           data=[{'name':'Cosco'}, {'name':'Cma-Cgm'}, {'name':'zim'}, {'name':'MSC'}, {'name':'Hapag-Lloyd'}, {'name':'Turkon'}, {'name':'Maersk'}, {'name':'Oocl'}, {'name':'All Trackers'}])

@app.route("/", methods=["GET","POST"])
def getvalue():
    name = request.form["name"]
    age = request.form["age"]
    db = request.form["email"]
    select = request.form.get('comp_select')
    
    choose = select
    
    time.sleep(5)
    driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
    
    
   
                
                
    if choose == 'Cosco':            
        try:
            driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
            driver.get("https://elines.coscoshipping.com/ebusiness/cargoTracking?trackingType=CONTAINER&number="+name+"")
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[3]/div/button').click()
            coslocation = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div[3]/div/div[3]/p[2]').text
            cosdate = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div[3]/div/div[1]').text
            cosdesc = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div[3]/div/div[2]/p[2]').text
           
            
            driver.quit()
            return render_template("cosco_container.html", loc=coslocation, date=cosdate, desc=cosdesc,  lastplace="Last Place")
        
        
        except Exception as e:
                driver.quit()
                time.sleep(3)
                
        
        try:
            driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
            driver.get("https://elines.coscoshipping.com/ebusiness/cargoTracking")
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[3]/div/button').click()# PopUp Clicck
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[1]/div/div[1]/div/div/div[1]/span[2]').click()
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[1]/div/div[1]/div/div/div[2]/ul[2]/div/li[2]').click()
            driver.find_element_by_xpath('//*[@id="wrap"]/input').send_keys(name)
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[1]/div/div[2]/form/div/div[2]/button').click()
            time.sleep(10)
            cosbookarrdate = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[5]/div[3]/div[2]/div/div[3]').text
            cosbooklocation = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/p').text
            cosbooklast = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[4]/p').text
            cosbookdesc = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/p').text
            
            
            por = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div[2]")
            desired_y = (por.size['height'] / 2) + por.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            port = por.text
                        
            first_pol = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[2]")
            desired_y = (first_pol.size['height'] / 2) + first_pol.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            fpol = first_pol.text
                        
            t_s_port = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div[3]/div[2]/div/div')
            desired_y = (t_s_port.size['height'] / 2) + t_s_port.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            tsport = t_s_port.text
                        
            #t_s_port2 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[4]/div[3]/div[2]/div/div')
            #desired_y = (t_s_port2.size['height'] / 2) + t_s_port2.location['y']
            #current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            #scroll_y_by = desired_y - current_y
            #driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            #tsport2 = t_s_port2.text
                        
            last_pod = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[4]/div[3]/div[2]/div')
            desired_y = (last_pod.size['height'] / 2) + last_pod.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            lpod = last_pod.text
                        
            fnd = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[4]/p')
            desired_y = (fnd.size['height'] / 2) + fnd.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            final = fnd.text
            
            eta = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[4]/div[4]/p')
            desired_y = (fnd.size['height'] / 2) + fnd.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            etat = eta.text
            
            # forma Cosco-stvis
            booknumb = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/p')
            desired_y = (booknumb.size['height'] / 2) + booknumb.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            bnum = booknumb.text
            
            placeofreciept = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/p')
            desired_y = (placeofreciept.size['height'] / 2) + placeofreciept.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            pori = placeofreciept.text
            
            pol = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/p')
            desired_y = (pol.size['height'] / 2) + pol.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            poli = pol.text
            
            vesel = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[4]/div[2]/p')
            desired_y = (vesel.size['height'] / 2) + vesel.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            veselo = vesel.text
            
            cargocutof = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[5]/div[2]/p')
            desired_y = (cargocutof.size['height'] / 2) + cargocutof.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            cutof = cargocutof.text
            
            vgm = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[6]/div[2]/p')
            desired_y = (vgm.size['height'] / 2) + vgm.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            vgmo = vgm.text
            
            shipinstruct = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[7]/div[2]/p')
            desired_y = (shipinstruct.size['height'] / 2) + shipinstruct.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            shipinst = shipinstruct.text
            
            billofland = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[4]/p')
            desired_y = (billofland.size['height'] / 2) + billofland.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            bill = billofland.text
            
            findest = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[4]/p')
            desired_y = (findest.size['height'] / 2) + findest.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            finaldest = findest.text
            
            pod = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[3]/div[4]/p')
            desired_y = (pod.size['height'] / 2) + pod.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            podo = pod.text
            
            etadelivery = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[4]/div[4]/p')
            desired_y = (etadelivery.size['height'] / 2) + etadelivery.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            etadel = etadelivery.text
            
            etarecdate = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[5]/div[2]/p')
            desired_y = (etarecdate.size['height'] / 2) + etarecdate.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            etadate = etarecdate.text
            
            containerquantity = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[6]/div[4]/p')
            desired_y = (containerquantity.size['height'] / 2) + containerquantity.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            contquant = containerquantity.text
            
            
            ship_vessel = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/a')
            desired_y = (ship_vessel.size['height'] / 2) + ship_vessel.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            shipvessel = ship_vessel.text
            
            
            cosco = driver.title
            
            
            
            
            blue = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABGdBTUEAALGPC/xhBQAAAn5JREFUOBHNVMtqFEEUPbe6e9IzSQSjiIv4wiwEQdfqSnzgRjIGjeIrxkVCXEQhLmRW+YLRBIMQFIMggpEIKiii+MKFG79AXSTZZBHnZSaZR1d5OpmZTsaZIUsvVNetc+49XXVvVwP/u0nDDRoj6J1ogmdZ2L0th+HDxUr8pUfN0EkLjwfTFYxObcGyUCoxAI0+xtmM/Aqn6Ra2egnMmnPQeojYR2yJDGG8v1AWtcsOuu7ugOUksbcvg67R4zB6BEZ9R8HuRFg3w3jHkM9/wbR4FPoJ2+7GptA0Eht1RYNOsMNofAxQJyj0CoVQHOGIBZ3ugcFFiPmGqRsX0D8exkzOhuu4MLnbgHHJCUTfwdTNz75wsEOnfRC5TAQqPQSn8AI6ZZF/B3EPYP+e3xAxXGf9JJy6R0F9ftn3UWW/5rNKcLLbI5jhGC4NTiV7XnZKs6t0SbqK8HfYOXYQyB39h6kFiAj0hjgQNLs6TEHlohC1j9KLDYfIEpNZz9TOapHVaxtKNIoyB08GVwj1lPU5zXYpFv09m3KI9WPN8IvIHOeGVm5KK4xpX4n0dnHeXkrsoN9BjpM4fPyAWCEsab5slSlj48pD178ANjwsse2LpPNM4ieAeWhDTCyKzhNPEwvDCHFN3DwBFv0GBuYhhmTyGk+UEETjEwzeTHZtUBAeeMJdGs1iLH9CAV7x1DyvlCR5pJ4K1shZPjoDdJ1CKjOqUOyIQakPjXTWxYl8wkJbTOHlySzE7mWdZtaVWCtIZBZOSy/eXl5YdZdHjrCoz3iello5dTHDOxOyzmLy+hs/JhD0V2futyGULSJvrfmD+FRda3UFD67+YS/qFLZu5vqIvyHE1b6bs+QNAAAAAElFTkSuQmCC"
            yelow = '"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABGdBTUEAALGPC/xhBQAAAqJJREFUOBHNVM1LVFEUP+e+93zvjR+UBG0yUyYwAiFwU0EkfRAtrEWZqOQuqIWb2YSr/gL7gPatEpxoEUoFhVPSooUtWiWNBuUiI79GnXlv3r33dO7oG9HUnF0HLufec3/n937v3HMvwP9uuJtAIkLItLtQnLegqj7E9oyM8fS6tRpU3sLL2VwcM35bwpgo/DlzW5O+BYg2Az94deouoL0QLIouLVTKAsi4yX0pbJuIYlI7ntDosUZYDRfh+s1lmW65GCn1EJA++S5ciTRWyyJeKORgnGOKQE0lbKsT3NrvMN2sASZimg2F+afJxwB0SVhixJVyEA46VvG37lOaehHho9eV7YGRNh+WlmxIkFcI8T6Te6QBq0g8cHq+vjesZYW+faIf3M+JIK9SeSFe0C9lCRBvfI9Owv6GeUQkxudNEj1v9YhWu8FEzNrWL9ltJsTOtOLgMo9764NdbFPxZM07gYZgcyhe2VG65ZSM5Pk4sJvXqDGRcAZZ044woZS6SgJaCbDwjxEIwF4I8ciObLxhayItUMxq0P0GKACGNdI1IBQE9JZrd5oFebw1zbpmDWY3Kx0Kgq7l5EMGqFA0AdFh81t8uknuyWSJAMHhXsxyw1U5kcffXS3zRoQ2jZ31zAXghhWBVlRAAUXDQajn+Dy55Gjxeo6zckzkk5kLCqSKhqSU5gA3TNNAMPvjDpFYwHDo6BNNcIAVbgZtwMszVuyweq4Cf2obQ8A5m9t+kUD3bbP/V4hVrlnstyAsxEfCr60bEALGtuxVvOSivnMjf6D0ONBoU2MhJ8ZZQUPFTJzAJZjxq+0z2DH5rURoSArp5nMUiWd8u2sqIeXa54nsGzXdk69MXpnQLGj4eD3UhBJWXH5B9miuROj4srJ+1/eYVAHsD5ZzIzYvxuKlAAAAAElFTkSuQmCC"'
            wd = ""

            tscolor1 =  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/span"))).value_of_css_property("background-image")
            tscolor2 =  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div/span"))).value_of_css_property("background-image")
            #print(re.split('[()]',tscolor)[1])

            qq = re.split('[()]',tscolor1)[1]
            gg = re.split('[()]',tscolor2)[1]
            
            if qq == yelow:
                wd = 27
            elif gg == yelow:
                wd = 65
            else:
                wd = 85        

            
                
                
            
            
            
            
            driver.quit()
            return render_template("cosco_booking.html", loc=cosbooklocation, date=cosbookarrdate, desc=tsport,  last=cosbooklast, por = port, first_pol=fpol, t_s_port=tsport,  last_pod=lpod, fnd=final, wido = wd, etatime = etat, bnumi = bnum, porii = pori, polii = poli, veseloi = veselo, cutofi = cutof, vgmoi= vgmo, shipinsti = shipinst, billi = bill, finaldesti = finaldest, podoi = podo, etadeli = etadel, etadatei = etadate, contquanti = contquant, vessel = shipvessel, titlei = cosco ) #t_s_port2=tsport2,
        
        except Exception as e:
                    driver.quit()
                    time.sleep(3)        
                    return render_template("pass.html")
            
    if choose == 'Turkon':
        try:
            driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
            
            driver.get('https://turkon.com/en/Container-Tracking.aspx')
            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_f_con"]').send_keys(name)# PopUp Clicck
            driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Button1"]').click()
            
            container_nom = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_con_mov"]/tr[1]/td[1]'))).text
            voyage = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[1]'))).text
            vessel = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[2]'))).text
            pol = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[3]'))).text
            transshipment = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[4]'))).text
            pod = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[5]'))).text
            departed_on = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[6]'))).text
            #transshipment_eta = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[7]'))).text
            pod_eta = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[7]'))).text
            
            
            
            rcvd_full = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_progress"]/div[2]/p[1]').text
            sailed = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_progress"]/div[3]/p[1]').text
            transit_loaded  = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_progress"]/div[4]/p[1]').text
            
            
            
            blue4 = '"https://turkon.com/images/icons/4.png"'
            blue8 = '"https://turkon.com/images/icons/8.png"'
            image4 =  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_progress"]/div[3]/li'))).value_of_css_property("background-image")
            image8 =  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_progress"]/div[4]/li'))).value_of_css_property("background-image")
            
            ti = ""
            img4 = re.split('[()]',image4)[1]
            img8 = re.split('[()]',image8)[1]
            
            if img4 == blue4:
                ti = 31.2
            if img8 == blue8:
                ti = 48.8
            
            
            
            
            title = driver.title       
            driver.quit()
            return render_template("turkon_booking.html", container = container_nom, voyg = voyage, veso = vessel, poli = pol, tr = transshipment, podi = pod, depon = departed_on, podeta = pod_eta, titlei = title, tim = ti, rfull = rcvd_full, sail = sailed, tloaded = transit_loaded )  # treta =  transshipment_eta, 
        
        except Exception as e:
                    driver.quit()
                    time.sleep(3)        
                    return render_template("pass.html")
                
   
    if choose == 'Hapag-Lloyd' :
        try:
            driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
            driver.get('https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html')
            time.sleep(5)

            
        
            #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_f_con"]'))).send_keys(name)
            
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="onetrust-pc-sdk"]/div[3]/div[1]/button[1]'))).click() #popup
            driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl12"]').clear() # INPUT gasufTaveba
            driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl12"]').send_keys(name)
            driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl25"]').click()
            
            typec = driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl29"]/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span').text  
            description = driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl29"]/tbody/tr/td/div/table/tbody/tr/td[3]/table/tbody/tr/td[2]/span').text
            dimension =  driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl29"]/tbody/tr/td/div/table/tbody/tr/td[5]/table/tbody/tr/td[2]/span').text
            tare =  driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl29"]/tbody/tr/td/div/table/tbody/tr/td[7]/table/tbody/tr/td[2]/span').text
            maxpayload =  driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl29"]/tbody/tr/td/div/table/tbody/tr/td[9]/table/tbody/tr/td[2]/span').text
            lastmovement =  driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl56"]/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span').text
            
            firstport = driver.find_element_by_xpath('//*[@id="tracing_by_container_f:hl66"]/tbody/tr[1]/td[2]/span').text
            
            #eta =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[7]').text
            
            
                        
            title = driver.title 
            return render_template('hl_container.html', a=typec, b=description, c=dimension , d=tare , e =maxpayload ,f =lastmovement, titlei = title, fport = firstport)
            driver.quit()

        except Exception as e:
                            
            driver.quit()
            time.sleep(3)
                        
            driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
            driver.get('https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html')
            time.sleep(3)
            
            driver.find_element_by_xpath('//*[@id="onetrust-pc-sdk"]/div[3]/div[1]/button[1]').click()
            driver.find_element_by_xpath('//*[@id="contentOlb"]/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="tracing_by_booking_f:hl12"]').send_keys(name)
            driver.find_element_by_xpath('//*[@id="tracing_by_booking_f:hl18"]').click()
            
            typebc = driver.find_element_by_xpath('//*[@id="tracing_by_booking_f:hl27"]/tbody/tr[1]/td[2]/span').text
            container_no = driver.find_element_by_xpath('//*[@id="tracing_by_booking_f:hl27"]/tbody/tr[1]/td[3]/span').text
            status = driver.find_element_by_xpath('//*[@id="tracing_by_booking_f:hl27"]/tbody/tr[1]/td[4]/span').text
            date = driver.find_element_by_xpath('//*[@id="tracing_by_booking_f:hl27"]/tbody/tr[1]/td[5]/span').text
            place_of_activity = driver.find_element_by_xpath('//*[@id="tracing_by_booking_f:hl27"]/tbody/tr[1]/td[6]/span').text

            return render_template('pass.html', a=typebc, b=container_no, c=status , d=date , e = place_of_activity )
    
    
    
        
        
       
    
    
    if choose == 'Maersk' :
        try:
            driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
            driver.get('https://www.maersk.com/')
            time.sleep(5)

            
            try:
                driver.find_element_by_xpath('//*[@id="coiPage-1"]/div[2]/button[2]').click()
            except:
                pass    
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="tracking-number_903edf5561964e07ad9e40efbdb7c502"]').send_keys(name)
            driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/div[2]/div[1]/form/div[2]/button').click()           
            
            #husto = driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div/div[1]/dl[1]/dd').text
            
            husto = driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div/div[1]/dl[1]/dd')
            desired_y = (husto.size['height'] / 2) + husto.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            fromw = husto.text
            
            poto = driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div/div[1]/dl[2]/dd')
            desired_y = (poto.size['height'] / 2) + poto.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            towere = poto.text
            
            conto = driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div/div[1]/dl[3]/dd')
            desired_y = (conto.size['height'] / 2) + conto.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            contom = conto.text
            
            
            conttypes = driver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr/td[2]/span[4]')
            desired_y = (conttypes.size['height'] / 2) + conttypes.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            containertype = conttypes.text
            
            esdate = driver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr/td[3]/span[4]')
            desired_y = (esdate.size['height'] / 2) + esdate.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            estimatedate = esdate.text
            
            lallca = driver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr/td[4]/span[4]')
            desired_y = (lallca.size['height'] / 2) + lallca.location['y']
            current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script('return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            lastlocation = lallca.text
            
            
            
            
            title = driver.title 
            driver.quit()
            return render_template('maersk.html', a=title,  b = fromw, c=towere, d=contom , e =containertype ,f =estimatedate, gg = lastlocation, )

        except Exception as e:       
            
            time.sleep(3)
                        
            
            return render_template('pass.html',) #a=typebc, b=container_no, c=status , d=date , e = place_of_activity )
        
        
    if choose == 'Cma-Cgm' :
        driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
        driver.get('https://www.cma-cgm.com/ebusiness/tracking')

        driver.find_element_by_xpath('//*[@id="acceptAll"]').click() # accept cookies
        
        driver.find_element_by_xpath('//*[@id="Reference"]').send_keys(name) #Search velSi monacemis Cawera
        driver.find_element_by_xpath('//*[@id="btnTracking"]').click() # search button click
        
        time.sleep(5)
        container = driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[1]/div/h1/span/span/span').text
        pol = driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[2]/div[2]/div[1]/div/table/tbody/tr[1]/td[4]').text #port of load
        vessel = driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[2]/div[2]/div[1]/div/table/tbody/tr[last()]/td[5]').text #last vessel-i
        
        last_date = driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[2]/div[2]/div[1]/div/table/tbody/tr[last()]/td[1]').text # date bolo elementi cxrilSi
        last_move = driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[2]/div[2]/div[1]/div/table/tbody/tr[last()]/td[3]').text # MOVE bolo elementi cxrilSi
        last_location = driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[2]/div[2]/div[1]/div/table/tbody/tr[last()]/td[4]').text # Last location bolo elementi cxrilSi
            
        title = driver.title       
        driver.quit()
                
        return render_template("sma_cgm.html", a = title, b = container, c = pol, d = vessel, e = last_date, f = last_move, gg = last_location) #pol = port_of_load, veselo = vessel, depdate = departure_date, pod = port_of_discharge, trship = transshipment, pcd = price_calculation_date,  titlei = title)
    
        
        
    if choose == 'MSC':
        driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
        driver.get('https://www.msc.com/track-a-shipment?agencyPath=mwi')
       
        driver.quit()
        return render_template("pass.html")
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
