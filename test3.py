
features= {'methods':["Method"],'typ':["Content-Type"],'conLen':["Content-Length"],'host':["Host"]}

t="application/x-www-form-urlencoded"
#usual kinds of Content-Type
typ=["application/x-www-form-urlencoded",]
host=["apple","ball","vat","dog"]

def search(searchFor):
    for k in features:
        for v in features[k]:
            if searchFor in v:
                return k
    return None

mka='Host'

print eval(search(mka)).index('apple')
