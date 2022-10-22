from flask import Flask, render_template , request

import ipapi

import speedtest


app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/', methods=['GET','POST'])
def home():
    
    
        
       

    

    if request.method == 'POST':
        
        ip = ipapi.location(output='ip')
        city = ipapi.location(output='city')

        spd = speedtest.Speedtest()
        spd.get_servers()
        spd.get_best_server()
        spd.download()
        spd.upload()
        res = spd.results.dict()
        download = round(res["download"]/1000000,2)
        upload = round(res["upload"]/1000000,2)
        ping = round(res["ping"])
        client = res["client"]["isp"]
        country = res["client"]["country"]
        
        print("finish")


        return render_template('index.html', ip = ip ,city=city, download=download, upload=upload,ping=ping,client=client)
    else:
        return render_template('index.html',ip="there is no place like 127.0.0.1", download=0, upload=0,ping=0,client="---",city="---")	

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=1234)
