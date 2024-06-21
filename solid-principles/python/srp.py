################# Making a buf reader /writer the wrong way without following Single Responsibility 

class BufHandler:
    def __init__(self,file) -> None:
        self.file= file

    def read_file(self):
        with open(self.file, 'r') as file:
            return file.read()

    def write_file(self, data):
        with open(self.file, 'w') as file:
            file.write(data)


buf_handler= BufHandler('example.txt')
content = buf_handler.read_file()
print(f'Content read: {content}')

buf_handler.write_file('Hello, SRP!')
print('Data written to file.')


################# Making a buf reader /writer the right way

class BufReader:
    def __init__(self,file) -> None:
        self.file= file

    def read_file(self):
        with open(self.file, 'r') as file:
            return file.read()

class BufWriter:
    def __init__(self,file) -> None:
        self.file= file
    def write_file(self, data):
        with open(self.file, 'w') as file:
            file.write(data)


reader = BufReader('example.txt')
writer = BufWriter('example.txt')

content = reader.read_file()
print(f'Content read: {content}')

writer.write_file('Hello, SRP!')
print('Data written to file.')



