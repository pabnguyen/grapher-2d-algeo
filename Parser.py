class Parser:
    def __init__(self, sentence):
        self.sentence = sentence
        self.keyword = ''
        self.data = []
        self._parse_data()

    def _parse_data(self):
        self.data = self.sentence.split()
        self._parse_task()

    def print_data(self):
        print(self.data)

    def _parse_task(self):
        self.keyword = self.data[0]
