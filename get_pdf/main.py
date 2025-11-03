import requests
from pathlib import Path
import fitz  # PyMuPDF
import os


def get_data(IMG_PATH, img_name, end, pdf_name, JSESSION, WMONID, page_id):
    BASE = "https://edu.ssafy.com"
    URL = BASE + IMG_PATH
    out_dir = Path("downloads")
    out_dir.mkdir(exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": f"https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/{page_id}/index.html",
        "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        "X-Requested-With": "XMLHttpRequest",
    }

    pdf_document = fitz.open()  # PDF 생성용

    for idx in range(1, end + 1):
        out_file = out_dir / f"{img_name}_{idx}.jpg"
        URL_F = URL + str(idx).zfill(4) + ".jpg"

        with requests.Session() as s:
            s.cookies.set("JSESSIONID_HAKSAF", JSESSION, domain="edu.ssafy.com", path="/")
            s.cookies.set("WMONID", WMONID, domain="edu.ssafy.com", path="/")

            with s.get(URL_F, headers=headers, stream=True, verify=True) as r:
                print(f"[{idx}] status:", r.status_code, "content-type:", r.headers.get("Content-Type"))
                r.raise_for_status()
                with open(out_file, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 8):
                        if chunk:
                            f.write(chunk)
        print("Saved to", out_file.resolve())

        try:
            pix = fitz.Pixmap(str(out_file))
            pdf_page = pdf_document.new_page(width=pix.width, height=pix.height)
            pdf_page.insert_image(pdf_page.rect, filename=str(out_file))
            pix = None
        except Exception as e:
            print(f"⚠️ 이미지 {idx} 추가 중 오류:", e)

    output_path = os.path.join(out_dir, f"{pdf_name}.pdf")
    pdf_document.save(output_path)
    pdf_document.close()

    print(f"\n✅ PDF 저장 완료: {output_path}")


if __name__ == "__main__":
    IMG_PATH = "/data/upload_files/crossUpload/openLrn/ebook/unzip/A2025101709083371500/assets/page-images/page-ee9d3adb-1d3e7415-"
    JSESSION = "VVj-0cLRT_YXAcehtEfA1iUO2B_BN0nwbxoYYaWiG8-hVaooxFAa!-2096080651!1456852319!1760916783825"
    WMONID = "Q8RVGq_Du-z"
    page_id = "A2025101512361977200"

    # (기본 주소, 이미지파일 이름, 마지막 페이지 번호, pdf 이름, jsession, wmonid, page_id)
    get_data(IMG_PATH, "AI5", 235, "AI_5강", JSESSION, WMONID, page_id)
