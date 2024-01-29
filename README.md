<h1> How To Run</h1>

<h3> 1- install python : </h3>
<p> run 'sudo apt install python3' </p>
<h3>2- install mariadb :</h3>
<p> run 'sudo apt install mariadb-server' </p>
<p> you must to create market database (run 'create database market;' ) </p>
<p> for configurations you can use db.env  </p>
<h3>3- clone repository :</h3>
<p> first make a directory then in your directory  run 'git clone https://github.com/moheb1234/market.git'</p>

<h3>4- virtual environment :</h3>
<p> in your directory run 'python3 -m venv venv'</p>
<p>you need to activate venv run 'source venv/bin/activate'</p>

<h3> 5- install packages :</h3>
<p> cd to the project and run 'pip install -r requirements.txt' or 'pip3 install -r requirements.txt'</p>

<h3>6- migrations:</h3>
<p> run 'python manage.py migrate'</p>

<h3> 7- run server :</h3>
<p> now you can run the server.  run 'python manage.py runserver' </p>


<h1>Api</h1>

<p><b>endpoint :</b> user/register/</p>
<p><b>HttpMethod :</b> = POST</p>
<p><b>Authorization :</b> = All</p>
<p><b>request data :</b> = username  , email , password  , confirm_password</p>
<p><b>result :</b> register a user and send a verify code to user email</p>
<p><b>status :</b> 201 </p>
<p><b>response data :</b> username ,  email</p>
<p><b>errors :</b> 1- duplicate username and email -> status 400 and error message 2- password and confirm password are not equal -> status 400 and error message</p>
<hr>

<p><b>endpoint:</b> user/verify-email/</p>
<p><b>HttpMethod:</b>  PUT</p>
<p><b>Authorization:</b>  All</p>
<p><b>request data:</b> verify_code </p>
<p><b>result:</b> active registerd user</p>
<p><b>status:</b> 200 </p>
<p><b>response data:</b> none</p>
<p><b>errors:</b> verify code is invalid -> status 400 and error message </p>
<hr>

<p><b>endpoint:</b> user/login/</p>
<p><b>HttpMethod:</b>  POST</p>
<p><b>Authorization:</b>  All</p>
<p><b>request data:</b> username , password </p>
<p><b>result:</b> authenticate a user (login)</p>
<p><b>status:</b> 201 </p>
<p><b>response data:</b> token</p>
<p><b>errors:</b> 1- no user found with input username -> status 404 and error message 2- user is exist but password is wrong -> status 401 and error message 3- username and password is correct but user is not active (need to verify email) -> status 403 and error message</p>
<hr>

<p><b>endpoint:</b> user/personal-info/</p>
<p><b>HttpMethod:</b> PUT</p>
<p><b>Authorization:</b> authenticated user</p>
<p><b>request data:</b> phone_number , passport_number , card , photo , birthday , country ,city (all fields are optional) </p>
<p><b>result:</b> edit personal informations</p>
<p><b>status:</b> 200 </p>
<p><b>response data:</b> all personal informations</p>
<p><b>errors:</b>None</p>
<hr>

<p><b>endpoint:</b> user/personal-info/</p>
<p><b>HttpMethod:</b> GET</p>
<p><b>Authorization:</b> authenticated user</p>
<p><b>request data:</b>None </p>
<p><b>result:</b> get personal info</p>
<p><b>status:</b> 200 </p>
<p><b>response data:</b> all personal informations</p>
<p><b>errors:</b>None</p>
<hr>

<p><b>endpoint:</b> strategy/macd/</p>
<p><b>HttpMethod:</b> POST</p>
<p><b>Authorization:</b> authenticated user</p>
<p><b>request data:</b>all strategy field and extra field for macd indicator </p>
<p><b>result:</b> create a new strategy for user</p>
<p><b>status:</b> 201 </p>
<p><b>response data:</b> all strategy data</p>
<p><b>errors:</b> duplicate strategy name -> status 400 and error message</p>
<hr>

<p><b>endpoint:</b> strategy/macd/</p>
<p><b>HttpMethod:</b> GET</p>
<p><b>Authorization:</b> authenticated user</p>
<p><b>request data:</b>None </p>
<p><b>result:</b> list all strategy's that created by user</p>
<p><b>status:</b> 200 </p>
<p><b>response data:</b> list all strategy's that created by user</p>
<p><b>errors:</b> None</p>
<hr>








   



