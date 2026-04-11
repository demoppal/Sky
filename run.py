import sys
import os

# Core_script.so ကို ရှာလို့ရအောင် လက်ရှိ folder ကို path ထဲထည့်ခြင်း
sys.path.append(os.getcwd())

try:
    # .so ဖိုင်နာမည် Core_script ဖြစ်တဲ့အတွက် Core_script ကို import လုပ်ပါမယ်
    import Core_script 
    
except ImportError as e:
    print("\033[31m" + "="*50)
    print(f"[!] ERROR: 'Core_script.so' ဖိုင်ကို ရှာမတွေ့ပါ")
    print(f"[!] ဖိုင်နာမည် မှန်မမှန် သို့မဟုတ် Folder တစ်ခုတည်းမှာ ရှိမရှိ စစ်ဆေးပါ")
    print(f"[!] Details: {e}")
    print("="*50 + "\033[0m")
    sys.exit(1)

def launch():
    try:
        # Core_script.so ထဲက main() function ကို လှမ်းခေါ်တာပါ
        # (သင့်မူရင်း script မှာ def main(): လို့ ပေးထားခဲ့ရင် ဒါက တန်းအလုပ်လုပ်ပါမယ်)
        Core_script.main()
        
    except AttributeError:
        print("\033[31m[!] Error: Core_script.so ထဲမှာ main() ဆိုတဲ့ function မတွေ့ပါဘူး\033[0m")
    except KeyboardInterrupt:
        print("\n\033[33m[!] User က ပိတ်လိုက်ပါပြီ။ သွားပြီနော်...\033[0m")
        sys.exit(0)
    except Exception as e:
        print(f"\033[31m[!] Runtime Error: {e}\033[0m")

if __name__ == "__main__":
    launch()
    
