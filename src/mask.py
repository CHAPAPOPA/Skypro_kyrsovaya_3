class Mask:
    def __init__(self):
        pass

    def how_many_split(self, number):
        words = number.split()
        if len(words) == 2:
            return words[0]
        else:
            return " ".join(words[:-1])

    def check_number(self, number):
        numbers_list = number.split()
        return numbers_list[-1]

    def mask_number(self, line):
        final_word = self.how_many_split(line)
        number = self.check_number(line)
        if len(number) == 20:
            number = '*' * 2 + number[-4:]
        else:
            number = "{} {} {} {}".format(
                number[:4],
                number[4:6] + '**',
                '*' * 4,
                number[-4:]
            )
        return f"{final_word} {number}"



