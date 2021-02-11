while True:
        fel = 0
        try:
            user_input = int(input("Mata in det heltalet du vill öva på: "))
        except:
            print("Det var inget heltal")
        for i in range(1, 11):
            while True:
                for_input = int(input(f'Vad blir {user_input} * {i} blir: '))
                if user_input * i != for_input:
                    print("WRONG")
                    fel += 1
                else:
                    print("RIGHT")
                    break
        print(" ")
        print("Bra jobbat!")
        print(f'Du hade {fel} fel')