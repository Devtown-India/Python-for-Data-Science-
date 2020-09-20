while(True):
    try:
        num = int(input("Enter a integer: "))
        print(f"Hey you entered {num}, is it your lucky number XD")
        break
    except:
        print("Not a valid number")
    finally:
        print('\nAttempted to Input\n')
