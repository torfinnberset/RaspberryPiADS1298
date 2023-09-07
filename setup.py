from setuptools import setup, find_packages

setup(name = 'RaspberryPiADS1298',
      version = '0.1.0',
      description = 'A lib for running ADS1298 on Raspberry Pi',
      author='Torfinn Berset',
      author_email='torfinnb@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy'],
      url='https://github.com/torfinnberset/RaspberryPiADS1298',
      keywords=['device', 'control', 'eeg', 'emg', 'ekg', 'exg', 'ads1298', 'raspberry', 'pi'],  # arbitrary keywords
      zip_safe=False)
