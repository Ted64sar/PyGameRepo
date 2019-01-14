class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    data = open("top 10000 passwd.txt").read().split()
    stroki = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'ёйцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    f0 = '0' in password
    f1 = '1' in password
    f2 = '2' in password
    f3 = '3' in password
    f4 = '4' in password
    f5 = '5' in password
    f6 = '6' in password
    f7 = '7' in password
    f8 = '8' in password
    f9 = '9' in password
    if len(password) < 9:
        raise LengthError
    elif password.upper() == password:
        raise LetterError
    elif password.lower() == password:
        raise LetterError
    elif not (f0 or f1 or f2 or f3 or f4 or f5 or f6 or f7 or f8 or f9):
        raise DigitError
    else:
        for j in range(len(password) - 2):
            for x in stroki:
                if password[j:j + 3:].lower() in x:
                    raise SequenceError
    return True


a = True
while a is True:
    parol = input()
    try:
        if parol == 'Ctrl+Break':
            raise KeyboardInterrupt
        else:
            z = check_password(parol)
            if z is True:
                print('ok')
                break

    except LengthError:
        print('LengthError')
    except SequenceError:
        print('SequenceError')
    except DigitError:
        print('DigitError')
    except LetterError:
        print('LetterError')
    except KeyboardInterrupt:
        print('Bye-Bye')
        break
