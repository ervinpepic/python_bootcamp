from bs4 import BeautifulSoup

with open(file="website.html") as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.string)
# print(soup.a)
anchors = soup.find_all(name="a")
for tag in anchors:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
company_CEO_name = soup.select_one(selector="#name")
print(company_url)
print(company_CEO_name)
heading_class = soup.select(".heading")
print(heading_class)

print(soup.select("ul li"))