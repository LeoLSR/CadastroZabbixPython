from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


ip = '192.168.99.59'
usuario = 'Admin'
senha = 'zabbix'

def verificar():
    if valor == 1:
        inserir()
        
    if valor == 2:
        conferir()

    
        
def conferir():

    driver = webdriver.Chrome()
    driver.get(f"http://{ip}/")
    driver.find_element(By.XPATH,'/html/body/div/main/div[2]/form/ul/li[1]/input').send_keys(usuario)
    driver.find_element(By.XPATH,'/html/body/div/main/div[2]/form/ul/li[2]/input').send_keys(senha,Keys.ENTER)
    driver.get(f'http://{ip}/zabbix/zabbix.php?action=host.list')
    with open('conferir.txt','r') as arquivo:
        for linha in arquivo:
            site = linha.split(',')[0]
            time.sleep(4)
            driver.find_element(By.XPATH,'/html/body/div/main/div[1]/form/div/div[1]/div/div[1]/div/div[3]/input').send_keys(Keys.CONTROL,"a")
            driver.find_element(By.XPATH,'/html/body/div/main/div[1]/form/div/div[1]/div/div[1]/div/div[3]/input').send_keys(site,Keys.ENTER)
            time.sleep(2)

def inserir():


    tipo = int(input('Quais opções você deseja: ( 1 - Adicionar grupo de hosts  2 - Adicionar Hosts):  '))

    driver = webdriver.Chrome()
    driver.get(f"http://{ip}/")
    #--------AUTENTICAR ------------#
    driver.find_element(By.XPATH,'/html/body/div/main/div[2]/form/ul/li[1]/input').send_keys(usuario)
    driver.find_element(By.XPATH,'/html/body/div/main/div[2]/form/ul/li[2]/input').send_keys(senha,Keys.ENTER)
    #--------------------------------


    if tipo == 1: #Adicionado ao grupo de hosts

        driver.get(f'http://{ip}/zabbix.php?action=hostgroup.list')
        driver.find_element(By.XPATH, '/html/body/div/header/div[3]/nav/ul/li/button').click()

        with open('grupodehosts.txt', 'r') as arquivo:
            for linha in arquivo:
                try:
                    grupo_hosts = linha.split(',')[0]
                    time.sleep(1)
                    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div/div/div/div/input').send_keys(grupo_hosts,Keys.ENTER)
                    time.sleep(2)
                    driver.find_element(By.XPATH, '/html/body/div/header/div[3]/nav/ul/li/button').click()
                    time.sleep(2)
                except:
                    print(f'O {grupo_hosts} já está cadastrado')
                    driver.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/button[2]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '/html/body/div/header/div[3]/nav/ul/li/button').click()





valor = int(input(f'  O que você deseja?( 1 - Inserir ou 2 - Conferir) '))

verificar()

