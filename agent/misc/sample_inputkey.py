from getch import getch

print("Push any key. (ESC : exit)")

while True:
    key = ord(getch())
    print(key)
    if key == 27:  # ESC
        print("ESC : exit.")
        break
    elif key == 119:  # W key
        print("Down W Key")
    elif key == 113:  # Q key
        print("Down Q Key")
