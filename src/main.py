def main():
    print('tt')

    with open ('../word/template.html') as f:
        t=f.read()
        print(t)


    with open('dictionary.csv',encoding="shift-jis") as f:
        s = f.read()
        print(s)
    ss =s.split('\n')
    words = []
    for i in range(len(ss)):
        line = ss[i]
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
        if i<len(ss)-1:
            word_next=ss[i+1].split(',')[1]
            createHtml(t,word,pro,meaning,word_next)
        else:
            createHtml(t,word,pro,meaning,'')

    print(words)



    
def addLink(meaning,words):
    for word in words:
        if word in meaning:
            link='<a href={word}.html>{word}</a>'.format(word=word)
            meaning=meaning.replace(word,link)
    return meaning




def createHtml(t,word,pro,meaning,word_next):
    with open ('../word/{word}.html'.format(word=word),'w') as f:
        html = t.replace('{word}',word).replace('{pro}',pro).replace('{meaning}',meaning)
        if word_next:
            html = html.replace('{word_next}',word_next)
        f.write(html)
    


if __name__ == '__main__':
    main()
