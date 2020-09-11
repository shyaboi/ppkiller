import os

def chromeKillSub():
    print("killing google things....starting with chrome")
    os.system(f'taskkill /IM chrome.exe /F')
    os.system(f'taskkill /IM GoogleCrashHandler.exe /F')
    os.system(f'taskkill /IM GoogleCrashHandler64.exe /F')

    
    return