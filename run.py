import main  # main.so ကို import လုပ်တာပါ

if __name__ == "__main__":
    try:
        main.main()  # main.so ထဲက main function ကို ခေါ်တာပါ
    except Exception as e:
        print(f"Error: {e}")
        
