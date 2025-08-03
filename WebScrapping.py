from bs4 import BeautifulSoup
html = "<html><body><h1>Title</h1></body></html>"  # Example HTML
tag = "h1"  # Example tag
soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())
print(soup.find(tag))
print(soup.find_all(tag))