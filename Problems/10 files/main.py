for n in range(1, 11):
    with open(f'file{n}.txt', 'w') as file:
        file.write(str(n))
