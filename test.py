splitter = 1
str_ = 'unbenannt.png28.png'
mat = re.match(f'unbenannt\.png\d{{splitter}}\.png$', str_)

mat = re.match('unbenannt\.png\d{'+str(splitter)+'}\.png$', str_)
