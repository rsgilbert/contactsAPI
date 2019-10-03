import xlrd
# from django.core.files.storage import default_storage
from .models import Finance, Contact

def add_to_contacts(f):
    g = records_generator(f)
    for c in Finance.objects.all():
        c.delete()
    for row in g:
        contact = Contact(
            firstname=record[1],
            lastname=record[2],
            email=record[3],
            sitename=record[4],
            tel1=record[5],
            job=record[6],
            tel2=record[7]
        )
        contact.save()
        print(row)



def add_to_finance_contacts(f):
    g = records_generator(f)
    for c in Finance.objects.all():
        c.delete()
    for row in g:
        finance = Finance.objects.create(
            name=row[0],
            duty=row[1],
            room=row[2],
            contact=row[3]
        )
        finance.save()
        print(row)


def records_generator(f):
    book = xlrd.open_workbook(file_contents=f.read())
    for sheet_idx in range(book.nsheets):
        sheet = book.sheet_by_index(sheet_idx)
        rows = (sheet.get_rows())
        for row in rows:
            print(row)
            for cell in row:
                yield [cell.value for cell in row]
