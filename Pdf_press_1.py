# -*- coding: utf-8 -*-
"""
# Created by: Resul Demirci
# contact me :https://www.linkedin.com/in/resul-demirci-a23870127/
"""

import pypdfium2 as pdfium
import cv2
import os
import sys
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog, QDialog
from PIL import Image
import time

def choose_pdf_1(dosya,boyut):
    image_list=[]
    pdf = pdfium.PdfDocument(dosya)
    page = pdf.get_page(0)
    page.close()
    page_indices = [i for i in range(len(pdf))]
    renderer = pdf.render_to(
        pdfium.BitmapConv.pil_image,
        page_indices = page_indices)

    for image, index in zip(renderer, page_indices):
        
        percent = (100*index)/len(page_indices)
        percent=round(percent,2)
        sys.stdout.write("\rPDF is compressing -----> {0}%".format(percent))
        sys.stdout.flush() 
        time.sleep(0.1)
        image = image.resize(boyut)
        image.convert('RGB')
        image_list.append(image)
    
       
    sys.stdout.write("\rPDF is compressing -----> ...COMPLETED...")
    image_list[0].save(dosya.replace('.pdf','_pressed.pdf'), save_all=True, append_images=image_list[1:])
    image.close()
    pdf.close()  
def main(dosya):
        print(''' Options: 
        [1] : High Quality Compress
        [2] : Middle Quality Compress
        [3] : Low Quality Compress 
        
        ''')

        option = input("Select on option ------> [1/2/3], type [q] to exit: ")
        if option.lower() == '1':
            choose_pdf_1(dosya,(800,1067))
        if option.lower() == '2':
            choose_pdf_1(dosya,(720,960))
        if option.lower() == '3':
            choose_pdf_1(dosya,(450,600))
        if option.lower() == "q":
            print("Goodbye")
            running = False
            sys.exit()
if __name__ == "__main__":
    running = True
    while running:
        option1 = input("\nSelect a PDF File ------> [S], type [q] to exit: ")
        if option1.lower() == 's':
            fileName = QFileDialog.getOpenFileName(None ,"Open a file", "",
                                                "*pdf")
            dosya = fileName[0]
            if dosya != "":
                main(dosya)
        if option1.lower() == "q":
            print("Goodbye")
            running = False
            sys.exit()
        



