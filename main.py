import time
import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def rodar_speedtest():
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Descomente para rodar em segundo plano

    driver = webdriver.Chrome(options=chrome_options)

    try:
        agora = datetime.datetime.now()
        print(f"Iniciando teste: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

        # --- ORGANIZAÇÃO DE PASTAS ---
        # Cria a pasta principal 'screenshots' se não existir
        pasta_base = "screenshots"
        # Cria a subpasta com a hora atual (ex: 'screenshots/07h', 'screenshots/14h')
        nome_subpasta = agora.strftime("%Hh")
        caminho_diretorio = os.path.join(pasta_base, nome_subpasta)

        if not os.path.exists(caminho_diretorio):
            os.makedirs(caminho_diretorio)
            print(f"Pasta {caminho_diretorio} criada.")

        # --- EXECUÇÃO DO TESTE ---
        driver.get("https://speed.unifique.com.br/")
        time.sleep(5)

        # Localize o seletor correto do site da sua ISP
        botao = driver.find_element(By.ID, "startStopBtn")
        botao.click()

        # Espera o teste terminar (aumente se o teste da sua ISP for demorado)
        time.sleep(60)

        # --- SALVAMENTO DO PRINT ---
        timestamp = agora.strftime("%H-%M-%S")
        nome_arquivo = f"speedtest_{timestamp}.png"
        caminho_final = os.path.join(caminho_diretorio, nome_arquivo)

        driver.save_screenshot(caminho_final)
        print(f"Sucesso! Print salvo em: {caminho_final}")

    except Exception as e:
        print(f"Erro ao rodar teste: {e}")

    finally:
        driver.quit()


# Loop de 5 minutos
while True:
    rodar_speedtest()
    time.sleep(300)