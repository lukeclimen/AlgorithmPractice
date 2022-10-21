def angryProf(threshold, studentArrivals):
    """Returns a string of either YES or NO to answer the question
    of whether or not an angry prof will cancel his class. The threshold
    for attendance is passed in, as is the time-to-class arrival of each
    student (0 meaning right on time, negative meaning time to spare and
    positive meaning too late)."""
    onTimeStudents = 0
    for timeToClass in studentArrivals:
        if timeToClass <= 0:
            onTimeStudents += 1
    if onTimeStudents >= threshold:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    print('Will class be cancelled? ' + angryProf(4, [-93, -86, 49, -62, -90, -63, 40, 72, 11, 67]))
