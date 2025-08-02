import re
file_path = "./docs/web/nodejs.md"
regex = r'examples/nodejs/jss/[\w\.]+\.js'
def add_brackets_to_match(doc):
    # 定义正则表达式，这里我们假设"*.html"部分代表任意单个单词字符（\w）和点（\.)
    
    # 使用re.sub()函数进行替换操作，将匹配项前后添加中括号
    new_doc = re.sub(regex, r'[\g<0>]', doc, flags=re.IGNORECASE)
    
    return new_doc

# 示例文档
with open(file_path, "r", encoding="utf-8") as file:
  doc = file.read()
  print(len(doc))

# 执行替换操作
new_doc = add_brackets_to_match(doc)


regex = re.compile(regex, re.IGNORECASE)
    
# 使用findall获取所有匹配项
matches = regex.findall(doc)
print(len(matches))
new_doc += "\n\n\n"
for i in matches:
   new_doc += f"[{i}]: https://github.com/everythingfades/html/blob/main/{i}\n"
with open(file_path, "w", encoding="utf-8") as file:
  file.write(new_doc)