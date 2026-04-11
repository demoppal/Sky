import importlib.util
import os
import sys

# ၁။ ခေါ်သုံးမယ့် Binary ဖိုင်နာမည်
SO_FILE = "main.so"

def start_tool():
    # ဖိုင်ရှိမရှိ အရင်စစ်မယ်
    if not os.path.exists(SO_FILE):
        print(f"\033[31m[!] Error: {SO_FILE} ကို ရှာမတွေ့ပါ။\033[0m")
        print("ကျေးဇူးပြု၍ GitHub ကနေ pull ပြန်ဆွဲပါ သို့မဟုတ် ဖိုင်နာမည် မှန်မမှန် စစ်ပါ။")
        return

    # ၂။ .so ဖိုင်ကို Dynamic Load လုပ်မယ်
    try:
        spec = importlib.util.spec_from_file_location("main_module", os.path.abspath(SO_FILE))
        m = importlib.util.module_from_spec(spec)
        sys.modules["main_module"] = m
        spec.loader.exec_module(m)

        # ၃။ Script ထဲက main() function ကို စတင် Run မယ်
        if hasattr(m, 'main'):
            m.main()
        else:
            print("\033[31m[!] Error: Script ထဲမှာ main() function ကို ရှာမတွေ့ပါ။\033[0m")
            
    except Exception as e:
        print(f"\033[31m[!] Error Occurred: {e}\033[0m")

if __name__ == "__main__":
    start_tool()
    
