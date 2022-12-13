from flask import Flask , render_template , request
import pickle
import numpy as np
import jinja2
app = Flask(__name__,template_folder='templates')
file = open("car_price.pkl","rb")
model = pickle.load(file)

@app.route('/',methods=["GET"])
def home():
    return render_template('index1.html')
    

@app.route('/predict',methods=["POST"])
def predict():
    
    if request.method == 'POST':
        symboling = int(request.form['symboling'])
        normalized_losses = int(request.form['normalized_losses'])
        make = request.form['make']
        if (make=="toyota"):
            make = 19
        elif (make=="nissan"):
            make = 12
        elif (make=="mazda"):
            make = 8
        elif (make=="mitsubishi"):
            make = 11
        elif (make=="honda"):
            make = 5
        elif (make=="volkswagen"):
            make = 20            
        elif (make=="subaru"):
            make = 18            
        elif (make=="peugot"):
            make = 13            
        elif (make=="vovlo"):
            make = 21            
        elif (make=="dodge"):
            make = 4            
        elif (make=="mercedes-benz"):
            make = 9            
        elif (make=="bmw"):
            make = 2            
        elif (make=="audi"):
            make = 1            
        elif (make=="plymouth"):
            make = 14            
        elif (make=="saab"):
            make = 17            
        elif (make=="porsche"): 
            make = 15            
        elif (make=="isuzu"):
            make = 6            
        elif (make=="jaguar"):
            make = 7            
        elif (make=="chevrolet"):
            make = 3            
        elif (make=="renault"):
            make = 16            
        elif (make=="alfa-romero"):
            make = 0            
        else:    
            make =10
        gas = (request.form['gas'])
        if(gas =='gas'):
            
            gas = 1
    
        else:
           
            gas=0
        aspiration = request.form['aspiration']
        if(aspiration=="std"):
            aspiration=0
        else:
            aspiration=1
        num_of_doors = request.form['num_of_doors']
        if(num_of_doors=="four"):
            num_of_doors=1
        else:
            num_of_doors=2
        body_style = request.form['body_style']
        if(body_style=="sedan"):
            body_style=3
        elif(body_style=="hatchback"):
            body_style=2
        elif(body_style=="wagon"):
            body_style=4
        elif(body_style=="hardtop"):
            body_style=1
        else:
            body_style=0
        drive_wheels = request.form["drive_wheels"]
        if(drive_wheels =='fwd'):
            drive_wheels=1
        elif(drive_wheels=='rwd'):
            drive_wheels = 2
        else:
            drive_wheels = 0
      
            
        
        engine_location = request.form['engine_location']
        if (engine_location=="front"):
             engine_location=0
        else:
            engine_location=1
        wheel_base = float(request.form['wheel_base'])
        length = float(request.form['length'])
        width = float(request.form['width'])
        height = float(request.form['height'])
        curb_weight = float(request.form['curb_weight'])
        engine_type = request.form['engine_type']
        if(engine_type=="ohc"):
            engine_type=3
        elif(engine_type=="ohcf"):
            engine_type=4
        elif(engine_type=="ohcv"):
            engine_type=5
        elif(engine_type=="l"):
            engine_type=2
        elif(engine_type=="dohc"):
            engine_type=0
        elif(engine_type=="rotor"):
            engine_type=6
        else:
            engine_type=1
        
        num_of_cylinders = request.form['num_of_cylinders']
        if (num_of_cylinders=="four"):
            num_of_cylinders=2
        elif (num_of_cylinders=="six"):
            num_of_cylinders=3
        elif (num_of_cylinders=="five"):
            num_of_cylinders=1
        elif (num_of_cylinders=="eight"):
            num_of_cylinders=0
        elif (num_of_cylinders=="two"):
            num_of_cylinders=6
        elif (num_of_cylinders=="three"):
            num_of_cylinders=4
        else:
            num_of_cylinders=5
        
        engine_size = int(request.form['engine_size'])
        fuel_system = int(request.form['fuel_system'])
        bore = int(request.form['bore'])
        stroke = int(request.form['stroke'])
        compression_ration = float(request.form['compression_ration'])
        horsepower = float(request.form['horsepower'])
        peak_rpm = float(request.form['peak_rpm'])
        highway_mpg= float(request.form['highway_mpg'])
        prediction = model.predict([[symboling,normalized_losses,gas,make, aspiration, num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width, height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore, stroke,compression_ration,horsepower,peak_rpm,highway_mpg]])
        output = round(prediction[0],13)
        if output < 0:
            return render_template('index1.html',pred='input error')
        else:
            pred="prediction of car price in dollars  {}".format(output)
            return render_template('index1.html',pred = pred)
    else:
        return render_template('index1.html')
if __name__ =="__main__":
    app.run(debug=True)
    