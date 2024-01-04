<!--
**** README template for internal AGRAMKOW usage.
-->
<a name="readme-top"></a>

<!-- PROJECT LOGO / TITLE -->
<br/>
<div align="center">
  <h1 align="center">rflash - Client</h1>

  <p align="center">
    Remote flash client for automating embedded tests, utilizing the JLink debugger to flash the device.
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
This repo contains the python code for the client side part of the remote flash application, developed to automate embedded testing at AGRAMKOW.
The client side application is a simple script, taking a a path to the configuration file and the path to the produced binary, thereby sending the contents of both files to the server. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built with

* [Python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
The client side application is a relatively simple python project, and hence doesn't need anything but a python 3 installation.

### Prerequisites

* [python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation
1. Add repo as submodule to a given repo
    - It is recommended to install the client side application, as part of the repository it aims to help test. Replace the following placeholders with the actual destination folder:
``` sh
git submodule add ██████████████████████████ <destination_folder>
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
Call the rflash client with the following command, replacing the placeholders with the actual paths:
``` sh
python3 /path/to/src/main.py /path/to/conf.toml /path/to/produced/binary
```

A valid example configuration can be found in the `tests` folder, containing the minimum required configuration to be sent.

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