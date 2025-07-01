import subprocess, os, ctypes

# disabling window defender
def windead():
    commands = [r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 1 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableIOAVProtection /t REG_DWORD /d 1 /f""",
                r"""shutdown -r /t 0"""]


    for command in commands:
        try:
                subprocess.call(command)
        except Exception as e:
                print(e)


# Restoring window defender to normal functioning
def winlive():
    commands = [r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 0 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 0 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 0 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 0 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 0 /f""",
                r"""reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableIOAVProtection /t REG_DWORD /d 0 /f"""
                r"""shutdown -r /t 0"""]


    for command in commands:
        try:
            subprocess.call(command)
        except Exception as e:
            print(e)

print("""\nDefender Killer
Author: github.com/Always-Root
Purpose: When malware researchers work on Windows,
         Windows Defender often interferes significantly,
         making it difficult to proceed. Disabling it becomes
         a necessary step to continue research effectively.\n\n""")
if ctypes.windll.shell32.IsUserAnAdmin():
    response = input("1 => Disable Defender\n2 => Enable Defender\n3 => Exit\n# ")
    if int(response) == 1:
        windead()
    elif int(response) == 2:
        winlive()
    else:
        print("")
else:
    print("Please, run the script with admin privileges.")

# compiling
# pyinstaller --noconfirm --noconsole --onefile --uac-admin --clean source_file.py
