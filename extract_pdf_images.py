"""Extract each page of EV-FLOW.pdf as PNG to public/ev-flow/."""
import fitz  # PyMuPDF
import os

PDF_PATH = r"c:\Users\Aswin Jojo\AppData\Roaming\Cursor\User\workspaceStorage\2d4320bf37b48b10b55c70558e56b7f7\pdfs\9b161f15-447c-4396-91ec-0f8d879b7507\EV-FLOW.pdf"
OUT_DIR = os.path.join(os.path.dirname(__file__), "public", "ev-flow")

os.makedirs(OUT_DIR, exist_ok=True)
doc = fitz.open(PDF_PATH)
for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x scale for clarity
    out_path = os.path.join(OUT_DIR, f"page-{i+1:02d}.png")
    pix.save(out_path)
    print("Saved", out_path)
doc.close()
print("Done.")
