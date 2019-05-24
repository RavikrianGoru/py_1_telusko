def main():
    try:
        print('Open: Resources..........')
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        c = a / b
        print(c)
    except ValueError as e:
        print("Invalid input format")
    except ZeroDivisionError as e:
        print("Can not divide a number by 0")
    except Exception as e:
        print('Invalid input')
    finally:
        print('Close: Resources..........')

if __name__ == '__main__':
    main()
