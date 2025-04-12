import emoji

class Jar:
    def __init__(self, capacity=12, cookie_num=0):
        self.capacity = capacity
        self.cookie_num = cookie_num

    def __str__(self):
        cookie_number=""
        for i in range (0, self.cookie_num):
            cookie_number = str(cookie_number) + emoji.emojize(":cookie:")
        return cookie_number
    

    def deposit(self, n):
        new_amount = self.cookie_num + n
        if  new_amount> self.capacity:
            raise ValueError
        else:
            self.cookie_num = new_amount
        return new_amount

    def withdraw(self, n):
        new_amount = self.cookie_num - n
        if  new_amount < 0:
            raise ValueError
        else:
            self.cookie_num = new_amount
        return new_amount

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self._size


def main():
    myJar = Jar(capacity=10, cookie_num=3)
    print(myJar)
    myJar.deposit(3)
    print(myJar)
    myJar.withdraw(1)
    print(myJar)
    print(f"The jar has {myJar.size} cookies out of a capacity of {myJar.capacity}")


if __name__ == "__main__":
    main()