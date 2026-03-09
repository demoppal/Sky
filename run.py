import json
import os
import sys
import uuid

# ၁။ ဖုန်းရဲ့ Unique ID ကို ထုတ်ယူခြင်း (သို့မဟုတ် Random ID တစ်ခု သတ်မှတ်ခြင်း)
def get_device_id():
    # ဒါက ဖုန်းတစ်လုံးချင်းစီအတွက် မတူညီတဲ့ ID တစ်ခု ထုတ်ပေးမှာပါ
    return str(uuid.uuid4())[:8].upper()

# ၂။ key.json ဖိုင်ထဲက ID ကို ဖတ်တဲ့အပိုင်း
def get_stored_id():
    if os.path.exists('key.json'):
        try:
            with open('key.json', 'r') as f:
                data = json.load(f)
                return data.get("id")
        except:
            return None
    return None

# ၃။ လုပ်ဆောင်ချက်အပိုင်း
device_id = get_device_id()
stored_id = get_stored_id()
authorized_id = "SWT-COCO-1234" # သင် Approve ပေးမယ့် ID ကို ဒီမှာ ပြောင်းလို့ရပါတယ်

if stored_id == authorized_id:
    print("✅ ID Approved! SWT Turbo ကို စတင်နေပါပြီ...")
    try:
        import starlink
        # starlink.so ထဲက function ကို နှိုးပါ
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("❌ ACCESS DENIED (ဝင်ရောက်ခွင့် မရှိပါ)")
    print(f"🔑 သင့်ရဲ့ ID: {device_id}") 
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("💡 အပေါ်က ID ကို ကူးပြီး Admin ဆီမှာ Approve တောင်းပါ။")
    
    # key.json မရှိရင် အလိုအလျောက် ဆောက်ပေးမယ့်အပိုင်း (User အတွက် အလွယ်တကူ)
    if not os.path.exists('key.json'):
        with open('key.json', 'w') as f:
            json.dump({"id": ""}, f, indent=4)
            
    sys.exit()
    
