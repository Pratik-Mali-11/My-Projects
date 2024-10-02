from PIL.FontFile import WIDTH
from matplotlib.pyplot import table
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from datetime import datetime

def create_receipt_pdf(name,items):
    pdf_file_name = f"{name}_receipt.pdf"
    c = canvas.Canvas(pdf_file_name,pagesize = A4)
    width, height = A4

    c.setTitle("Payment receipt")
    c.setAuthor("Frank")

    c.setFont("Helvetica-Bold",20)
    c.drawCentredString(width/2,height-100,"Payment receipt")

    c.setFont("Helvetica",12)
    c.drawString(50,height-150,f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    c.drawString(50,height-170,f"Customer Name: {name}")

    table_data = [["Description","Quantity","Price","Total"]]
    total_amount = 0
    for item in items:
        total = item['price']*item['quantity']
        total_amount +=total
        table_data.append([item['description'],str(item['quantity']),f"Rs.{item['price']:.2f}",f"Rs.{total:.2f}"])

    table_data.append(["","","Total",f"Rs.{total_amount:.2f}"])

    table = Table(table_data,colWidths=[3*inch,1*inch,1*inch,1*inch])

    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.lightgrey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
        ('ALIGN',(1,1),(-1,-1),'CENTER'),
        ('FONTNAME',(0,0),(-1,0),'Helvetica'),
        ('BOTTOMPADDING',(0,0),(-1,0),10),
        ('GRID',(0,0),(-1,-1),1,colors.black),
    ]))



    table.wrapOn(c,width,height)
    table.drawOn(c,50,height-300)
    c.setFont("Helvetica",10)
    c.drawCentredString(width/2,50,"Thankyou for your payment!")
    c.save()
    print(f"receipt saved as {pdf_file_name}")


if __name__=="__main__":
    items = [
        {'description':'T-shirt','quantity': 4,'price':999.00},
        {'description': 'Jeans', 'quantity': 2, 'price': 1599.00},
        {'description': 'shoes', 'quantity': 3, 'price': 2499.00}
    ]

    name = 'Pratik'
    create_receipt_pdf(name,items)
