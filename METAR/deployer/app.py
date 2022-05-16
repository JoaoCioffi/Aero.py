#-- Main Libraries --#
from flask import Flask, render_template, request
import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
import time
import pickle
import warnings
warnings.simplefilter(action='ignore', category=[FutureWarning,UserWarning])


#-- ML Model --#
X_train, y_train = pd.read_csv('X_train.csv'),pd.read_csv('y_train.csv')
reg_model = MultiOutputRegressor(GradientBoostingRegressor(max_leaf_nodes=10, min_impurity_decrease=0,
                                                           min_samples_leaf=2,min_samples_split=2,n_estimators=700,
                                                           max_depth=3,learning_rate=0.1,criterion='friedman_mse'))
start = time.time()                                                     
reg_model = reg_model.fit(X_train, y_train)
end = time.time()


#-- Flask Environment --#
app = Flask(__name__)

@app.route('/')
def man():
    return render_template('API.html')

@app.route('/predict', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        #Numerical Variables
        tmpf = request.form['tmpf']
        dwpf = request.form['dwpf']
        relh = request.form['relh']
        drct = request.form['drct']
        sknt = request.form['sknt']
        alti = request.form['alti']
        vsby = request.form['vsby']
        skyl1 = request.form['skyl1']
        feel = request.form['feel']
    
        #Sky Coverage (Boolean Type)
        skyc1_BKN = request.form['skyc1_BKN']
        skyc1_FEW = request.form['skyc1_FEW']
        skyc1_NSC = request.form['skyc1_NSC']
        skyc1_OVC = request.form['skyc1_OVC']
        skyc1_SCT = request.form['skyc1_SCT']
        skyc1_VV = request.form['skyc1_VV']
    
        #Month (Boolean Type)
        month_Apr = request.form['month_Apr']
        month_Aug = request.form['month_Aug']
        month_Dec= request.form['month_Dec']
        month_Feb = request.form['month_Feb']
        month_Jan = request.form['month_Jan']
        month_Jul = request.form['month_Jul']
        month_Jun = request.form['month_Jun']
        month_Mar = request.form['month_Mar']
        month_May = request.form['month_May']
        month_Nov = request.form['month_Nov']
        month_Oct = request.form['month_Oct']
        month_Sep = request.form['month_Sep']
    
        #Day of the Week (Boolean Type)
        dayofweek_flag_Fri = request.form['dayofweek_flag_Fri']
        dayofweek_flag_Mon = request.form['dayofweek_flag_Mon']
        dayofweek_flag_Sat = request.form['dayofweek_flag_Sat']
        dayofweek_flag_Sun = request.form['dayofweek_flag_Sun']
        dayofweek_flag_Thurs = request.form['dayofweek_flag_Thurs']
        dayofweek_flag_Tues = request.form['dayofweek_flag_Tues']
        dayofweek_flag_Wed = request.form['dayofweek_flag_Wed']
    
        #Season (Boolean Type)
        season_flag_autumn = request.form['season_flag_autumn']
        season_flag_spring = request.form['season_flag_spring']
        season_flag_summer = request.form['season_flag_summer']
        season_flag_winter = request.form['season_flag_winter']
    
        #Flight Rule Code (Boolean Type)
        fr_code_IFR = request.form['fr_code_IFR']
        fr_code_LIFR = request.form['fr_code_LIFR']
        fr_code_MVFR = request.form['fr_code_MVFR']
        fr_code_VFR = request.form['fr_code_VFR']
    
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
        return render_template('after.html', data=y_pred)

if __name__ == "__main__":
    app.run(debug=True)