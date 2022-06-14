import re


def getNumber():
    number = input("Enter a number: ")
    return number


def numberCleaner(number):
    """
    Remove non-numeric numbers, add a leading zero if it doesnt exist and check if the number is 10 digits long
    """
    cleanNumber = re.sub("[^0-9]", "", number)

    if cleanNumber[0] != "0":
        cleanNumber = "0" + cleanNumber

    if len(cleanNumber) != 10:
        raise ValueError("The number provided is not the correct length.")

    return cleanNumber


if __name__ == "__main__":
    number = getNumber()
    numberCleaner(number)
