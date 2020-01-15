# for letter in "Helo world":
#     print(letter)



import random

class LotteryMachine:
    #pull six random numbers 1 -> 49
    #check if number already pulled before returning

    def __iter__(self):
        #initial setup
        #return an object that implements __next__()
        self.numbers = []
        return self


    def __next__(self):
        # get the next value and return it
        if len(self.numbers) == 6:
            raise StopIteration
        else:
            number = random.randint(1, 49)
            while number in self.numbers:
                number = random.randint(1, 49)
            self.numbers.append(number)
            return number

machine = LotteryMachine()

for number in machine:
    print(number)
