def main():
    print('tt')
    space = '	'

    with open ('../word/template.html') as f:
        t=f.read()
        print(t)


    with open('dictionary.txt',encoding="utf-16") as f:
        s = f.read()
        print(s)
    ss =s.split('\n')
    words = []
    infos=[]
    for i in range(len(ss)):
        line = ss[i]
        parts = line.split(space)
        #parts = line.split('	')

        
        if parts[0]=='index':
            continue

        pro = parts[4]
        if not pro:
            continue
        word = parts[2]
        words.append(word)
        meaning =parts[5]
        infos.append([word,pro,meaning])



    words.reverse()        
    print('aaaaaaaaaaaaaaaaaaaaa')
    print(words)
    print('bbbbbbbbbbbbbbbbbbb')
    print(infos)
    for i in range(len(infos)):
        if i==0:
            print('hh')
            createHtml(t,infos[i][0],infos[i][1],infos[i][2],words,infos[i+1][0],'#')
        elif i <len(infos)-1:

            createHtml(t,infos[i][0],infos[i][1],infos[i][2],words,infos[i+1][0],infos[i-1][0])
        else:

            createHtml(t,infos[i][0],infos[i][1],infos[i][2],words,'#',infos[i-1][0])




               
def addLink(word,words):
    done=[]
    for w in words:
        if w in word and w!=word:
            flag=False
            for d in done:
                if w in d:
                    flag=True
            if flag:
                continue
            link='<a href={w}.html>{w}</a>'.format(w=w)
            word=word.replace(w,link)
            done.append(w)
    return word




def createHtml(t,word,pro,meaning,words,word_next,word_before):
    with open ('../word/{word}.html'.format(word=word),'w') as f:
        word_link=addLink(word,words)
        html = t.replace('{word}',word).replace('{pro}',pro).replace('{meaning}',meaning).replace('{word_link}',word_link)
        if word_next:
            html = html.replace('{word_next}',word_next)
            html = html.replace('{word_before}',word_before)
       
        f.write(html)
    


if __name__ == '__main__':
    main()
