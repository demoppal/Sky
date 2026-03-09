import json
import os
import sys
import uuid

# ၁။ User ရဲ့ ID ကို ဖတ်မယ် (မရှိရင် အသစ်ထုတ်ပေးမယ်)
def get_or_create_id():
    file_path = 'key.json'
    
    # ဖိုင်မရှိရင် သို့မဟုတ် ဖိုင်ထဲမှာ ID မရှိရင် ID အသစ်တစ်ခု သတ်မှတ်မယ်
    if not os.path.exists(file_path):
        new_id = str(uuid.uuid4())[:8].upper() # ဥပမာ: A52B1110 မျိုးထွက်လာမယ်
        with open(file_path, 'w') as f:
            json.dump({"id": new_id}, f, indent=4)
        return new_id
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            u_id = data.get("id", "").strip()
            if not u_id: # ID ကွက်လပ်ဖြစ်နေရင်
                u_id = str(uuid.uuid4())[:8].upper()
                with open(file_path, 'w') as f:
                    json.dump({"id": u_id}, f, indent=4)
            return u_id
    except:
        return "ERROR_ID"

# ၂။ Approved စာရင်းကို စစ်ဆေးမယ်
def check_approval(u_id):
    approved_file = 'approved_ids.txt'
    if not os.path.exists(approved_file):
        return False
    
    with open(approved_file, 'r') as f:
        allowed = [line.strip() for line in f.readlines() if line.strip()]
    return u_id in allowed

# --- ပင်မလုပ်ဆောင်ချက် ---
current_id = get_or_create_id()

# မျက်နှာပြင်မှာ အမြဲတမ်း ID ကို အပေါ်ဆုံးကပြမယ်
os.system('clear') # Screen ကို အရင်ရှင်းမယ်
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f" 🔑 YOUR ID: {current_id}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if check_approval(current_id):
    print(" ✅ STATUS: APPROVED (အသုံးပြုနိုင်ပါပြီ)")
    print(" 🚀 SWT Turbo စတင်နေပါပြီ...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        import starlink
        # starlink.main() # .so ထဲက function ကို ဒီမှာနှိုးပါ
    except Exception as e:
        print(f" ❌ Error: {e}")
else:
    print(" ❌ STATUS: NOT APPROVED (ခွင့်ပြုချက်မရသေးပါ)")
    print(" 💡 အပေါ်က ID ကို ကူးပြီး Admin ဆီမှာ Approve တောင်းပါ။")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sys.exit() # ID မမှန်ရင် ဒီမှာတင် ရပ်သွားပါလိမ့်မယ်
