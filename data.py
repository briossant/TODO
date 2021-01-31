class Data:
    def __init__(self, path):
        self.path = path
        self.tasks = []
        self.open_file()

    def open_file(self):
        try:
            with open(self.path, 'r') as inputs:
                for i in inputs:
                    self.tasks = i.split('|')
                for i, x in enumerate(self.tasks):
                    if x == '':
                        self.tasks.pop(i)
        except FileNotFoundError:
            open(self.path, 'x')
        print(self.tasks)

    def add_task(self, task):
        self.tasks.append('TODO : ' + task)
        self.upload()

    def complete_task(self, index):
        self.tasks.pop(index)
        self.upload()

    def upload(self):
        with open(self.path, 'w') as output:
            output.write('|'.join(self.tasks)+'|')
