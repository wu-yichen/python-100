class NumberGenerator:

    @staticmethod
    def getSeven(n):
        return [i for i in range(n) if i % 7 == 0]
        

print(NumberGenerator.getSeven(8))
