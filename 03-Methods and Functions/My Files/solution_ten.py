def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

def myfunc(s):
  updated_s = ''
  for index,char in enumerate(s):
    if index % 2 == 0:
      updated_s += char.upper()
    else:
      updated_s += char.lower()
  
  return updated_s