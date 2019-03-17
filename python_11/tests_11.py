from cw_11_1 import Student

def test_student_average_success():
    niko = Student('Niko', 'NK', 13, [10, 10, 9, 10, 5])
    avg = niko.avg_mark()
    assert avg == 8.8

def test_student_average_wrong():
    niko = Student('Niko', 'NK', 13, [10, 10, 9, 10, 5])
    avg = niko.avg_mark()
    assert avg == 100