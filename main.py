# ---coding:utf-8----
from flask import Flask, render_template, request
from handle import Handle

app = Flask(__name__)

handles = Handle()

@app.route('/', methods=['POST', 'GET'])
def index():
    dic_list = handles.dic_ls()
    if request.method == 'GET':
        dic_con = handles.dic_content(dic_list[0])
        return render_template("index.html", dic_list=dic_list, dic_con=dic_con, dic_sele=dic_list[0])

    if request.method == 'POST':
        dic_name = request.form['dic_name']
        dic_con = handles.dic_content(dic_name)
        return render_template("index.html", dic_list=dic_list, dic_con=dic_con, dic_sele=dic_name)

@app.route('/study', methods=['POST', 'GET'])
def study():
    if request.method == 'POST':
        dic_name = request.form['dic_sele']
        en_list, cn_list = handles.dic_cnlist(dic_name)

        us_audio_links = ["http://dict.youdao.com/dictvoice?type=0&audio=" + word for word in en_list]

        return render_template('study.html', dic_name=dic_name, en_list=en_list, cn_list=cn_list, n=len(en_list), us_audio_links=us_audio_links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')