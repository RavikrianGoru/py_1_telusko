def main():
    text = input("Enter text to check palindrome or not:")
    print(f'Input : {text}')

    if is_palindrome_v2(text):
        print('Yes, {text} is palindrome.')
    else:
        print('NO, {text} is not palindrome.')


def is_palindrome(text):
    return text == text[::-1]


def is_palindrome_v2(text):
    ''' case insensitive ignore punctuation '''
    forbidden = (' ', '.', ',', ';', ':', '?')
    text = removePunctuations(text, forbidden)
    return text == text[::-1]


def removePunctuations(text, forbidden):
    for each in forbidden:
        text = text.replace(each, '')
    text = text.lower()
    return text


if __name__ == '__main__':
    main()


