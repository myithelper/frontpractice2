import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import argparse

def main():
    parser = argparse.ArgumentParser(description='dictionary parameteres')
    parser.add_argument('--m', type=int, default=0)
    parser.add_argument('--n', type=int, default=0)
    m= parser.parse_args().m
    n=parser.parse_args().n
    downDict()

    with open('../word/template.html') as f:
        t = f.read()

    df = pd.read_excel('./dictionary.xlsx', sheet_name='dictionary', header=0)
    print(df)

    df = df.dropna(axis=0)
    if n>0:
        df=df[m:n]
    print(df)

    words = []
    infos = []
    for idx, row in df.iterrows():
        words.append(row.word)
        infos.append([row.word, row.pronouncation, row.meaning])

    words.reverse()
    print(infos)
    for i in range(len(infos)):
        if i == 0:
            createHtml(t, infos[i][0], infos[i][1], infos[i]
                       [2], words, infos[i+1][0], '#')
        elif i < len(infos)-1:

            createHtml(t, infos[i][0], infos[i][1], infos[i]
                       [2], words, infos[i+1][0], infos[i-1][0])
        else:

            createHtml(t, infos[i][0], infos[i][1], infos[i]
                       [2], words, '#', infos[i-1][0])


def addLink(word, words):
    done = []
    for w in words:
        if w in word and w != word:
            flag = False
            for d in done:
                if w in d:
                    flag = True
            if flag:
                continue
            link = '<a href={w}.html>{w}</a>'.format(w=w)
            word = word.replace(w, link)
            done.append(w)
    return word


def createHtml(t, word, pro, meaning, words, word_next, word_before):
    with open('../word/{word}.html'.format(word=word), 'w') as f:
        word_link = addLink(word, words)
        html = t.replace('{word}', word).replace('{pro}', pro).replace(
            '{meaning}', meaning).replace('{word_link}', word_link)
        if word_next:
            html = html.replace('{word_next}', word_next)
            html = html.replace('{word_before}', word_before)

        f.write(html)


def downDict():
    with open ('./fileid.txt') as f:
        id = f.read()

    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)

    # 指定したIDのデータをダウンロード
    file3 = drive.CreateFile({'id': id})
    file3.GetContentFile('dictionary.xlsx','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')



    
    


if __name__ == '__main__':
    main()
