from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_prime = Jar(5)
    assert jar_prime.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    jar.deposit(3)
    assert jar.size == 10


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10
    jar.withdraw(10)
    assert jar.size == 0
