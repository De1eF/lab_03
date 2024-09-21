def calc(num):
    if len(num) != 3:
        print("Лише трьохзначні числа дозволено")
        return
    
    for c in num:
        if not c.isdigit():
            print("Лише числа є дозволеними")
            return

    result = ""

    for c in num:
        result += c + "\n"
        
    print(result)

calc(input("Трьозначне число:"))