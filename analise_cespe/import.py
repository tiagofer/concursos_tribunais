import textract
import re
import pandas as pd

arr=list()
text = textract.process("tre_al_2004_cespe.PDF", encoding="ascii")
text = str(text)
arr = re.split(r'[1,3].+',text)
#arr = text.split(r'\\n')
result = list()
print(len(result))
print(arr)
df = pd.DataFrame(arr)
df.to_csv('df.csv')
