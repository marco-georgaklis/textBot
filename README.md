# Twilio Text Bot
This is a basic chat bot with a few key features:
- You can get it to send you photos of cats
- You can get it to send you memes
- You can get it to send you quotes
- You can get it to give you stock picks

## What you will need:
- A twilio phone number (see twilio.com)
- If you want to use the stock predicting feature, please see my RobinBot repository. You will use the same reddit application for the stock pick scanning.
- ngrok. Download it from their website and follow their instructions.

### Navigate to project directory
```
cd path/to/textBot
```
### Run server.py
```
python server.py
```
You should get something that looks like this:
```
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 329-497-168
```
### Navigate to directory with ngrok executable
```
cd path/to/
```
### Run ngrok redirector
```
./ngrok http 5000
```
You should get a response like this
```
Session Status                online                                                                                                                                               
Account                       bob@gmail.com (Plan: Free)                                                                                                            
Version                       2.3.35                                                                                                                                               
Region                        United States (us)                                                                                                                                   
Web Interface                 http://127.0.0.1:4040                                                                                                                                
Forwarding                    http://ec96560668e3.ngrok.io -> http://localhost:5000                                                                                                
Forwarding                    https://ec96560668e1.ngrok.io -> http://localhost:5000  
```
Copy one the "Forwarding" urls and paste it in your twilio console under Phone numbers >> the phone number you bought >> Messaging >> Webhook

Try texting your bot!
