import winreg

def print_registry_values(key_path):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            i = 0
            print(key)
            while True:
                try:
                    name, value, value_type = winreg.EnumValue(key, i)
                    print(f"{name}: {value}")
                    i += 1
                except OSError:
                    break
    except OSError as e:
        print(f"Error opening key: {e}")

# Example usage
key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
print_registry_values(key_path)