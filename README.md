# bwt-aqaperla
Project to read smart-meter data from BWT Aqa Perla S water softener. 
As they are equipped with a USB serial port I did some search on the web and
found some code artifacts from some home-automation projects:

# Source 1: IP Symcon Forum
https://www.symcon.de/forum/threads/25709-BWT-Aqa-Perla-goes-IP-Symcon

# Source 2: KNX User Forum
https://knx-user-forum.de/forum/supportforen/openhab/42254-bwt-aqua-perla-auslesen-jedoch-fehlt-mir-der-aktuelle-durchfluss

However, none of the above can be used standalone. So, since I am working on my "smarthome"
project anyway and as well was interested to gain access to the BWT smart meter using
a Raspberry PI and Python, I ended up with my own code to communicate with the BWT aqa perla.

It is tested and working with a AQA Perla S II (model 2015). There are still some
value that I have to explore and format correctly.

End goal is to load the data into an InfluxDB and report on it with Grafana as well 
as providing OpenHAB2 access to the BWT using the python code.
