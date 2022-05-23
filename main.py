class BookCopy:
    def __init__(self, purchase_date, barcode_num):
        self.purchase_date = purchase_date
        self.barcode_num = barcode_num

    def __str__(self):
        return "COPY: {purchase_date} - {barcode_num}".format(purchase_date=self.purchase_date,
                                                              barcode_num=self.barcode_num)


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = []

    def create_copy(self, purchase_date, barcode_num):
        book_copy = BookCopy(purchase_date, barcode_num)
        self.copies.append(book_copy)
        return book_copy

    def print_copies(self):
        print(self)
        for c in self.copies:
            print(c)

    def __str__(self):
        return "BOOK: {title} - {author}".format(title=self.title, author=self.author)


if __name__ == '__main__':
    b = Book("Patrones de Diseño", "Rodrigo Salazar", "0123456789")
    bc = b.create_copy("23/05/2022", 1234)
    bc.barcode_num = 4321
    b.print_copies()
