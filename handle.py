# ---coding:utf-8----
import os
import json
import setting

class Handle(object):
    # setting dir
    dir = setting.dir

    # 获取单词数据
    def fetch_word_data(self, word):
        try:
            with open(f'{setting.new_path}/words/{word}.json','r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return {'word': word}

    # 输出单词数据
    def trans(self, word):
        data = self.fetch_word_data(word)
        pronunciation = data.get('accent', '')
        means = data.get('mean_cn', '')
        sentence = data.get('sentence', '')
        sentence_trans = data.get('sentence_trans', '')
        return [('发音：',pronunciation,'\n释义：',means,'\n例句：',sentence,'\n例句翻译：',sentence_trans,),]

    def dic_ls(self):
        dic_list = os.listdir(self.dir)
        return dic_list

    # 获取字典内容(返回str)
    def dic_content(self, dic_name):
        dic_obj = open(self.dir + dic_name)
        try:
            dic_con = dic_obj.read()
        finally:
            dic_obj.close()
        return dic_con

    # 返回给定字典的英文LIST和中文翻译LIST
    def dic_cnlist(self, dic_name):
        dic_str = self.dic_content(dic_name)
        if dic_str[-1] == "\n":
            dic_str.rstrip("\n")
        en_list = dic_str.split('\n')
        cn_list = []
        for item in en_list:
            cn_t = self.trans(item)
            cn_str = "".join(cn_t[0])
            cn_word = cn_str.replace('\\n', '-------------------')
            cn_list.append(cn_word)
        return en_list, cn_list