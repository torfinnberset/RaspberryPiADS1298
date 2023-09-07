# Raspberry Pi ADS1298 Driver

<p align="center">
  <img alt="banner" src="/images/banner.jpg/" width="600">
</p>
<p align="center" href="">
  A High Level Driver for ADS1298 Control with Raspberry Pi
</p>

## Install

### Using PyPI

```
pip install RaspberryPiADS1298
```

Anaconda is not currently supported, if you want to use anaconda, you need to create a virtual environment in anaconda, activate it and use the above command to install it.

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

Signal  |  RPi GPIO |  ADS Pin
--------------------------------
MOSI    |     20    |    DIN
MISO    |     19    |    DOUT
SCLK    |     21    |    SCLK
CS      |     24    |    CS
--------------------------------
START   |     22    |    START
RESET   |     24    |    nRESET
PWRDN   |     25    |    nPWRDN
DRDY    |     23    |    DRDY

### Hardware Setup for EEG

Connect sensing electrode to P (+) and ref to SRB1. With default config, the API doesn't enable the bias, that should help if you want to test with only a few electrodes.

## How to use it

It is easy as :

```python
from RaspberryPiADS1298 import ADS1298_API
from time import time, sleep

# init ads api
ads = ADS1298_API()

# init device
ads.openDevice()
# attach default callback
ads.registerClient(DefaultCallback)
# configure ads
ads.configure(sampling_rate=1000)

print("ADS1298 API test stream starting")

# begin test streaming
ads.startTestStream()

# begin EEG streaming
# ads.startEegStream()

# wait
sleep(10)

print("ADS1298 API test stream stopping")

# stop device
ads.stopStream()
# clean up
ads.closeDevice()

sleep(1)
print("Test Over")

```


## Credits

### Author
Fred Simard (ADS1299 driver)
Torfinn Berset (ADS1298 driver)
