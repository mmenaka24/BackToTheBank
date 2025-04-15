def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def standardise_str(string):
    if not isinstance(string, str):
        raise TypeError("Input must be a string")

    return string.lower().strip()


def value(greeting):
    greeting = standardise_str(greeting)

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
