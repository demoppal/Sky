import os
import sys

# ၁။ လိုအပ်တဲ့ Library တွေရှိမရှိစစ်ဆေးပြီး မရှိရင်သွင်းမယ်
try:
    import requests
    import urllib3
except ImportError:
    print("\033[33m[*] Installing required libraries...\033[0m")
    os.system("pip install requests urllib3")
    print("\033[32m[*] Done. Please restart the tool.\033[0m")
    sys.exit()

# ၂။ .so ဖိုင် ရှိမရှိ စစ်ဆေးမယ်
if not os.path.exists("core_script.so"):
    print("\033[31m[!] Error: 'core_script.so' not found!\033[0m")
    print("\033[36mPlease make sure both run.py and core_script.so are in the same folder.\033[0m")
    sys.exit()

# ၃။ core_script.so ထဲက main logic ကို လှမ်းခေါ်မယ်
try:
    import core_script
    if __name__ == "__main__":
        # core_script ထဲက main() function ကို run မယ်
        core_script.main()
except Exception as e:
    print(f"\033[31m[!] Tool Start Failed: {e}\033[0m")
    print("\033[33mHint: This tool is compiled for specific architecture (ARM64/Termux).\033[0m")
