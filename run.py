import json
import os
import sys

# ၁။ User ရဲ့ key.json ထဲက ID ကို ဖတ်မယ်
def get_user_id():
    if not os.path.exists('key.json'):
        # key.json မရှိရင် အသစ်ဆောက်ပေးပြီး ရပ်လိုက်မယ်
        with open('key.json', 'w') as f:
            json.dump({"id": ""}, f, indent=4)
        return None
    
    try:
        with open('key.json', 'r') as f:
            data = json.load(f)
            return data.get("id", "").strip()
    except:
        return None

# ၂။ Approved စာရင်းထဲမှာ ပါ၊ မပါ သေချာစစ်မယ်
def is_approved(user_id):
    if not user_id: # ID ဗလာဖြစ်နေရင် ပေးမဝင်ဘူး
        return False
        
    if not os.path.exists('approved_ids.txt'):
        # Approved ဖိုင်မရှိရင် ဘယ်သူ့ကိုမှ ပေးမဝင်ဘူး
        return False
    
    with open('approved_ids.txt', 'r') as f:
        # ID တစ်ခုချင်းစီကို ဖတ်ပြီး Space တွေဖြတ်မယ်
        allowed_list = [line.strip() for line in f.readlines() if line.strip()]
        return user_id in allowed_list

# ၃။ ပင်မလုပ်ဆောင်ချက်
user_id = get_user_id()

if is_approved(user_id):
    print(f"✅ Access Granted: {user_id}")
    try:
        import starlink
        # starlink.main()  # starlink.so ထဲက function ကို ဒီမှာ နှိုးပါ
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("❌ ACCESS DENIED (ခွင့်ပြုချက်မရှိပါ)")
    print(f"🔑 သင့် ID: {user_id if user_id else 'ID ထည့်သွင်းထားခြင်းမရှိပါ'}")
    print("💡 အပေါ်က ID ကို Admin ဆီပို့ပြီး Approve တောင်းပါ။")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sys.exit()
    
