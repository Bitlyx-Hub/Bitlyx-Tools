import os
import markdown

if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    html_content = markdown.markdown(markdown_content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Successfully converted README.md to index.html")
else:
    print("README.md file not found")
