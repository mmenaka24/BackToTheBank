def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def standardiseStr(string):
    if not isinstance(string, str):
        raise TypeError

    return string.lower().strip()


def value(greeting):
    greeting = standardiseStr(greeting)

    if greeting == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
