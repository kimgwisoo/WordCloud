from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

text = "파이썬 워드클라우드 파이썬 좋아 워드클라우드 파이썬 라이브러리 좋아 파이썬 워드클라우드 예시 워드클라우드 우한 폐렴 조심 데이터 분석 우한 워드클라우드 중국 박쥐 감염 코로나 바이러스"
text2 = "Python WordCloud Python like WordCloud Python library like Python WordCloud example WordCloud Wuhan Pneumonia Be Careful Data analysis Wuhan WordCloud China bat infection COVID-19"
text3 = "파이썬 워드클라우드 Python 좋아 WordCloud 파이썬 library like 파이썬 WordCloud 예시 워드클라우드 Wuhan Pneumonia 조심 DATA analysis 우한 워드클라우드 China Bat infection 코로나 바이러스"

'''
font_path : 한글의 경우 깨지지 않게 폰트 경로 지정
background_color : 백그라운드 색 지정
stopwords : 불용어 지정
'''
stopwords = set(STOPWORDS)
stopwords.add('워드클라우드')
wordcloud = WordCloud(font_path='font/NanumGothic.ttf',
                      stopwords=stopwords,
                      background_color='white').generate(text3)

plt.figure(figsize=(22, 22))
plt.imshow(wordcloud, interpolation='lanczos')
plt.axis('off')
plt.show()
plt.savefig()
