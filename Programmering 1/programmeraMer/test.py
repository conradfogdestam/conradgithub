
while True:
    try:
        mul = int(input('Vilket tal vill du öva på? '))
        break
    except:
        print('inget heltal försök igen')

count = 0


for i in range(1,11):
    while True:
            a = (int(input(f'{mul} x {i}: ')))

            if a == mul * i:
                print('RÄTT!')
                count += 1
                break
            else:
                print('FEL!!')


print(f'Du hade {count} rätt av 10!')
