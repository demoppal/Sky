import os
import importlib.util

# 1. .so ဖိုင်အရှည်ကြီးရဲ့ နာမည်ကို သတ်မှတ်မယ်
original_so = "myscript.cpython-313-aarch64-linux-android.so"
target_so = "myscript.so"

# 2. အကယ်၍ ဖိုင်နာမည်က အရှည်ကြီး ဖြစ်နေရင် အလွယ်ခေါ်လို့ရအောင် နာမည်ခဏပြောင်းမယ်
if os.path.exists(original_so):
    os.rename(original_so, target_so)

# 3. အခု myscript ဆိုပြီး ပုံမှန်အတိုင်း import လုပ်မယ်
try:
    import myscript
    if __name__ == "__main__":
        myscript.main()
except ImportError:
    print("Error: .so file ကို ရှာမတွေ့ပါ။ GitHub ကနေ သေချာ pull လုပ်ထားလား စစ်ပေးပါ။")
except Exception as e:
    print(f"Error: {e}")
    
