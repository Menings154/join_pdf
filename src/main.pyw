import os
import glob
import sys
import shutil
import PyPDF2 as pdf


def main_function():
    final_path = r"C:\Users\Benja\OneDrive\Desktop\Join PDF\merged pdfs\\" + sys.argv[1].lower() + ".pdf"
    # final_path = r"C:\Users\Benja\OneDrive\Desktop\Join PDF\merged pdfs\\" + "test_k" + ".pdf"
    files = glob.glob(r"C:\Users\Benja\OneDrive\Desktop\Join PDF\pdfs to merge\*.pdf")

    try:
        os.mkdir(r"C:\Users\Benja\OneDrive\Desktop\Join PDF\pdfs to merge\old\\" + sys.argv[1].lower())
    except:
        pass

    try:
        dic = {}
        for file in files:
            dic[int(file[55:-4])] = file

    except:
        dic = {}
        for file in files:
            dic[os.stat(file).st_mtime] = file

    order = list(dic.keys())
    order.sort()

    pdf_writer = pdf.PdfFileWriter()
    for key in order:
        pdf_reader = pdf.PdfFileReader(dic[key])
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(pageNumber=page))

        print(dic[key][:55] + "old" + "\\" + sys.argv[1].lower() + "\\" + dic[key][55:])
        shutil.move(dic[key], dic[key][:55] + "old" + "\\" + sys.argv[1].lower() + "\\" + dic[key][55:])
        # shutil.move(dic[key], dic[key][:55] + "old" + "\\" + "test_k" + "\\" + dic[key][55:])
   
    with open(final_path, 'wb') as out:
        pdf_writer.write(out)
    


if __name__ == '__main__':
    main_function()