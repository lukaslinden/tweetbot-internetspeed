# Tweet at your Internetprovider

You want to auto-tweet your provider when your connection is below the promised speed? Well here you go!

## Disclaimer

There are many factors to consider when measuring your internetspeed. Use at your own risk and don't harass anyone.

### What you need

* Raspberry Pi (updated)
* Twitter Account (with api keys)

### Quick install

Install python & speedtest-cli & twython

```
sudo apt-get install python-pip
sudo pip install speedtest-cli
sudo pip install twython
```

Now let's connect to your twitter account!

```
sudo nano auth.py
```

Add your keys and save the file

```
consumer_key        = 'ABCDEFGHIJKLKMNOPQRSTUVWXYZ'
consumer_secret     = '1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ'
access_token        = 'ZYXWVUTSRQPONMLKJIHFEDCBA'
access_token_secret = '0987654321ZYXWVUTSRQPONMLKJIHFEDCBA'
```

Alright, now lets create the speedtest.py and insert the code: [speedtest.py](speedtest.py)

```
sudo nano speedtest.py
```

Insert your twitter-message and your download-limit (you can also filter by upload or ping)

### Let's test this!

```
python speedtest.py
```

Now you can add a cronjob to automate the testing and tweeting! Yay!
If you want to also monitor your internetspeeds -> save the data as .csv and upload it via IFTTT to your Dropbox and/or Google Docs.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* directly inspired by https://twitter.com/A_Comcast_User
* code partially by https://thepi.io/how-to-use-your-raspberry-pi-to-monitor-broadband-speed/
* I just wanted to gather all information in one place to get your Twitter-Bot up and running in no time so anyone could do this
