
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
import os
import requests
import json
import sys
import datetime, time
import pytz
app = Flask(__name__)

app.config["DEBUG"] = True


Info = []
@app.route('/a')
def hello_world():
    return 'Hello from Flask! kjhjj bjhkh'


@app.route('/wibble')
def wibble():
    return 'This is my pointless new page'


@app.route("/")
def index():
    return render_template("greet.html")

@app.route("/test", methods=["GET", "POST"])
def form():
    return render_template('greet.html')

@app.route('/form', methods=['GET', 'POST'])
def hello():
    to=request.form['to']
    say=request.form['say']
    if to != "":
        return render_template('greet.html', say=os.getcwd(), to=request.form['to'])



@app.route('/test1', methods=['GET', 'POST'])
def hellodc():

    return '''<!doctype html>
    <title>Upload new File</title>
    <div style="display: block;margin-right: auto;margin-left: auto;text-align:center;"> 
    </div><style>input {display: block;margin-right: auto;margin-left: auto;margin-top: 10px;width:80%;transition: 0.3s;}.asd{border: 5px solid #43dfc2;border-radius: 20px;height: 80px;padding-left: 5px;}.asd:hover{border: 5px dotted #38ff00;height: 90px;border-radius: 50px;}</style><form action="./upload" method=post enctype=multipart/form-data><div> <input oninput="var location =document.forms[0].elements['link'].value;document.forms[0].elements['name'].value=decodeURIComponent(location.substr(location.lastIndexOf('/')+1));" name="link" class="asd" id="link" value="link" ><input class="asd" name="name" id="name" value="name" ></div><input  style="height: 90px;padding: 10px;background: #cad76d;border-radius: 50px;width: 250px;cursor: pointer;" type=submit value=Upload></form>
    '''

#@app.route('/upload',methods = ['GET','POST'])
#def upload_file():
#    if request.method =='POST':
#        file = request.files['file']
#        file.save(file.filename)
#    return 'okkkkkkkk'

@app.route('/upload',methods = ['GET','POST'])
def upload_file():
    if (request.method =='POST' or request.method == 'GET'):
        namev =request.form['name']
        url=request.form['link']

        #mshh = 'Download started at \n'+str(datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S %f"))
        #url21x = 'https://api.telegram.org/bot1354851134:AAHuF0FP2TlHkpH1S8uAT3FA0NEhC3UhFtk/sendMessage?chat_id=-1001268605608&text=' + mshh + '&parse_mode=Markdown'
        #requests.get(url21x)

        #ppath = os.path.join('/home/frjhgu/mysite/uploads/',namev)
        t0 = time.time()
        r = requests.get(url)
        t1 = time.time()
        size443re=sys.getsizeof(r.content)/1000000
        #mshh = 'Download finshed at \n'+str(datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S %f"))+'\n Dowmload speed: _'+str(round(size443re/(t1-t0), 3))+'_ Mb/s'
        # url21x = 'https://api.telegram.org/bot1354851134:AAHuF0FP2TlHkpH1S8uAT3FA0NEhC3UhFtk/sendMessage?chat_id=-1001268605608&text=' + mshh + '&parse_mode=Markdown'
        # requests.get(url21x)
        if namev:
            #f = open(ppath, 'wb')
            #f.write(r.content)
            sample_file = r.content
            #mshh = 'Uploading '+ str(sys.getsizeof(sample_file)/1000000) +' Mb started at \n'+str(datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S %f"))
            #url21x = 'https://api.telegram.org/bot1354851134:AAHuF0FP2TlHkpH1S8uAT3FA0NEhC3UhFtk/sendMessage?chat_id=-1001268605608&text=' + mshh + '&parse_mode=Markdown'
            #requests.get(url21x)
            t0 = time.time()
            upload_file = {"file": (namev ,sample_file)}
            urll= 'https://bot.sapp.ir/wUhqub6FyG0ZiPVLkYX33GCI2zz292xb6tyu7-zxB9th8Lw3wCzLyNA9fO0NFvxNtfoYZXGMlU0879Vus1tgMXd0oLomLa3MUdosd3V-ouRv5AwVuXkJ7GrJPumxq5S_u5VeUzlVic5eDrJ0/uploadFile'
            r1 = requests.post(urll, files = upload_file)
            t1 = time.time()
            x =  r1.text
            y = json.loads(x)
            furl=y["fileUrl"]
            urlsu = "https://bot.sapp.ir/JzdoVqPnRb7rn032wT29fZvNOZUCXX3pR4xp9HFWh0bkQ_8Qtw8j_L9zKZtxEBB3-HiJJjD6W423CyzbhvfHYtLdUpBgN0AXjdlACFTVhmkGNx2aj3VR7-3NghnkQLV3jzolToUeLWalQSLv/sendMessage"
            data = {
                "to": "Ke39LIXbMYNlfSwyBk6vK6Rd8kljthh9ef34khcZiYmbWxX3vrbyDWw95xY",
                "type": "FILE",
                "body": str(datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S %f")),
                "time": "1538399819589",
                "fileName": namev,
                "fileType": "FILE_TYPE_OTHER",
                "fileSize": sys.getsizeof(sample_file),
                "fileUrl": furl
                }

            data1 = {
                "to": "NZv2fcsrfKXULnb14EM_rgcln1WwPl5EivL0Jz_WhALVEWSPxPY3ClJ2GiI",
                "type": "FILE",
                "body": str(datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S %f")),
                "time": "1538399819589",
                "fileName": namev,
                "fileType": "FILE_TYPE_OTHER",
                "fileSize": sys.getsizeof(sample_file),
                "fileUrl": furl
                }
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            r4 = requests.post(urlsu, data=json.dumps(data1), headers=headers)
            r3 = requests.post(urlsu, data=json.dumps(data), headers=headers)
            #url21 = 'https://api.telegram.org/bot1354851134:AAHuF0FP2TlHkpH1S8uAT3FA0NEhC3UhFtk/sendMessage?chat_id=-1001268605608&text=%D9%81%D8%A7%DB%8C%D9%84+%D8%B4%D9%85%D8%A7+%D8%A8%D8%A7+%D9%85%D9%88%D9%81%D9%82%DB%8C%D8%AA+%D8%A7%D8%B1%D8%B3%D8%A7%D9%84+%D8%B4%D8%AF' + '\n نام فایل:' + namev +'\n' + str(datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S %f")) +'\n Upload speed:'+str(round(size443re/(t1-t0), 3))+' Mb/s'+'&parse_mode=Markdown'
            #ttr = requests.get(url21)
            #filename = 'yuyu'
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template('greet.html', say=r3.text, to=sys.getsizeof(sample_file))
    return 'okkkkkkkk'

@app.route('/apaupload',methods = ['GET','POST'])
def upload_filetoaparat():
    if (request.method =='POST'):
        url=request.form['link']
        foo=request.form['foo']
        descr=request.form['data[descr]']
        tags=request.form['data[tags]']
        category=request.form['data[category]']
        title=request.form['data[title]']
        r = requests.get(url)
        sample_file = r.content
        r1 = requests.get('https://www.aparat.com/etc/api/uploadform/luser/drassat/ltoken/b067158e925e3d66f6753dab558db550')
        x =  r1.text
        y = json.loads(x)
        furl=y['uploadform']['frm-id']
        faction=y['uploadform']['formAction']

        if foo=='true':
            datas = {
            "frm-id":furl,"data[title]":title,
            "data[category]":category,"data[tags]":tags,"data[descr]":descr,
            "data[video_pass]":'true'}
        else:
            datas={
            "frm-id":furl,"data[title]":title,
            "data[category]":category,
            "data[tags]":tags,
            "data[descr]":descr,
            "data[video_pass]":'false'}
        files={'video': ('video.mp4', sample_file, 'video/mp4')}
        r7 = requests.post(faction, files=files, data=datas)
        return render_template('greet.html', say=r7.text, to=sys.getsizeof(sample_file))

@app.route('/apaupper', methods=['GET', 'POST'])
def helnnnnlodc():

    return '''

	<!doctype html>
    <title>Upload new File</title>
    <div style="display: block;margin-right: auto;margin-left: auto;text-align:center;"> 
 </div><style>
	input:not([type="radio"]) ,select  {text-align: center;display: block;margin-right: auto;margin-left: auto;margin-top: 10px;width:80%;transition: 0.3s;}.asd{border: 5px solid #43dfc2;border-radius: 20px;height: 80px;padding-left: 5px;}.asd:hover{border: 5px dotted #38ff00;height: 90px;border-radius: 50px;}
	.asdf ,textarea {
 text-align: right;
 display: block;
 margin-right: auto;
 margin-left: auto;
 margin-top: 10px;
 width:80%;

    padding-left: 5px;
}

</style>


<form action="./apaupload" method=post enctype=multipart/form-data  id="apaform"><div>


<input  name="link" class="asd" id="link"  placeholder="لینک ویدیو" >

<input class="asd" name="data[title]" id="name" placeholder="عنوان ویدیو" >
<span class="asdf">: دسته‌بندی آپارات</span>
<select class="asd" name="data[category]"  form="apaform">
<option value="22">گیم</option><option value="21">سلامت</option><option value="20">بانوان</option><option value="18">کارتون</option><option value="17">هنری</option><option value="16">تبلیغات</option><option value="15">متفرقه</option><option value="14">حیوانات</option><option value="13">گردشگری</option><option value="12">حوادث</option><option value="11">ورزشی</option><option value="10">علم و تکنولوژی</option><option value="9">سیاسی</option><option value="8">خبری</option><option value="7">موسیقی</option><option value="6">مذهبی</option><option value="5">فیلم</option><option value="4">تفریحی</option><option value="3">آموزشی</option><option value="2">طنز</option>
</select>
<span class="asdf">برچسب‌های ویدیو (اجباری - حداقل سه مورد) که با - از هم جدا میشوند</span>
<input class="asd" name="data[tags]" id="name" placeholder="برچسب1 - برچسب2" >
<span class="asdf">:توضیحات ویدیو</span>
 <textarea class="asd" id="subject" name="data[descr]" placeholder="..... توضیحات ویدیو
" style="height:200px"></textarea>

</div>
<span class="asdf">لینک پروکسی نشود؟
<input type="radio" id="myRadio">بله<br><input type="radio"  >نه</span>
<button type="submit" class="like" name="foo" value="false" style="height: 90px;padding: 10px;background: #6f7285;border-radius: 50px;width: 250px;cursor: pointer;">ذخیره، بعدا منتشر میکنم</button>
<button type="submit" class="like" name="foo" value="true" style="height: 90px;padding: 10px;background:#df0f50;border-radius: 50px;width: 250px;cursor: pointer;" >انتشار ویدیو</button>

</form>

    '''

