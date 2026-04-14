import sys
import os

try:
    import engine 
except ImportError:
    print("\033[31m[!] engine.so not found!\033[0m")
    sys.exit()

if __name__ == "__main__":
    os.system('clear')
    engine.main()
    
