import sys
import os

# 1. Verification of the Compiled (.so) File
try:
    import engine  # This imports your engine.so
except ImportError:
    print("\033[31m[!] Error: 'engine.so' not found!\033[0m")
    print("\033[33m[*] Ensure the .so file is in this directory.\033[0m")
    sys.exit()

# 2. Execution Logic
def start_app():
    try:
        # Calls the main() function inside engine.so
        engine.main()
    except KeyboardInterrupt:
        print("\n\033[31m[!] Terminated by user.\033[0m")
        sys.exit()
    except Exception as e:
        print(f"\033[31m[!] System Error: {e}\033[0m")
        sys.exit()

if __name__ == "__main__":
    # Clear screen before starting for a clean UI
    os.system('clear')
    start_app()
    
