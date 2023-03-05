class Zajecia:

    def __init__(self):
        self.studenci = []

    def zapiszStudenta(self, student):
        if len(self.studenci) > 10:
            print("Osiągnięto maksymalną liczbę studentów.")

        else:
            self.studenci.append(student)

        return None