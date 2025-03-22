

import os
import time
import ctypes  # For Windows dialog boxes

REPEAT_INTERVAL = 3600  # Repeat frequency in seconds

while True:
    # Text-to-speech command (Windows PowerShell)
    os.system("powershell -Command \"Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Hey Khuzaima drink water')\"")
    
    # Dialog box (Windows API)
    ctypes.windll.user32.MessageBoxW(0, "Hey Khuzaima, Drink water", "Reminder", 0x40)
    
    time.sleep(REPEAT_INTERVAL)