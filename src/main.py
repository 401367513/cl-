def hello(name: str = "World") -> str:
    """返回问候语。"""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """返回两数之和。"""
    return a + b


if __name__ == "__main__":
    print(hello())
