# Naive-Bayes-classifier---text-classifier-
Use Naive Bayes classifier to classify text, categorize the movie review as positive or negative
用朴素贝叶斯 、 简单贝叶斯模型来分类影评 （电影评论） 为正面还是负面

tools: nltk, sklearn
lang: python

1. import the data - movie review
导入数据，电影评论
2. preprocess the data
预处理
3. split as train, vaid and test
分成训练、验证和测试集
4. shuffle those data randomly
随机排序，也即打乱数据集
5. some functions to extract features
写一些函数用于提取特征
6. train and predict
训练和测试

feature extraction:
1. collect all words and store their frequencies
2. sorting and ordering
3. choose the top (say) 20000 words that have the highest frequencies as a vector
4. generate the features for every movie review: one hot encoding
5. train the dataset and evaluate
6. input some typed strings to predict
特征提取：
收集所有的单词以及频率，
排序
选出排名最高前的一些，比如说20000个
对每个影评生成 独热编码
训练数据、评估
手动输入一些句子来测试


