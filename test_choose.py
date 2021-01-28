#tscolor =  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div/div[2]"))).text   monacemebis wamoReba ScrolliT

# -*- coding: utf-8 -*-
from selenium import webdriver
import re
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_path = r"C:\Users\User\Downloads\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

name = "TRKU4419696"



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
transshipment_eta = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[7]'))).text
#pod_eta = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[8]'))).text
            
#//*[@id="ContentPlaceHolder1_cargo_body"]/tr/td[7]


print([container_nom,  voyage, vessel, pol, transshipment, pod,  departed_on, transshipment_eta,  ])











