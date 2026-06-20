import urllib.request
import json
import re

url = "https://api.github.com/users/kavyapingale022-source/repos"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
repos = json.loads(response.read().decode('utf-8'))

html_file = "c:/Users/KAVYA/Downloads/WEBSITES/Portfolio Website/index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

projects_html = ""
for repo in repos:
    name = repo.get("name", "")
    description = repo.get("description", "A project by Kavya")
    homepage = repo.get("homepage", "")
    html_url = repo.get("html_url", "")
    
    if not description:
        description = "A project by Kavya"
        
    demo_link = f'<a href="{homepage}" target="_blank" rel="noopener noreferrer" class="proj-link"><i class="fas fa-external-link-alt"></i> Live Demo</a>' if homepage else ''
    
    projects_html += f'''
        <div class="proj-card">
          <div class="proj-thumb">
            <div class="proj-emoji-placeholder">🚀</div>
          </div>
          <div class="proj-content">
            <h3 class="proj-title">{name}</h3>
            <p class="proj-desc">{description}</p>
            <div class="proj-links">
              {demo_link}
              <a href="{html_url}" target="_blank" rel="noopener noreferrer" class="proj-link"><i class="fab fa-github"></i> GitHub</a>
            </div>
          </div>
        </div>
'''

pattern = re.compile(r'(<div class="grid-3" id="proj-container">)(.*?)(</div>)', re.DOTALL)

if pattern.search(content):
    new_content = pattern.sub(r'\1\n' + projects_html + r'\n\3', content)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Portfolio updated successfully with GitHub projects.")
else:
    print("Could not find proj-container in index.html")
