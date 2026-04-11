import importlib.util
import os
import sys

# ၁. ဖိုင်နာမည် အတိအကျကို ဒီမှာရေးထားတယ်
so_file = "myscript.cpython-313-aarch64-linux-android.so"

def load_and_run():
    if not os.path.exists(so_file):
        print(f"Error: {so_file} ကို ရှာမတွေ့ပါ။")
        return

    # ၂. .so ဖိုင်ကို တိုက်ရိုက် Load လုပ်တဲ့ process
    spec = importlib.util.spec_from_file_location("myscript", os.path.abspath(so_file))
    myscript = importlib.util.module_from_spec(spec)
    sys.modules["myscript"] = myscript
    
    try:
        spec.loader.exec_module(myscript)
        # ၃. script ကို စတင် run မယ်
        myscript.main()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    load_and_run()
    
