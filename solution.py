while True:
    print("please enter a number")
    number = input(":>")
    if number is "done":
        break
    try:
       number = int(number)
    except:
        print("Invalid input")
        continue
    if number%2 == 0:
        print("even")
    else:
        print("odd") 
 
