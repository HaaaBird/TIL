import pytesseract
from pdf2image import convert_from_path
import fitz  # PyMuPDF
from PIL import Image
import os

# 🧠 Tesseract OCR 실행 파일 경로 (Windows 기준)
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def apply_ocr_to_pdf(input_pdf_path):
    output_pdf_path = os.path.splitext(input_pdf_path)[0] + "_ocr.pdf"
    pdf_document = fitz.open()
    
    pages = convert_from_path(input_pdf_path, dpi=300)
    print(f"총 {len(pages)}페이지 OCR 처리 중...")

    for i, img in enumerate(pages, 1):
        text = pytesseract.image_to_string(img, lang="kor+eng")
        
        img_byte_arr = img.tobytes("jpeg", "RGB")
        pix = fitz.Pixmap(fitz.csRGB, fitz.open("jpeg", img_byte_arr).extract_image(0)["image"])
        page = pdf_document.new_page(width=pix.width, height=pix.height)
        page.insert_image(page.rect, stream=img_byte_arr)
        page.insert_text((50, 50), text, fontsize=8, overlay=False)
        print(f"{i}페이지 완료")

    pdf_document.save(output_pdf_path)
    pdf_document.close()
    print(f"\n📘 OCR 적용된 PDF 저장 완료: {output_pdf_path}")


if __name__ == "__main__":
    # 🔹 OCR 적용할 PDF 파일 경로 지정
    pdf_path = r"C:/TIL/get_pdf/downloads/AI_1.pdf"
    apply_ocr_to_pdf(pdf_path)
