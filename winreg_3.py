import winreg

def enum_values(key):
    i = 0
    while True:
        try:
            name, value, value_type = winreg.EnumValue(key, i)
            print(f"Name: {name}, Value: {value}, Type: {value_type}")
            i += 1
        except OSError:
            break

# Open a registry key
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")

# Enumerate the values in the key
enum_values(key)

# Close the key
winreg.CloseKey(key)