from flask import Flask,render_template
 
FAI=Flask(__name__)

@FAI.route('/staticfile')

def staticfile():
    return render_template('static_file.html')

@FAI.route('/urlnav')

def htmlnav():
    return render_template('urlnav.html')

if __name__=='__main__':
    FAI.run(debug=True)    
    
