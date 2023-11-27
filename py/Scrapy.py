import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def save_content_to_file(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def save_website_resources(url, folder_name):
    response = requests.get(url)
    html_content = response.text
    create_folder_if_not_exists(folder_name)
    html_file_path = os.path.join(folder_name, 'index.html')
    save_content_to_file(html_content, html_file_path)
    soup = BeautifulSoup(html_content, 'html.parser')
    for link_tag in soup.find_all('link', {'rel': 'stylesheet'}):
        css_url = link_tag.get('href')
        if css_url and not css_url.startswith(('http:', 'https:')):
            css_url = urljoin(url, css_url)
        css_content = requests.get(css_url).text
        css_file_path = os.path.join(folder_name, 'style.css')
        save_content_to_file(css_content, css_file_path)
    for style_tag in soup.find_all('style'):
        css_content = style_tag.get_text()
        css_file_path = os.path.join(folder_name, 'style_inline.css')
        save_content_to_file(css_content, css_file_path)
    for script_tag in soup.find_all('script', {'src': True}):
        js_url = script_tag.get('src')
        if js_url and not js_url.startswith(('http:', 'https:')):
            js_url = urljoin(url, js_url)
        js_content = requests.get(js_url).text
        js_file_path = os.path.join(folder_name, 'script.js')
        save_content_to_file(js_content, js_file_path)
logo = """
\033[38;5;6m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;46m███████  ██████ ██████   █████  ██████        ██   ██ 
\x1b[38;5;46m██      ██      ██   ██ ██   ██ ██   ██        ██ ██  
\x1b[38;5;46m███████ ██      ██████  ███████ ██████  █████   ███   
\x1b[38;5;46m     ██ ██      ██   ██ ██   ██ ██             ██ ██  
\x1b[38;5;46m███████  ██████ ██   ██ ██   ██ ██            ██   ██ 
\033[38;5;6m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
def main():
    os.system('clear')
    print(logo)
    website_url = input("[=]>> ENTER WEBSITE URL : ")
    print("\033[38;5;6m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    folder_name = input("[=]>> ENTER FOLDER NAME : ")
    print("\033[38;5;6m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\x1b[38;5;46m[=]> LOADING....")
    save_website_resources(website_url, folder_name)
    print(f"[=]> DATA SAVED TO : {folder_name}")
main()
