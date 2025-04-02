class HistoryContainer:
    """
    A class to manage a history of modifications.
    It allows adding entries, retrieving the history, and clearing it.

    More function with be added when needed.
    """
    def __init__(self):
        self.history = []

    def addHistory(self, entry):
        self.history.append(entry)

    def getHistory(self):
        return self.history

    def clearHistory(self):
        self.history.clear()

    def __str__(self):
        string = "History:\n"
        for entry in self.history:
            string += str(entry) + "\n"
        return string.strip()

class History:
    """
    A class to store modification details.
    By default, it is best paired with table like data structures, but other structure should work well.

    """
    def __init__(self, **kwargs):
        self.data = {}
        for key, value in kwargs.items():
            self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self):
        return str(self.data)