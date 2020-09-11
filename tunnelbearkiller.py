import os, subprocess, sys

def tunnelBearKillSub():
    print("killing google things....starting with chrome")
    os.system(f'taskkill /IM "TunnelBear.UI.exe" /F')
    os.system(f'taskkill /IM TunnelBear.exe /F')
    os.system(f'taskkill /IM "TunnelBear.Maintenance.exe" /F')
    subprocess.Popen(["powershell.exe", f'Stop-Process -Name "TunnelBear.Maintenance"'], stdout=sys.stdout)

    
    return