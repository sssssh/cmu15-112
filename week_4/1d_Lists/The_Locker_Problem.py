def lockerProblem(lockers):
    isOpen = [False] * (lockers + 1)
    students = lockers
    for student in range(1, students+1):
        for locker in range(student, lockers+1, student):
            isOpen[locker] = not isOpen[locker]
    openLockers = []
    for locker in range(1, lockers+1):
        if isOpen[locker]:
            openLockers.append(locker)
    return openLockers


print(lockerProblem(2000))
