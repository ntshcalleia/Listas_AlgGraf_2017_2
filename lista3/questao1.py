def elevatorFloor(real_floor):
    if real_floor < 4:
        return real_floor

    prev_floor = 2
    current_floor = 3

    for i in range(4, real_floor + 1):
        prev_floor = current_floor
        current_floor = prev_floor + 1
        if current_floor % 10 == 4:
            current_floor = current_floor + 1

    return current_floor

def main():
    floor = int(input("Andar Real: "))
    print("Andar no Elevador: {}".format(elevatorFloor(floor)))


if __name__ == '__main__':
    main()