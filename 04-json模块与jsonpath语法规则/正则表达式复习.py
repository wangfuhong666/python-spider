import re
text="1aaa_234  678\t9\n"
print(re.findall(r"a{0,2}", text))