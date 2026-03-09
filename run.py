import json
import os
import sys

# ၁။ key.json ဖိုင်ထဲက ID ကို ဖတ်တဲ့အပိုင်း
def get_user_id():
    if os.path.exists('key.json'):
        try:
            with open('key.json', 'r') as f:
                data = json.load(f)
                return data.get("id")
        except:
            return None
    return None

# ၂။ ခွင့်ပြုထားတဲ့ ID စစ်ဆေးတဲ့အပိုင်း
authorized_id = "COCO_SWT_789" # ဒီနေရာမှာ သင်ပေးချင်တဲ့ ID ကို ပြောင်းရေးပါ
user_id = get_user_id()

if user_id == authorized_id:
    print("✅ ID Approve ဖြစ်ပါသည်။ SWT Turbo ကို စတင်နေပါပြီ...")
    
    # ၃။ ID မှန်မှ .so ဖိုင်ကို Import လုပ်ပြီး Run မယ်
    try:
        import starlink
        # starlink.so ထဲမှာပါတဲ့ function ကို ဒီမှာ လှမ်းခေါ်ပါ
        # ဥပမာ- starlink.main() သို့မဟုတ် starlink.start()
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("❌ Error: ID မရှိပါ သို့မဟုတ် Approve မရသေးပါ။")
    print(f"သင့် ID: {user_id}")
    sys.exit()
    
