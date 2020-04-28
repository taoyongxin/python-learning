"""
中文文本的情感分析
@Date 2020.04.28
pip3 install snownlp
"""

from snownlp import SnowNLP

text = '人们日常所犯最大的错误，是对陌生人太客气，而对亲密的人太苛刻了，而努力改掉这个习惯。'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断，返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
text1 = '这部电影太棒了'
text2 = '这部电影简直是烂到爆'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
# 这部电影太棒了 0.9829468270441747
print(text1, s1.sentiments)
# 这部电影简直是烂到爆 0.2296519477554504
print(text2, s2.sentiments)

# 关键字抽取
text3 = '中华民族是一个伟大的民族，爱国主义精神是我们这个民族最美的花朵。\
    爱国，是一个神圣的字眼，在历史发展的曲折过程中，爱国主义历来是我国人民所崇尚的。'
s3 = SnowNLP(text3)
print(s3.keywords(limit=5))
#['爱国主义', '民族', '一个', '美', '精神']
s3 = SnowNLP(text3)
print(s3.summary(limit=4))
# ['中华民族是一个伟大的民族', '爱国主义精神是我们这个民族最美的花朵',
#  '是一个神圣的字眼', '爱国主义历来是我国人民所崇尚的']
