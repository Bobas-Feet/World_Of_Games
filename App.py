class AppScore:

    count = 1

    def __init__(self, name):
        self.name = name
        self.id = AppScore.count
        AppScore.count += 1

