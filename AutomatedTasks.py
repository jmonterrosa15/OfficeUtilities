import webbrowser
import subprocess
import os

def main():
    #Select the productivity task that you want to do
    #1: salesforce, 2: read at learn.cisco.com
    print('Qué deseas hacer hoy? ')
    print('1: Learning')
    print('2 Salesforce')
    option = input()

    if (option == '1'):
        openLearning()
    elif (option == '2'):
        openSalesforce()
        
#Open firefox: Cisco Learning
def openLearning():
    #Open Firefox
    subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe', 'https://learn.cisco.com/'])
    #Open Onenote
    os.system('start explorer shell:appsfolder\Microsoft.Office.OneNote_8wekyb3d8bbwe!microsoft.onenoteim')
    print('Learning Tasks Started')


def openSalesforce():
    #Open Salesforce
    webbrowser.open("https://ciscosales.my.salesforce.com/home/home.jsp")
    #Open outlook tabs
    os.startfile("outlook")
    os.startfile("outlook")
    #Open Sticky Notes
    os.system('start explorer shell:appsfolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App')
    print('Salesforce Tasks Started')
main()

#Tip: to find app IDs, go to PowerShell and use get-StartApps