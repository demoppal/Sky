import kzee
import os

if __name__ == "__main__":
    try:
        # kzee.so ထဲက main() function ကို လှမ်းခေါ်တာပါ
        kzee.main()
    except KeyboardInterrupt:
        print("\n[!] Stopping script...")
    except Exception as e:
        print(f"\n[!] Error: {e}")
        
