import os
import shutil
import glob
import fitz  # PyMuPDF
import re
import json

src_dir = r"C:\Users\KAVYA\Downloads\Certificate"
dest_dir = r"c:\Users\KAVYA\Downloads\WEBSITES\Portfolio Website\assets\certificates"

os.makedirs(dest_dir, exist_ok=True)

pdf_files = glob.glob(os.path.join(src_dir, "*.pdf"))

admin_file = r"c:\Users\KAVYA\Downloads\WEBSITES\Portfolio Website\admin.html"
index_file = r"c:\Users\KAVYA\Downloads\WEBSITES\Portfolio Website\index.html"

new_certs = []
idx = 100

for pdf in pdf_files:
    filename = os.path.basename(pdf)
    base_name = os.path.splitext(filename)[0]
    
    # Copy PDF
    dest_pdf = os.path.join(dest_dir, filename)
    shutil.copy2(pdf, dest_pdf)
    
    # Extract Image & Text
    doc = fitz.open(pdf)
    page = doc[0]
    pix = page.get_pixmap(dpi=150)
    image_filename = f"{base_name}.jpg"
    dest_img = os.path.join(dest_dir, image_filename)
    pix.save(dest_img)
    
    text = page.get_text()
    doc.close()
    
    # Heuristics for name/issuer
    issuer = "Online Course"
    if "coursera" in text.lower():
        issuer = "Coursera"
    elif "udemy" in text.lower():
        issuer = "Udemy"
    elif "google" in text.lower():
        issuer = "Google"
    elif "aws" in text.lower() or "amazon" in text.lower():
        issuer = "AWS"
    elif "guvi" in text.lower():
        issuer = "GUVI"
    elif "infosys" in text.lower():
        issuer = "Infosys"
        
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Find something that looks like a title
    title = f"Certificate {base_name}"
    # This is a very rough heuristic. It's often safer to just use a generic name
    # but we can try to find the longest line that isn't a name
    for line in lines:
        if len(line) > 10 and "certif" not in line.lower() and "kavya" not in line.lower():
            # Possible course name
            pass
            
    # Let's just use the filename for now, and the user can edit it in Admin.
    title = f"Certificate {idx - 99}"
    
    url = f"assets/certificates/{filename}"
    img_url = f"assets/certificates/{image_filename}"
    
    cert_obj = f"{{id:{idx},name:'{title}',issuer:'{issuer}',date:'2024',url:'{url}',emoji:'🏆',image:'{img_url}'}}"
    new_certs.append(cert_obj)
    idx += 1

certs_array_str = "certificates:[" + ",".join(new_certs) + "],"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find DEFAULTS certificates array
    content = re.sub(r'certificates:\s*\[.*?\],', certs_array_str, content, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file(admin_file)
update_file(index_file)

print(f"Processed {len(new_certs)} certificates successfully.")
