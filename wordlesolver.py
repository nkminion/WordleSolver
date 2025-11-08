import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def CreateWordList(WordList):
	with open('WordList.txt','r',encoding='UTF-8') as file:
		while line := file.readline():
			WordList.append(line.rstrip())
			
def GetStatus(status,num):
	status = list(status)
	for i in range(5):
		cell = driver.find_element(By.XPATH,f'//*[@id="wordle-app-game"]/div[1]/div/div[{num}]/div[{i+1}]/div')
		state = cell.get_attribute("data-state")
		if (state=="correct"):
			status[i] = "G"
		elif (state=="present"):
			status[i] = "Y"
		elif (state=="absent"):
			status[i] = "B"
	status = "".join(status)
	return status

def MakeGuess(num,status,WordList,guess):
	if num == 1:
		print(f"Guess: {(guess := 'audio')}")
		return guess
	else:
		for i in range(len(status)):
			if status[i] == 'G':
				j = 0
				while (j<len(WordList)):
					if WordList[j][i] != guess[i]:
						WordList.pop(j)
					else:
						j += 1
			elif status[i] == 'Y':
				j = 0
				while (j<len(WordList)):
					if guess[i] not in WordList[j]:
						WordList.pop(j)
					else:
						j += 1
				j = 0
				while (j<len(WordList)):
					if WordList[j][i] == guess[i]:
						WordList.pop(j)
					else:
						j += 1
			elif status[i] == 'B':
				j = 0
				while (j<len(WordList)):
					if ((guess[i] in WordList[j]) and WordList[j].count(guess[i]) >= guess.count(guess[i])):
						#print(f"Letter: {guess[i]}\nOccurence in guess: {guess.count(guess[i])}\nOccurence in word: {WordList[j].count(guess[i])}\nRemoving word: {WordList[j]}")
						WordList.pop(j)
					else:
						j += 1
			else:
				print("Wrong input lol, I need to automate this")
		print(f"Guess: {(guess := random.choice(WordList))}")
		return guess
						

WordList = []
status = "     "
guess = ""
tries = 1
WordleURL = "https://www.nytimes.com/games/wordle/index.html"
DriverPath = "chromedriver"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get(WordleURL)
print("Page Loaded")
#play button
try:
    PlayButton = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[2]/button[3]"))
    )
    PlayButton.click()

    #close popup
    ClosePopupButton = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="help-dialog"]/div/div/button'))
    )
    ClosePopupButton.click()

    Game = wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body'))
    )
except Exception:
	print("Error occured in clicking")

CreateWordList(WordList)
time.sleep(4)

if Game is not None:
    while (tries <= 6):
        guess = MakeGuess(tries,status,WordList,guess)
        Game.send_keys(guess)
        Game.send_keys(Keys.ENTER)
        time.sleep(2)
        status = GetStatus(status,tries)
        if status == "GGGGG":
            break
        tries += 1

time.sleep(10)
driver.quit()

