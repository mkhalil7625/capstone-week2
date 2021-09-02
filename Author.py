class Author:
    def __init__(self,name:str):
        self.name = name
        self.books = []

    def publish(self,title:str):
        self.books.append(title)

    def __str__(self):
        titles= ','.join(self.books) or 'No Published books'
        return f'{self.name}, Books: {titles}'
        
    def __repr__ (self):
        return f'{self.name}, Books:{self.books}'

def main():
    x=Author('MK')
    x.publish('book1')
    x.publish('book2')

    print(x)

    x1=Author('Mo')
    print(x1)

main()