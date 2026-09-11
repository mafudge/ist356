if __name__ == "__main__":
    print("Hello from mymodule")

country = "USA"

def say_hi(name: str):
    print(f"Hi, {name}!")

if __name__ == "__main__":
    print("Goodbye from mymodule")


def area_of_rect(length: float, width: float) -> float:
    return length * width 

def test_area_of_rect():
    length = 10
    width = 5
    expect = 50
    actual = area_of_rect(length, width)
    assert actual == expect, f"Expected {expect}, but got {actual}"

if __name__ == "__main__":
    print("Running tests...")
    test_area_of_rect()
