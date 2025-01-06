from tkinter import *
import win32print
import win32ui
from PIL import Image, ImageDraw, ImageFont

def print_variable():
    content_to_print = """TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
NEW LINE 1
NEW LINE 2
NEW LINE 3"""
    
    printer_name = "EPSON LX-310"

    try:
        printer = win32print.OpenPrinter(printer_name)
        printer_info = win32print.GetPrinter(printer, 2)
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        hdc.StartDoc("Print Variable Content")
        hdc.StartPage()

        font = ImageFont.load_default()
        
        lines = content_to_print.split('\n')
        
        x_pos, y_pos = 10, 10
        line_height = 20  

        image = Image.new("RGB", (600, 300), (255, 255, 255))  
        draw = ImageDraw.Draw(image)
        
        for line in lines:
            draw.text((x_pos, y_pos), line, font=font, fill=(0, 0, 0))
            y_pos += line_height 
        
        image.save("temp_image.png")
        image = Image.open("temp_image.png")

        hdc.DrawText(content_to_print, (100, 100, 500, 200))  

        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()

        alert_label.config(text="Print job sent successfully!", fg="green")
    except Exception as e:
        alert_label.config(text=f"Error: {e}", fg="red")

root = Tk()
root.title("Print Variable Content")
root.geometry("300x150")

Label(root, text="Click the button to print the content.").pack(pady=10)
Button(root, text="Print Content", command=print_variable).pack(pady=10)

alert_label = Label(root, text="", fg="blue")
alert_label.pack(pady=10)

root.mainloop()