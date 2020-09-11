import os

def chromeKillSub():
    print("killing google things....starting with chrome")
    os.system(f'taskkill /IM chrome.exe /F')
    return