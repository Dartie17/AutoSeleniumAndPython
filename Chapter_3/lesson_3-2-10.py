def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == 42, "Should be absolute value of a number"

# Конструкция if __name__ == "__main__" служит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля
if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")