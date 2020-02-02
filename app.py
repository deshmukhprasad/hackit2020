from flask import Flask, request 
import gzip, io, requests, os,csv,sys
import pandas as pd
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/temp/', methods= ['POST']) 
# ‘/’ URL is bound with hello_world() function. 
def temp(): 
    
    file = request.files['archive']
    # print(gzip.decompress(file))
    file.save('/file1.csv')
    file.save('/file1.txt.gz')
    statinfo = os.stat('/file1.txt.gz')
    print("Compressed File size : ",statinfo.st_size)
    with open('/file1.csv', 'rb') as fd:
        gzip_fd = gzip.GzipFile(fileobj=fd)
        destinations = pd.read_csv(gzip_fd)
        tp_content1 = destinations.to_csv(
      sep=',',
      header=False,
      index=False,
      quoting=csv.QUOTE_ALL,
      quotechar='"',
      doublequote=True,
      line_terminator='\n')
    
    with open('/odfile1.csv', 'a') as od1:
        od1.write(tp_content1)

 
    return "sdf"
    # return file

@app.route('/water/', methods= ['POST']) 
# ‘/’ URL is bound with hello_world() function. 
def water(): 
    
    file = request.files['archive']
    # print(gzip.decompress(file))
    file.save('/file2.csv')
    file.save('/file2.txt.gz')
    statinfo = os.stat('/file2.txt.gz')
    print("Compressed File size : ",statinfo.st_size)
    
    with open('/file2.csv', 'rb') as fd2:
        gzip_fd2 = gzip.GzipFile(fileobj=fd2)
        destinations = pd.read_csv(gzip_fd2)
        tp_content2 = destinations.to_csv(
      sep=',',
      header=False,
      index=False,
      quoting=csv.QUOTE_ALL,
      quotechar='"',
      doublequote=True,
      line_terminator='\n')
    
    with open('/odfile2.csv', 'a') as od2:
        od2.write(tp_content2)
    #f=gzip.open('/home/ravi/file2.txt.gz','rb')
    #file_content=f.read()
    #print(file_content)
    return "sdf"
    # return file  
# main driver function 
if __name__ == '__main__':  
    app.run() 