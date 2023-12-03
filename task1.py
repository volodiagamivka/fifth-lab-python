class Musician:
    """Information about singers"""
    
    def __init__(self, name, fee, age):
        self.__name = name
        self.__fee = fee
        self.__age = age

    def get_name(self):
        return self.__name

    def get_fee(self):
        return self.__fee

    def get_age(self):
        return self.__age

    def __del__(self):
        print(f"{self.__name} був видалений")


class MusicFestival:
    """Information about festival"""
    
    def __init__(self, max_finance, musicians=None):
        self.__max_finance = max_finance
        self.singers = []
        if musicians is None:
            musicians = []
        for musician in musicians:
            self.add_musician(musician)

    def add_musician(self, musician):
        total_fee = sum(sing.get_fee() for sing in self.singers) + musician.get_fee()
        if total_fee <= self.__max_finance:
            self.singers.append(musician)
            print(f"{musician.get_name()} доданий до фестивалю.")
        else:
            print(
                f"{musician.get_name()} не може бути доданий через перевищення бюджету."
            )

    def remove_musician(self, musician):
        if musician in self.singers:
            self.singers.remove(musician)
            print(f"{musician.get_name()} був видалений з фестивалю.")
        else:
            print(f"{musician.get_name()} немає на фестивалі.")


def main():
    michael_cashmore = Musician("Michael Cashmore", 5000, 30)
    ben_adams = Musician("Ben Adams", 3000, 25)
    adele = Musician("Adele", 20000, 35)

    festival = MusicFestival(10000)

    festival.add_musician(michael_cashmore)
    festival.add_musician(ben_adams)
    festival.add_musician(adele)

    festival.remove_musician(michael_cashmore)


if __name__ == "__main__":
    main()
