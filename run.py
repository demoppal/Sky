import json
import os
import sys

# ၁။ key.json ထဲက User ထည့်ထားတဲ့ ID ကို ဖတ်မယ်
def get_user_id():
    if os.path.exists('key.json'):
        try:
            with open('key.json', 'r') as f:
                data = json.load(f)
                return data.get("id")
        except: return None
    return None

# ၂။ ခွင့်ပြုထားတဲ့ ID စာရင်း (approved_ids.txt) ကို ဖတ်မယ်
def is_approved(user_id):
    if not os.path.exists('approved_ids.txt'):
        # ဖိုင်မရှိရင် အသစ်ဆောက်ပေးမယ်
        with open('approved_ids.txt', 'w') as f:
            f.write("ADMIN_COCO\n") 
        return False
    
    with open('approved_ids.txt', 'r') as f:
        # ဖိုင်ထဲက ID တွေကို တစ်ကြောင်းချင်းစီ ဖတ်ပြီး စစ်မယ်
        allowed_list = [line.strip() for line in f.readlines()]
        return user_id in allowed_list

# ၃။ လုပ်ဆောင်ချက်အပိုင်း
user_id = get_user_id()

if is_approved(user_id):
    print(f"✅ ID {user_id} Approved! SWT Turbo စတင်နေပါပြီ...")
    try:
        import starlink
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("❌ ACCESS DENIED")
    print(f"🔑 သင့် ID: {user_id if user_id else 'မရှိပါ'}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sys.exit()
    
