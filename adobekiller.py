import os, subprocess, time, sys

# strings with spaces
def adobeKillSub2():
    subprocess.Popen(["powershell.exe", f'Stop-Process -Name "Adobe Desktop Service"'], stdout=sys.stdout)
    subprocess.Popen(["powershell.exe", f'Stop-Process -Name "AdobeUpdateService"'], stdout=sys.stdout)

    print("killing adobe things......")

    os.system('taskkill /IM acrotray.exe /F');print("acro tray killed")
    os.system('taskkill /IM CCXProcess.exe /F');print("CCXProcess killed")
    os.system('taskkill /IM AdobeIPCBroker.exe /F');print("AdobeIPCBroker killed")
    os.system('taskkill /IM AdobeNotificationClient.exe /F');print("AcrobatNotificationClient killed")
    os.system('taskkill /IM CoreSync.exe /F');print("CoreSync killed")
    os.system('taskkill /IM CCLibrary.exe /F');print("CCLibrary killed")
    os.system('taskkill /IM CRWindowsClientService.exe /F');print("CRWindowsClientService killed")
    os.system('taskkill /IM AdobeNotificationHelper.exe /F');print("AdobeNotificationHelper killed")
    os.system('taskkill /IM AcroCEF.exe /F');print("AcroCEF killed")
    os.system('taskkill /IM Acrobat.exe /F');print("Acrobat killed")
    os.system('taskkill /IM "Creative Cloud.exe" /F');print("Creative Cloud killed")
    os.system(f'taskkill /IM CRLogTransport.exe /F');print("CRLogTransport killed")
    os.system(f'taskkill /IM CRWindowsClientService.exe /F');print("CRWindowsClientService killed")
    os.system(f'taskkill /IM AdobeCollabSync.exe /F');print("AdobeCollabSync killed")
    os.system(f'taskkill /IM "Adobe CEF Helper.exe" /F');print("CRWindowsClientService killed")
    os.system(f'taskkill /IM AcrobatNotificationClient.exe /F');print("AcrobatNotificationClient killed")
    os.system(f'taskkill /IM  Photoshop.exe /F');print("Photoshop killed")
    os.system(f'taskkill /IM "Adobe Xd.exe" /F');print("xD killed")
    os.system(f'taskkill /IM Acrobat.exe /F');print("Acrobat killed")
    os.system(f'taskkill /IM Lightroom.exe /F');print("Lightroom killed")
    os.system(f'taskkill /IM AdobeNotificationClient.exe /F');print("AdobeNotificationClient killed")
    os.system(f'taskkill /IM "Creative Cloud Helper.exe" /F');print("Creative Cloud Helper killed")


    print("Adobe things......Killed")
    return

def adobeKillSub():
    adobeKillSub2()
    time.sleep(.2)
    adobeKillSub2()
    time.sleep(.2)
    adobeKillSub2()
    time.sleep(.2)
    adobeKillSub2()
    print("adobe more or less dead")