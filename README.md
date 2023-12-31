# Raspberry Pi ADS1298 Driver

<p align="center">
  <img alt="banner" src="/images/banner.jpg/" width="600">
</p>
<p align="center" href="">
  A High Level Driver for ADS1298 Control with Raspberry Pi
</p>

## Install

### From sources

For the latest version, you can install the package from the sources using the setup.py script

```
python setup.py install
```

or in developer mode to be able to modify the sources.

```
python setup.py develop
```

## Hardware Configuration

The Raspberry Pi 4b is used as a reference

| Signal | RPi GPIO | ADS Pin |
|--------|:--------:|--------:|
| MOSI   |    20    |     DIN |
| MISO   |    19    |    DOUT |
| SCLK   |    21    |    SCLK |
| CS     |    24    |      CS |
| START  |    22    |   START |
| RESET  |    24    |  nRESET |
| PWRDN  |    25    |  nPWRDN |
| DRDY   |    23    |    DRDY |

### Hardware Setup for EEG

Connect sensing electrode to P (+) and ref to SRB1. With default config, the API doesn't enable the bias, that should help if you want to test with only a few electrodes.

## How to use it

It is easy as :

```python
from RaspberryPiADS1298 import Ads1298Api
from time import sleep

# init ads api
ads = Ads1298Api()

# init device
ads.open_device()
# attach default callback
ads.register_client(DefaultCallback)
# configure ads
ads.configure(sampling_rate=1000)

print("ADS1298 API test stream starting")

# begin test streaming
ads.start_test_stream()

# begin ExG streaming
# ads.startExgStream()

# wait
sleep(10)

print("ADS1298 API test stream stopping")

# stop device
ads.stop_stream()
# clean up
ads.close_device()

sleep(1)
print("Test Over")

```


## Credits

### Author
Fred Simard (ADS1299 driver)
Torfinn Berset (ADS1298 driver)
