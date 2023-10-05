from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from merge_pdf_app.models import PDFFile
from PyPDF2 import PdfReader, PdfWriter

from io import BytesIO

def merge_pdf_files(request):
    if request.method == 'POST':
        pdf_file_1 = request.FILES['pdf_file_1']
        pdf_file_2 = request.FILES['pdf_file_2']

        pdf_reader_1 = PdfReader(pdf_file_1)
        pdf_reader_2 = PdfReader(pdf_file_2)

        pdf_writer = PdfWriter()

        for page in pdf_reader_1.pages:
            pdf_writer.add_page(page)

        for page in pdf_reader_2.pages:
            pdf_writer.add_page(page)


        stream = BytesIO()
        merged_pdf_file = pdf_writer.write(stream)

        

        response = HttpResponse(stream.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=merged.pdf'

        return response

    else:
        return render(request, 'merge_pdf.html')
