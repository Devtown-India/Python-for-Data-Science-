while(True):
    try:
        num = int(input("Enter a integer: "))
        print(f"Hey you entered {num}, is it your lucky number XD")
        break
    except ValueError:
        print("Not a valid number")
    except KeyboardInterrupt:
        print("\nNo input taken")
        break
    # except (ValueError, KeyboardInterrupt):
    #     print("Not a valid number")
    #     break
    finally:
        print('\nAttempted to Input\n')
