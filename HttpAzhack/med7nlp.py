import spacy

def med7nlp1(text):

    med7 = spacy.load("en_core_med7_lg")

    doc = med7(text)

    r = []

    for ent in doc.ents:
        if ent.label_ == 'DRUG' or ent.label_ == 'STRENGTH':
            r.append([ent.text, ent.label_])

    if r == []:
        return None

    n = len(r)

    res = []
    res2 = []
    for i in range(1,n):
        if r[i][1] == 'STRENGTH' and r[i-1][1] == 'DRUG' and r[i-1][0] not in res:
            res.append(r[i - 1][0])
            res2.append(r[i][0])

    res3 = []
    for s in res2:
        for n in s.split():
            try:
                if str(int(float(n))).isdigit():
                    res3.append(int(float(n)))
            except:
                pass

    mg = str(max(res3))
    tab_name = res[res3.index(max(res3))]
    
    if tab_name[-2:] == "IP":
        tab_name = tab_name[:-2]
    
    return str(tab_name.strip())
