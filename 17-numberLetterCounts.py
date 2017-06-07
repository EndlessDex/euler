def word_form(number):
    ones = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
            'nine')
    tens = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
            'eighty', 'ninety')
    teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen')
    levels = ('', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
              'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion')

    word = ''
    number = str(number)[::-1]
    if len(number) % 3 == 1: number += '0'

    for x, digit in enumerate(number):
        if x % 3 == 0:
            word = levels[x // 3] + ', ' + word
            prevDigit = int(digit)
        elif x % 3 == 1:
            if digit is '1':
                num = teens[prevDigit]
            elif digit is '0':
                num = ones[prevDigit]
            else:
                num = tens[int(digit)]
                if prevDigit:
                    num += '-' + ones[prevDigit]
            word = num + ' ' + word
        elif x % 3 == 2:
            if digit is not '0':
                if all(n is '0' for n in number[:x]):
                    word = ones[int(digit)] + ' hundred' + word
                else:
                    word = ones[int(digit)] + ' hundred and ' + word
    return word.strip(' , ')


lengths = [len(word_form(i).replace(' ', '').replace('-', ''))
           for i in range(1, 1000 + 1)]
print(sum(lengths))
