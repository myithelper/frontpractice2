def main():
    print('tt')

    with open ('../template.html') as f:
        t=f.read()
        print(t)


    with open('dictionary.csv',encoding="shift-jis") as f:
        s = f.read()
        print(s)
    ss =s.split('\n')
    print(ss)
    print(ss[1])
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
        createHtml(t,word,pro,meaning)
    print(words)



        

def createHtml(t,word,pro,meaning):
    with open ('../word/{word}.html'.format(word=word),'w') as f:
        html = t.format(word=word,pro=pro,meaning=meaning)
        f.write(html)
    


if __name__ == '__main__':
    main()
