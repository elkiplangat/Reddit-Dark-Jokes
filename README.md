# Reddit-Dark-Jokes
A simple python script that fetches jokes from r/darkjokes and optionally adds them to [variety](http://peterlevi.com/variety/) wallpaper quotes
## how to run
1. clone this repo & create a virtual environment(optional)
2. go to [reddit](https://www.reddit.com/prefs/apps)
3. create an app
4. set redirect url to localhost:8000
5. copy the credentials you are given
6. create a .env file in the project's root directory
7. add the credentials to the .env file like this:
  ```
   client_id = "client id that reddit gave you."
   client_secret = "secret key that reddit gave you."
   user_agent = "whatever name you gave your reddit app while creating it."
   ```
8. do a pip install -r requirements.txt in your terminal
10. run the script. `python3 main.py`
11. You can optionally add a commandline argument if you're on linux and have variety installed. by running:
  `
  python3 main.py var
  `
  ![screenshot](https://github.com/elkiplangat/Reddit-Dark-Jokes/blob/main/Screenshot.png?raw=true)
  
 
  
