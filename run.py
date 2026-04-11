import importlib.util
import os
import sys

# ၁. ဖိုင်နာမည်ကို main.so လို့ပဲ ထားပါ (နာမည်အရှည်ကြီးဖြစ်နေရင် main.so လို့ အရင်ပြောင်းလိုက်ပါ)
so_file = "main.so"

def start():
    if not os.path.exists(so_file):
        print(f"Error: {so_file} file not found!")
        return

    # ၂. .so ဖိုင်ကို Load လုပ်တဲ့နေရာမှာ နာမည်ကို 'myscript' လို့ပဲ သုံးပါ
    # ဘာလို့လဲဆိုတော့ မူရင်း .py နာမည်က myscript ဖြစ်ခဲ့လို့ပါ
    module_name = "myscript" 
    
    spec = importlib.util.spec_from_file_location(module_name, os.path.abspath(so_file))
    m = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = m
    
    try:
        spec.loader.exec_module(m)
        # ၃. ပုံမှန်အတိုင်း main() ကို ခေါ်မယ်
        m.main()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start()
    
