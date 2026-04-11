import sys
import os

# လက်ရှိ folder ကို path ထဲထည့်ပေးခြင်းဖြင့် .so ဖိုင်ကို ရှာရလွယ်စေပါတယ်
sys.path.append(os.getcwd())

try:
    # ဖိုင်နာမည် core_script.so ဖြစ်တဲ့အတွက် core_script ကို import လုပ်ပါမယ်
    import core_script 
    
except ImportError as e:
    print("\033[91m" + "!"*50)
    print(f"[!] Error: 'core_script.so' ဖိုင်ကို ရှာမတွေ့ပါ")
    print(f"[!] ဖိုင်နာမည်က {os.getcwd()} ထဲမှာ ရှိနေရပါမယ်")
    print(f"[!] အမှားအသေးစိတ်: {e}")
    print("!"*50 + "\033[0m")
    sys.exit(1)

def start():
    try:
        # .so ထဲက main() function ကို ခေါ်လိုက်တာပါ
        core_script.main()
        
    except AttributeError:
        print("\033[91m[!] Error: .so ဖိုင်ထဲမှာ main() ဆိုတဲ့ function ကို ရှာမတွေ့ပါ\033[0m")
    except KeyboardInterrupt:
        print("\n\033[93m[!] Tool ကို ပိတ်လိုက်ပါပြီ\033[0m")
        sys.exit(0)
    except Exception as e:
        print(f"\033[91m[!] Runtime Error: {e}\033[0m")

if __name__ == "__main__":
    start()
    
