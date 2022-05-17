from flask import Flask, render_template, request
# import jsonify
# import requests
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    reg_model = pickle.load(open('GradientBooster.pkl', 'rb'))
    if request.method == 'POST':

        #Numerical Variables
        tmpf = float(request.form['tmpf'])
        dwpf = float(request.form['dwpf'])
        relh = float(request.form['relh'])
        drct = float(request.form['drct'])
        sknt = float(request.form['sknt'])
        alti = float(request.form['alti'])
        vsby = float(request.form['vsby'])
        skyl1 =float( request.form['skyl1'])
        feel = float(request.form['feel'])

        #Categorical Variables
        Sky_Coverage = request.form['skyc1']
        if(Sky_Coverage == 'BKN'):
            skyc1_BKN, skyc1_FEW, skyc1_NSC, skyc1_OVC, skyc1_SCT, skyc1_VV = 1,0,0,0,0,0
        elif(Sky_Coverage == 'FEW'):
            skyc1_BKN, skyc1_FEW, skyc1_NSC, skyc1_OVC, skyc1_SCT, skyc1_VV = 0,1,0,0,0,0
        elif(Sky_Coverage == 'NSC'):
            skyc1_BKN, skyc1_FEW, skyc1_NSC, skyc1_OVC, skyc1_SCT, skyc1_VV = 0,0,1,0,0,0
        elif(Sky_Coverage == 'OVC'):
            skyc1_BKN, skyc1_FEW, skyc1_NSC, skyc1_OVC, skyc1_SCT, skyc1_VV = 0,0,0,1,0,0
        elif(Sky_Coverage == 'SCT'):
            skyc1_BKN, skyc1_FEW, skyc1_NSC, skyc1_OVC, skyc1_SCT, skyc1_VV = 0,0,0,0,1,0
        else:
            skyc1_BKN, skyc1_FEW, skyc1_NSC, skyc1_OVC, skyc1_SCT, skyc1_VV = 0,0,0,0,0,1
        
        Month = request.form['month']
        if(Month == 'January'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 1,0,0,0,0,0,0,0,0,0,0,0
        elif(Month == 'February'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,1,0,0,0,0,0,0,0,0,0,0
        elif(Month == 'March'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,1,0,0,0,0,0,0,0,0,0
        elif(Month == 'April'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,1,0,0,0,0,0,0,0,0
        elif(Month == 'May'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,1,0,0,0,0,0,0,0
        elif(Month == 'June'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,0,1,0,0,0,0,0,0
        elif(Month == 'July'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,0,0,1,0,0,0,0,0
        elif(Month == 'August'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,0,0,0,1,0,0,0,0
        elif(Month == 'September'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,0,0,0,0,1,0,0,0
        elif(Month == 'October'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,0,0,0,0,0,1,0,0
        elif(Month == 'November'):
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,0,0,0,0,0,0,1,0
        else:
            month_Jan, month_Feb, month_Mar, month_Apr, month_May, month_Jun,\
            month_Jul, month_Aug, month_Sep, month_Oct, month_Nov, month_Dec = 0,0,0,0,0,0,0,0,0,0,0,1
        
        Day_of_Week = request.form['dayofweek']
        if(Day_of_Week == 'Sunday'):
            dayofweek_flag_Sun, dayofweek_flag_Mon, dayofweek_flag_Tues, dayofweek_flag_Wed,\
            dayofweek_flag_Thurs, dayofweek_flag_Fri, dayofweek_flag_Sat = 1,0,0,0,0,0,0
        elif(Day_of_Week == 'Monday'):
            dayofweek_flag_Sun, dayofweek_flag_Mon, dayofweek_flag_Tues, dayofweek_flag_Wed,\
            dayofweek_flag_Thurs, dayofweek_flag_Fri, dayofweek_flag_Sat = 0,1,0,0,0,0,0
        elif(Day_of_Week == 'Tuesday'):
            dayofweek_flag_Sun, dayofweek_flag_Mon, dayofweek_flag_Tues, dayofweek_flag_Wed,\
            dayofweek_flag_Thurs, dayofweek_flag_Fri, dayofweek_flag_Sat = 0,0,1,0,0,0,0
        elif(Day_of_Week == 'Wednesday'):
            dayofweek_flag_Sun, dayofweek_flag_Mon, dayofweek_flag_Tues, dayofweek_flag_Wed,\
            dayofweek_flag_Thurs, dayofweek_flag_Fri, dayofweek_flag_Sat = 0,0,0,1,0,0,0
        elif(Day_of_Week == 'Thursday'):
            dayofweek_flag_Sun, dayofweek_flag_Mon, dayofweek_flag_Tues, dayofweek_flag_Wed,\
            dayofweek_flag_Thurs, dayofweek_flag_Fri, dayofweek_flag_Sat = 0,0,0,0,1,0,0
        elif(Day_of_Week == 'Friday'):
            dayofweek_flag_Sun, dayofweek_flag_Mon, dayofweek_flag_Tues, dayofweek_flag_Wed,\
            dayofweek_flag_Thurs, dayofweek_flag_Fri, dayofweek_flag_Sat = 0,0,0,0,0,1,0
        else:
            dayofweek_flag_Sun, dayofweek_flag_Mon, dayofweek_flag_Tues, dayofweek_flag_Wed,\
            dayofweek_flag_Thurs, dayofweek_flag_Fri, dayofweek_flag_Sat = 0,0,0,0,0,0,1
        
        Season = request.form['season']
        if(Season == 'Summer'):
            season_flag_summer, season_flag_autumn, season_flag_winter, season_flag_spring = 1,0,0,0
        elif(Season == 'Autumn'):
            season_flag_summer, season_flag_autumn, season_flag_winter, season_flag_spring = 0,1,0,0
        elif(Season == 'Winter'):
            season_flag_summer, season_flag_autumn, season_flag_winter, season_flag_spring = 0,0,1,0
        else:
            season_flag_summer, season_flag_autumn, season_flag_winter, season_flag_spring = 0,0,0,1
        
        FR_CODE = request.form['fr_code']
        if(FR_CODE == 'VFR'):
            fr_code_VFR, fr_code_MVFR, fr_code_IFR, fr_code_LIFR = 1,0,0,0
        if(FR_CODE == 'MVFR'):
            fr_code_VFR, fr_code_MVFR, fr_code_IFR, fr_code_LIFR = 0,1,0,0
        if(FR_CODE == 'IFR'):
            fr_code_VFR, fr_code_MVFR, fr_code_IFR, fr_code_LIFR = 0,0,1,0
        else:
            fr_code_VFR, fr_code_MVFR, fr_code_IFR, fr_code_LIFR = 0,0,0,1
        
        arr = np.array([
                        [tmpf,dwpf,relh,drct,sknt,alti,vsby,skyl1,feel,skyc1_BKN,skyc1_FEW,
                        skyc1_NSC,skyc1_OVC,skyc1_SCT,skyc1_VV ,month_Apr,month_Aug,month_Dec,
                        month_Feb,month_Jan,month_Jul,month_Jun,month_Mar,month_May,month_Nov,
                        month_Oct,month_Sep,dayofweek_flag_Fri,dayofweek_flag_Mon,dayofweek_flag_Sat,
                        dayofweek_flag_Sun,dayofweek_flag_Thurs,dayofweek_flag_Tues,dayofweek_flag_Wed,
                        season_flag_autumn,season_flag_spring,season_flag_summer,season_flag_winter,
                        fr_code_IFR,fr_code_LIFR,fr_code_MVFR,fr_code_VFR,]
                       ])
        
        y_pred = reg_model.predict(arr)
        print(y_pred)
        prediction_text = f"Results: tmpf={round(y_pred.item(0),3)} | relh={round(y_pred.item(1),3)} | sknt={round(y_pred.item(2),3)} | alti={round(y_pred.item(3),3)} | vsby={round(y_pred.item(4),3)} | skyl1={round(y_pred.item(5),3)}"

        return render_template('index.html',prediction_text=prediction_text)

        # if prediction==1:
        #      return render_template('index.html',prediction_text="The Customer will leave the bank")
        # else:
        #      return render_template('index.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True)