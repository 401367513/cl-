from src.main import add, hello, multiply


class TestHello:
    def test_default(self):
        assert hello() == "Hello, World!"

    def test_custom_name(self):
        assert hello("Claude") == "Hello, Claude!"


class TestAdd:
    def test_positive(self):
        assert add(1, 2) == 3

    def test_negative(self):
        assert add(-1, -2) == -3

    def test_zero(self):
        assert add(0, 5) == 5


class TestMultiply:
    def test_positive(self):
        assert multiply(3, 4) == 12

    def test_negative(self):
        assert multiply(-2, 3) == -6

    def test_zero(self):
        assert multiply(0, 5) == 0
