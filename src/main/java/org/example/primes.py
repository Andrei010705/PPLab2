print("Entering python")

class AcceptFilter:
    def accept(self, n):
        return True


class DivisibleByFilter:
    number = None
    next_item = None

    def __init__(self, number, next_item):
        self.number = number
        self.next_item = next_item

    def accept(self, n):
        self_filter = self
        while self_filter is not None and type(self_filter) == DivisibleByFilter:
            if n % self_filter.number == 0:
                return False
            self_filter = self_filter.next_item
        return True


class PrimeChecker:
    def __init__(self):
        self.number = 2
        self.applied_filter = AcceptFilter()

    def next_item(self):
        while not self.applied_filter.accept(self.number):
            self.number += 1
        self.applied_filter = DivisibleByFilter(self.number, self.applied_filter)
        return self.number


def checksum_polynomial(text):
    checksum = 0
    for i, ch in enumerate(text):
        checksum += ord(ch) * ((i+1) ** 5)
    return checksum

def sumaEx1(word):
    checksum = 0
    word = word[1:-1] if len(word) > 2 else word  # eliminăm primul și ultimul dacă sunt mai multe caractere
    for i, ch in enumerate(word):
        checksum += ord(ch) * ((i + 1) ** 5)
    return checksum


if __name__ == '__main__':
    checker = PrimeChecker()
    primes = []

    for _ in range(5000):
        primes.append(checker.next_item())

    #aplicatii
    # text = ''.join(str(p) for p in primes)
    # text = text[1:-1]
    #
    # result = checksum_polynomial(text)

    #ex1
    primes_str = [str(p) for p in primes]

    #dictionar de grupe cu csum si numere
    groups = {}
    for num_str in primes_str:
        csum = sumaEx1(num_str)
        if csum not in groups:
            groups[csum] = []
        groups[csum].append(num_str)


    for csum, nums in groups.items():
        if len(nums) > 1:
            print(f"Numere cu aceeași sumă de control {csum}: {nums}")

    print(f'Computed 111{len(primes)} prime numbers')
    print(f'The last 5 are: {primes[-5:]}')
    print(f'The polinomial sum: {result}')
