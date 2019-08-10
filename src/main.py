def main():
    print('tt')

    with open ('../template.html') as f:
        t=f.read()
        print(t)


    with open('dictionary.csv',encoding="shift-jis") as f:
        s = f.read()
        print(s)
    ss =s.split('\n')
    words = []
    for line in ss:
        parts = line.split(',')
        if not parts[0]:
            continue
        if parts[0]=='index':
            continue
        word = parts[1]
        words.append(word)
        pro = parts[3]
        if not pro:
            break
        meaning =parts[4]
        meaning=addLink(meaning,words)
        createHtml(t,word,pro,meaning)
    print(words)



    
def addLink(meaning,words):
    for word in words:
        if word in meaning:
            link='<a href={word}.html>{word}</a>'.format(word=word)
            meaning=meaning.replace(word,link)
    return meaning




def createHtml(t,word,pro,meaning):
    with open ('../word/{word}.html'.format(word=word),'w') as f:
        html = t.format(word=word,pro=pro,meaning=meaning)
        f.write(html)
    


if __name__ == '__main__':
    main()
