from flask import Flask, session
from flask import render_template,request
from geopy.geocoders import Nominatim
import pymysql
import geocoder

app = Flask(__name__)

app.secret_key = 'any random string'


def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="", database="peertopeerride")
        return connection
    except:
        print("Something went wrong in database Connection")

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
        
        
#con = dbConnection()
#cursor = con.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/driverregistration')
def driverregistration():
    return render_template('driverregistration.html')


@app.route('/driverlogin')
def driverlogin():
    return render_template('driverlogin.html')


@app.route('/riderregistration')
def riderregistration():
    return render_template('riderregistration.html')

@app.route('/riderlogin')
def riderlogin():
    return render_template('riderlogin.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/ride')
def ride():
    return render_template('ride.html')

@app.route('/takearide')
def takearide():
    return render_template('takearide.html')

@app.route('/takeridelogin')
def takeridelogin():
    return render_template('takeridelogin.html')

@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/seealldrivers')
def seealldrivers():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('select * from location')
    row1 = cursor.fetchall()
    print(type(row1)) 
    print ("row1",row1)  
    print("lat",row1[0])
    print("latitude",row1[0][3])
    print("longitude",row1[0][4])
    print("drivername",row1[0][5])
    print("img",row1[0][6])
    print("icon",row1[0][7])
    lat_long=[]
    img=[]
    drivername=[]
    for i in list(row1):
        lat = i[3],i[4],i[5]
        lat2 = list(lat)
        id=i[0]
        dname=i[5]
        print("ssdsdssdsdsd",id)
        print("dname",dname)
        #im2 = list(im)
        #print("jsdjksjksdjsdfjsdjds",im2)
        lat_long.append(lat2)
        img.append([id])
        drivername.append([dname])
        print("lat_long",lat_long)
        print("drivername",drivername)
#    print(img)            
    return render_template('seealldrivers.html',data=lat_long,data2=img,data3=drivername)
    

@app.route('/SessionHandle',methods=['POST','GET'])
def SessionHandle():
    if request.method == "POST":
        details = request.form
        name = details['name']
        password = details['pass']
        session['namedriver'] = name        
        session['pass'] = password
        strofuser = name
        print (strofuser.encode('utf8', 'ignore'))
        return strofuser
   
@app.route('/SessionHandleride',methods=['POST','GET'])
def SessionHandleride():
    if request.method == "POST":
        details = request.form
        name = details['name']
        print(name)
        password = details['pass']
        print(password)
        session['name'] = name        
        session['pass'] = password
        strofuser = name
        print (strofuser.encode('utf8', 'ignore'))
        return strofuser
    
    
@app.route('/main')
def main():
    return render_template('main1.html') 

@app.route('/main1')
def main1():
    return render_template('main.html')

@app.route('/requestfromrider')
def requestfromrider():
    return render_template('requestfromrider.html')



@app.route('/location',methods=['POST','GET'])
def createseller():
    if request.method == "POST":
        details = request.form
        locationname = details['location']
        print("Location Name",locationname)
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(locationname)
        print("location",location)
        print("The latitude of the location is: ", location.latitude)
        print("The longitude of the location is: ", location.longitude)
        lat=location.latitude
        long=location.longitude
        print("latitude",lat)
        print("longitude",long)
        
        return render_template('map.html',latitude=lat,longitude=long) 
    
@app.route('/chooseyourride')
def chooseyourride():
    return render_template('chooseyourride.html')


@app.route('/uploadlocation',methods=['POST','GET'])
def uploadlocation():
    if request.method == "POST":
        nameoflocation = request.form['locationname']
        con = dbConnection()
        cursor = con.cursor()
        sql1 = "INSERT INTO location (locationname) VALUES(%s);"
        val1 = (nameoflocation)
        cursor.execute(sql1,val1)
        con.commit()
        ListOfFile = {'a':nameoflocation}
        return ListOfFile  
    return render_template('chooseyourride.html',data={}) 


@app.route('/showonmap',methods=['POST','GET'])
def showonmap():
    if request.method == "POST":     
        details = request.form
        locationname = details['data']
        from geopy.geocoders import Nominatim
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode(locationname)
        print(getLoc.address)
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
        finalriderlat=getLoc.latitude
        finalriderlong=getLoc.longitude
        g = geocoder.ip('me')
        print("current location",g.latlng)
        curloc=g.latlng
        print ("curloc",curloc)
        print ("lat",curloc[0])
        print ("long",curloc[1])
        finalcurlat=curloc[0]
        finalcurlong=curloc[1]
        
        
        return render_template('map.html',finalriderlat=finalriderlat,finalriderlong=finalriderlong,finalcurlat=finalcurlat,finalcurlong=finalcurlong)
    
 
@app.route('/paymentfromdriver')
def paymentfromdriver():
    return render_template('paymentfromdriver.html')



@app.route('/pay',methods=['POST','GET'])
def pay():
    if request.method == "POST":     
        details = request.form
      
        return render_template('message.html')
    
@app.route('/bookingofdriver',methods=['POST','GET'])
def bookingofdriver():
    if request.method == "POST":
        details = request.form
        latitude1 = details['latitude'] 
        longitude1 = details['longitude']  
        drivername1 = details['drivername']  
        print ("latitude after click on marker",latitude1)
        print ("longitude after click on marker",longitude1)
        print ("Driver Name",drivername1)
        datalatitude1=latitude1
        datalongitude1=longitude1
        con = dbConnection()
        cursor = con.cursor() 
        print(latitude1)
        print(longitude1)
        session['lat'] = latitude1 
        session['long'] = longitude1 
        session['dname'] = drivername1 
        
    return render_template('bookdriver.html',latitude1=latitude1, longitude1=longitude1, drivername1=drivername1) 


@app.route('/main2')
def main2(): 
    a = session.get("lat")
    b = session.get("long")
    c = session.get("dname")
    return render_template('bookdriver.html',a=a,b=b,c=c) 


@app.route('/bookride',methods=['POST','GET'])
def bookride():
    if request.method == "POST":
        details = request.form
        locationname = details['name']
        drivername = details['name1']
        ridername = session.get("name")
        print ("name",locationname)
        print ("adasdsadsadasdasdasdasdsad",drivername)
        from geopy.geocoders import Nominatim
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode(locationname)
        print(getLoc.address)
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
        riderlat=getLoc.latitude
        riderlong=getLoc.longitude
        import geocoder
        myloc = geocoder.ip('me')
        print(myloc.latlng)
        latlong=myloc.latlng
        print ("current latitude",latlong[0])
        print ("current longitude",latlong[1])
        currentlatitude=latlong[0]
        currentlongitude=latlong[1]
        con = dbConnection()
        cursor = con.cursor() 
        sql2  = "INSERT INTO currentlocationider(latitude,longitude,markerimage,riderlatitude,riderlongitude,dname,rname,status) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
        val2 = (str(currentlatitude), str(currentlongitude),"static/icons/cloudysunny.png",riderlat,riderlong,drivername,ridername,"ride request")
        cursor.execute(sql2,val2) 
        con.commit()
        
    return render_template('bookdriver.html')



@app.route('/seeallriders')
def seeallriders():
    drivername = session.get("namedriver")
    print ("drivername",drivername)
    con = dbConnection()
    cursor = con.cursor()
    result_count = cursor.execute('SELECT * FROM currentlocationider WHERE  dname = %s',(drivername))
    row1 = cursor.fetchall()
    print(type(row1)) 
    print ("hhshshshshsh",row1)      
    print("lat",row1[0])
    print("latitude",row1[0][1])
    print("longitude",row1[0][2])
    print("drivername",row1[0][6])
    print("ridername",row1[0][7])
    print("icon",row1[0][3])
    lat_long=[]
    img=[]
    ridername=[]
    for i in list(row1):
        lat = i[4],i[5],i[7]
        rname=i[7]
        lat2 = list(lat)
        id=i[0]
        print("ssdsdssdsdsd",id)
        print("ridername",rname)
        #im2 = list(im)
        #print("jsdjksjksdjsdfjsdjds",im2)
        lat_long.append(lat2)
        img.append([id])
        ridername.append([rname])
        print ("list of rider",)
#    print(lat_long)
#    print(img)        
    return render_template('requestfromrider.html',data=lat_long,data2=img)


@app.route('/bookingofrider',methods=['POST','GET'])
def bookingofrider():
    if request.method == "POST":
        details = request.form
        latitude1 = details['latitude'] 
        longitude1 = details['longitude'] 
        ridername = details['ridername']
        con = dbConnection()
        cursor = con.cursor()
        q = 'update currentlocationider set status =%s   WHERE rname = %s '
        val = (str("Ride Accepted"), str(ridername))
        cursor.execute(q, val)
        con.commit()
        
        result_count = cursor.execute('SELECT * FROM currentlocationider WHERE  rname = %s',(ridername))
        row1 = cursor.fetchall()
        print(type(row1)) 
        print (row1)      
        print("lat",row1[0])
        print("latitude",row1[0][4])
        print("longitude",row1[0][5])
        lat_long=[]
        for i in list(row1):
            lat = i[4],i[5]
            lat2 = list(lat)
            id=i[0]
            print("ssdsdssdsdsd",id)
            #im2 = list(im)
            #print("jsdjksjksdjsdfjsdjds",im2)
            lat_long.append(lat2)
            print("lat_long",lat_long)
            riderlat=lat_long[0][0]
            riderlong=lat_long[0][1]
            
            
        import geocoder
        myloc = geocoder.ip('me')
        print(myloc.latlng)
        location=myloc.latlng
        currlat=location[0]
        curlong=location[1]
        print("currlat",currlat)
        latlong=myloc.latlng  
        finalcurrentlatitude=latlong[0]
        finalcurrntlongitude=latlong[1]
        session['lat'] = latitude1           
        session['longi'] = longitude1           
        session['currlatitude'] =(latlong[0])          
        session['currlongitude'] =(latlong[1]) 
        session['riderlat'] = riderlat 
        session['riderlong'] = riderlong 
        
        
        
                # Python 3 program to calculate Distance Between Two Points on Earth
        from math import radians, cos, sin, asin, sqrt
        def distance(lat1, lat2, lon1, lon2):
        	
        	# The math module contains a function named
        	# radians which converts from degrees to radians.
        	lon1 = radians(lon1)
        	lon2 = radians(lon2)
        	lat1 = radians(lat1)
        	lat2 = radians(lat2)
        	
        	# Haversine formula
        	dlon = lon2 - lon1
        	dlat = lat2 - lat1
        	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        
        	c = 2 * asin(sqrt(a))
        	
        	# Radius of earth in kilometers. Use 3956 for miles
        	r = 6371
        	
        	# calculate the result
        	return(c * r)
        	
        	
        # driver code
        lat1 = finalcurrentlatitude
        lat2 = riderlat
        lon1 = finalcurrntlongitude
        lon2 = riderlong
        print(distance(lat1, lat2, lon1, lon2), "K.M")
        distanceinkilometers=distance(lat1, lat2, lon1, lon2)
        print ("distanceinkilometers",distanceinkilometers)
        number = distanceinkilometers * 8
        print('The product is: ',number)
        fare1=number
        New_Number1 = int(fare1)
        print("Number1 = ", New_Number1)
        fare=New_Number1
        print("fare",fare)
        session['fareofplace'] = fare 
        session['rider'] = ridername

        return "true"
    return render_template('showroute.html')


@app.route('/finishride',methods=['POST','GET'])
def finishride():
    if request.method == "POST":
        details = request.form
        f = session.get("fareofplace")
        r = session.get("rider")
        con = dbConnection()
        cursor = con.cursor()
        q = 'update currentlocationider set status =%s   WHERE rname = %s '
        val = (str("Finished Ride"), str(r))
        cursor.execute(q, val)
        con.commit()
        print ("fsadsdfsdfsdsfdfs",f)
    return render_template('paymentfromdriver.html',f=f,r=r)

@app.route('/showroute')
def showroute(): 
    a = session.get("lat")
    b = session.get("longi")
    c = session.get("currlatitude")
    d = session.get("currlongitude")
    e = session.get("riderlat")
    print("e",e)
    f = session.get("riderlong")
    
    return render_template('showroute.html', a=a,b=b,c=c,d=d,e=e,f=f) 



@app.route('/startride',methods=['POST','GET'])
def startride():
    if request.method == "POST":
        import geocoder
        myloc = geocoder.ip('me')
        print(myloc.latlng)
        latlong=myloc.latlng
        print ("current latitude",latlong[0])
        print ("current longitude",latlong[1])
        currentlatitude=latlong[0]
        currentlongitude=latlong[1]
        cursor.execute('select * from currentlocationider')
        row1 = cursor.fetchall()
        print (row1)      
        print("riderlat",row1[0][4])
        print("riderlong",row1[0][4])
        
        
    return render_template('bookdriver.html')
   
    
   
@app.route('/add',methods=['POST','GET'])
def add():
    if request.method == "POST":
        fare = request.form['name1'] 
        rname = request.form['name2'] 
        print ("fare",fare)
        print ("rname",rname)
        session['ridernameforpayment'] = rname 
        session['fareforrider'] = fare 
        
        ListOfFile = {'a':fare,'b':rname}
        return ListOfFile 
    return render_template('paymentfromdriver.html',data={})


@app.route('/paymentoption')
def paymentoption(): 
    a = session.get("ridernameforpayment")
    print ("ridernameforpayment",a)
    b = session.get("fareforrider")
    print("fareforrider",b)
    
    return render_template('paymentoption.html', a=a,b=b) 


@app.route('/makeapayment',methods=['POST','GET'])
def makeapayment():
    if request.method == "POST":
        ridername = request.form['ridername'] 
        farename = request.form['fare'] 
       
        session['ridernameforpayment123'] = ridername 
        session['fareforrider123'] = farename 
        
        ListOfFile = {'a':ridername,'b':farename}
        return ListOfFile 
    return render_template('paymentfromdriver.html',data={})


@app.route('/profile')
def profile():
    f = session.get("name")
    print("profilename",f)
    return render_template('profile.html', f=f)


@app.route('/profiledriver')
def profiledriver():
    f = session.get("namedriver")
    print("profilename",f)
    return render_template('profiledriver.html', f=f)
     
    
@app.route('/message')
def message():
    return render_template('message.html')


@app.route('/ratingfromdriver')
def ratingfromdriver():
    return render_template('ratingfromdriver.html')


    
    
@app.route('/rating',methods=['POST','GET'])
def rating():
    if request.method == "POST":
        details = request.form.get
        star1 = details('rate1')
        star2 = details('rate2')
        star3 = details('rate3')
        star4 = details('rate4')
        star5 = details('rate5')
        lst = []
        lst.extend((star1, star2, star3, star4, star5))
        print("list",lst)  
        lst = list(filter((None).__ne__, lst))
        print(lst)
        count = len(lst)
        print("Count",count)
        
        driver = session.get("namedriver")
        rider = session.get("name")
        
        con = dbConnection()
        cursor = con.cursor()
        sql1 = "INSERT INTO ratingtable (driver,rate,rider) VALUES(%s,%s,%s);"
        val1 = (driver,int(count),rider)
        cursor.execute(sql1,val1)
        con.commit()     
        
        return render_template('ratingfromrider.html',count=count)
    
    
@app.route('/ratingfromdrivertorider',methods=['POST','GET'])
def ratingfromdrivertorider():
    if request.method == "POST":
        details = request.form.get
        star1 = details('rate1')
        star2 = details('rate2')
        star3 = details('rate3')
        star4 = details('rate4')
        star5 = details('rate5')
        lst = []
        lst.extend((star1, star2, star3, star4, star5))
        print("list",lst)  
        lst = list(filter((None).__ne__, lst))
        print(lst)
        count = len(lst)
        print("Count",count)
        
        driver = session.get("namedriver")
        rider = session.get("name")
        
        con = dbConnection()
        cursor = con.cursor()
        sql1 = "INSERT INTO ratingtablefromdriver (driver,rate,rider) VALUES(%s,%s,%s);"
        val1 = (driver,int(count),rider)
        cursor.execute(sql1,val1)
        con.commit()     
        
        return render_template('ratingfromrider.html',count=count)
    
@app.route('/dataall',methods=['POST','GET'])
def dataall():
    if request.method == "POST":
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute("SELECT * FROM location")
        res = cursor.fetchall()
        print("requastdetails",res)
        return render_template('seealldrivers.html',res=res) 
    
    
    
    
    
@app.route('/findride')
def findride():
    return render_template('findride.html')

    
@app.route('/main45')
def main45():
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute("SELECT * FROM location")
        res = cursor.fetchall()
        print("requastdetails",res)
        return render_template('nearbydrivers.html',res=res)
    
@app.route('/main478')
def main478():
        drivername = session.get("namedriver")
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute("SELECT * FROM findride1")
        row1 = cursor.fetchall()
        res=row1
        print(type(row1)) 
        print (row1)      
        return render_template('request.html',res=res)
    
@app.route('/main56')
def main56():
    return render_template('waitingpage.html')


@app.route('/offerride')
def offerride():
    return render_template('offerride.html')

@app.route('/Uploadfile',methods=['POST','GET'])
def Uploadfile():
    print("Get method")
    if request.method == "POST":
        print("Post method")
        ridername = session.get("name")
        drivername = session.get("namedriver")
        clocation = request.form['clocation']
        destination= request.form['dest'] 
        noofpassagers = request.form['nopass'] 
        con = dbConnection()
        cursor = con.cursor()
        sql1 = "INSERT INTO findride1 (cloac,dest,nopass,username,drivername) VALUES(%s,%s,%s,%s,%s);"
        val1 = (clocation,destination,noofpassagers,ridername,drivername)
        cursor.execute(sql1,val1)
        con.commit()
        
        ListOfFile = {'i':clocation,'a':destination,'b':noofpassagers}
        
        return ListOfFile  
    return render_template('findride.html',data={})  


@app.route('/status')
def status():
    ridername = session.get("name")
    print ("ridername",ridername)
    con = dbConnection()
    cursor = con.cursor()
    result_count = cursor.execute('SELECT * FROM currentlocationider WHERE  rname = %s',(ridername))
    row1 = cursor.fetchall()
    res=row1
    print(type(row1)) 
    print ("hhshshshshsh",row1)      
    return render_template('status.html',res=res)


@app.route('/ratingfromrider')
def ratingfromrider():
    c = session.get("count")
    print ("gfgfgfgffgfggggggggggfgfgfg",c)
    return render_template('ratingfromrider.html')

@app.route('/ratingfromriderdisplay')
def ratingfromriderdisplay():
    
    driver = session.get("namedriver")
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM ratingtable WHERE driver = %s',(driver))
    row1 = cursor.fetchall()
    print ("hhshshshshsh",row1) 
    
    return render_template('ratingfromriderdisplay.html',res=row1)


@app.route('/ratingfromdriverdisplay')
def ratingfromdriverdisplay():
    
    rider = session.get("name")
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM ratingtablefromdriver WHERE rider = %s',(rider))
    row1 = cursor.fetchall()
    print ("hhshshshshsh",row1) 
    
    return render_template('ratingfromdriverdisplay.html',res=row1)


@app.route('/Logout')
def Logout():    
    session.pop('name')
    return render_template('index1.html')


@app.route('/History')
def History():  
    ridername = session.get("name")
    
    con = dbConnection()
    cursor = con.cursor()
    result_count = cursor.execute('SELECT * FROM findride1 WHERE  username = %s',(ridername))
    res = cursor.fetchall()
    print("requastdetails",res)
    return render_template('history.html',res=res)


@app.route('/Historydriver')
def Historydriver():  
    drivername = session.get("namedriver")
    con = dbConnection()
    cursor = con.cursor()
    result_count = cursor.execute('SELECT * FROM findride1 WHERE  drivername = %s',(drivername))
    res = cursor.fetchall()
    print("requastdetails",res)
    return render_template('historydriver.html',res=res)




if __name__ == "__main__":
    app.run("0.0.0.0")