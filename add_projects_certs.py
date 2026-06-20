import urllib.request
import json
import re
import os

url = "https://api.github.com/users/kavyapingale022-source/repos"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req)
    repos = json.loads(response.read().decode('utf-8'))
except Exception as e:
    print("Failed to fetch repos:", e)
    repos = []

proj_objects = []
idx = 1
for repo in repos:
    name = repo.get("name", "").replace("'", "\\'")
    desc = repo.get("description", "A project by Kavya")
    if not desc:
        desc = "A project by Kavya"
    desc = desc.replace("'", "\\'")
    live = repo.get("homepage", "")
    github = repo.get("html_url", "")
    emoji = "🚀"
    
    proj_str = f"{{id:{idx},title:'{name}',description:'{desc}',github:'{github}',live:'{live}',emoji:'{emoji}',tags:[]}}"
    proj_objects.append(proj_str)
    idx += 1

projects_array_str = "projects:[" + ",".join(proj_objects) + "],"

base_dir = "c:/Users/KAVYA/Downloads/WEBSITES/Portfolio Website"
admin_file = os.path.join(base_dir, "admin.html")
index_file = os.path.join(base_dir, "index.html")

# 1. Update admin.html
with open(admin_file, 'r', encoding='utf-8') as f:
    admin_content = f.read()

# Update projects DEFAULTS
admin_content = re.sub(r'projects:\s*\[\s*\],', projects_array_str, admin_content)

# Update cert-modal
cert_modal_find = r'<div class="form-group"><label class="form-label">Emoji Icon</label><input class="form-input" id="ct-emoji" placeholder="🏆"></div>'
cert_modal_replace = cert_modal_find + '\n      <div class="form-group"><label class="form-label">Image URL</label><input class="form-input" id="ct-image" placeholder="https://…/cert.png"></div>'
admin_content = admin_content.replace(cert_modal_find, cert_modal_replace)

# Update openCertModal
open_cert_find = r"if(id){ const c=D.certificates.find(x=>x.id===id)||{}; document.getElementById('ct-name').value=c.name||''; document.getElementById('ct-issuer').value=c.issuer||''; document.getElementById('ct-date').value=c.date||''; document.getElementById('ct-url').value=c.url||''; document.getElementById('ct-emoji').value=c.emoji||''; }"
open_cert_replace = r"if(id){ const c=D.certificates.find(x=>x.id===id)||{}; document.getElementById('ct-name').value=c.name||''; document.getElementById('ct-issuer').value=c.issuer||''; document.getElementById('ct-date').value=c.date||''; document.getElementById('ct-url').value=c.url||''; document.getElementById('ct-emoji').value=c.emoji||''; document.getElementById('ct-image').value=c.image||''; }"
admin_content = admin_content.replace(open_cert_find, open_cert_replace)

open_cert_find2 = r"else   { ['ct-name','ct-issuer','ct-date','ct-url','ct-emoji'].forEach(i=>document.getElementById(i).value=''); }"
open_cert_replace2 = r"else   { ['ct-name','ct-issuer','ct-date','ct-url','ct-emoji','ct-image'].forEach(i=>document.getElementById(i).value=''); }"
admin_content = admin_content.replace(open_cert_find2, open_cert_replace2)

# Update saveCert
save_cert_find = r"const obj={name:document.getElementById('ct-name').value.trim(),issuer:document.getElementById('ct-issuer').value.trim(),date:document.getElementById('ct-date').value.trim(),url:document.getElementById('ct-url').value.trim(),emoji:document.getElementById('ct-emoji').value.trim()};"
save_cert_replace = r"const obj={name:document.getElementById('ct-name').value.trim(),issuer:document.getElementById('ct-issuer').value.trim(),date:document.getElementById('ct-date').value.trim(),url:document.getElementById('ct-url').value.trim(),emoji:document.getElementById('ct-emoji').value.trim(),image:document.getElementById('ct-image').value.trim()};"
admin_content = admin_content.replace(save_cert_find, save_cert_replace)

with open(admin_file, 'w', encoding='utf-8') as f:
    f.write(admin_content)


# 2. Update index.html
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Update projects DEFAULTS
index_content = re.sub(r'projects:\s*\[\s*\],', projects_array_str, index_content)

# Render certs with image
render_cert_find = r'<div class="cert-icon">${c.emoji||\'🏆\'}</div>'
render_cert_replace = r'<div class="cert-icon">${c.image?`<img src="${c.image}" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;" alt="cert">`:c.emoji||\'🏆\'}</div>'
index_content = index_content.replace(render_cert_find, render_cert_replace)

# Remove hardcoded HTML from proj-container
index_content = re.sub(r'(<div class="grid-3" id="proj-container">)(.*?)(</div>\s*</div>\s*</section>)', r'\1\3', index_content, flags=re.DOTALL)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Successfully updated admin.html and index.html")
