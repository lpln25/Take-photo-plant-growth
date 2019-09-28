# Take-photo-plant-growth
take photo at period of time

This Project can help you to Take pictures `plant-growth` with run the code `main.py` or auto Take pictures `main v1.0`, it's very simple! just read the instruction

1. Take pictures with `main.py` :  just run with python3.
2. Take pictures with `main v1.0.py` : just set period times to run this code, I will show you.

## Pieces

![Raspberry pi zero - Picamera](http://s4.picofile.com/file/8373721376/pies.jpg)

## Run source `main.py`
1. update our Raspberry Pi 
~~~python
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev python3-pip
sudo pip3 install spidev
~~~
2. install the PiCamera library
~~~python
sudo pip install picamera
~~~
3. run code from currnet folder
~~~python
$ sudo python3 main.py
~~~

## Run source `main v1.0.py`
if your Raspberry Pi is not update, do steps 1 and 2 at previous level
1. Auto run code in `crontab`
~~~python
$ sudo crontab -e
~~~
2.add comment in GNU File: `crontab`
~~~python
# m h  dom mon dow   command
5 * * * /usr/bin/python3 /home/pi//main v1.0.py 1
10 * * * /usr/bin/python3 /home/pi//main v1.0.py 1
*/1 * * * /usr/bin/python3 /home/pi//main v1.0.py 0
~~~
3.To Save it, press `^X` then press `Y`
`First line` take picture at 05:00:00 o'clock with filter.
`Second line` take picture at 10:00:00 o'clock with filter.
`Third line` take picture at 05:00:00 o'clock.
