<!--
**** README template for internal AGRAMKOW usage.
-->
<a name="readme-top"></a>

<!-- PROJECT LOGO / TITLE -->
<br/>
<div align="center">
  <h1 align="center">rflash - Server</h1>

  <p align="center">
    Remote flash server for automating embedded tests, utilizing the JLink debugger to flash the device.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
## Table of Contents
- [Table of Contents](#table-of-contents)
- [About](#about)
  - [Built with](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

<br/>


<!-- ABOUT THE PROJECT -->
## About
This repo contains the python code for the server side part of the remote flash application, developed to automate embedded testing at AGRAMKOW.
The server side listens for a single connection, receives the configuration to be used, as well as the binary to be flashed, flashing the device and returning the resulting information.
This code was developed to run on a Raspberry Pi, but can in theory run on any machine able to run Python - the code has however only been tested on an RPi 4B. The application was designed to run as a systemd service, started on startup - hence the installation instructions will reflect this. Feel free to adjust this process for your machine.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built with

* [Python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
The server side application is a relatively simple python project, and hence doesn't need anything but a python 3 installation.

### Prerequisites

* [python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation
1. Clone the repo
``` sh
git clone ██████████████████████████
```

2. Create the startup script / Add to startup script
    - If none is present, create a startup script: `/usr/local/bin/startup.sh`
    - Add the following line, replacing the provided template paths with the ones specific to your setup:
``` sh
/path/to/python/executable /path/to/src/main.py
```

3. Create the startup service (if not yet created)
    - If none is present, create the systemd unit file: `/usr/local/lib/systemd/system/startup.service`
    - Add the following lines to the file:
``` sh
[Unit]
Description=Runs /usr/local/bin/startup.sh

[Service]
ExecStart=/usr/local/bin/startup.sh

[Install]
WantedBy=multi-user.target
```

4. Enable the systemd service and start the service with the following commands:
``` sh
sudo systemctl enable startup && sudo systemctl start startup
```

<!-- USAGE EXAMPLES -->
## Usage
For usage, please refer to the rflash - client side application after installing the server application on the server machine.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] More configs

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

This software is proprietary and meant for in-house use only.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Sophus Christoffer Ott - 2SCT@agramkow.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>