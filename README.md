<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">
  <div><a href="https://github.com/fredzo/owon-xdg-python-tools/">Owon XDG Python Tools</a></div>
  </h3>
  <p align="center">
    Python tools for <a href="https://www.owon.com.hk/products_owon_xdg2000_series_2-ch_arbitrary_waveform_generator">Owon XDG / Multicomp MP75xxx </a> Abitrary Waveform Generators.
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project provides a set of Python scripts used to work with <a href="https://www.owon.com.hk/products_owon_xdg2000_series_2-ch_arbitrary_waveform_generator">Owon XDG / Multicomp MP75xxx </a> Abitrary Waveform Generators.

It is based on the work of [James @baldengineer on element14](community.element14.com/challenges-projects/element14-presents/workbenchwednesdays/w/documents/23206/160-mhz-arbitrary-waveform-generator-review---workbench-wednesdays-44?CommentId=eb6b685d-1705-4b3f-a9cd-d44dcebba150).


<!-- USAGE EXAMPLES -->
## Usage
### 406frame_to_bin.py
Generated a BIN file from the provided 406 Mhz Cospas/Sarsat beacon frame
This bin file can be loaded in an Owon XDG or Multicomp MP75xxx
Arbitrary waveform generator.

## Original files from James @baldengineer
### mp750290_csv_to_bin.py
This program converts a CSV file with time and voltage points into a binary file for the Multicomp Pro MP750290 (and similar) AWGs.
You can load these BINary files via USB port/drive (using the front panel connector.)

### sine_1meg.bin and SINE_1MEG.CSV
Sample files of a 1 MHz Sine Wave

### program_csv_via_SCPI_mp750290.py
Using `pyvisa` this script loads the waveform memory with a CSV file. 
WIP : not working (crashes the generator).


<!-- BUILD AND INSTALL -->
## Build And Install

### Build

To build the project, you just have to run **Build** command in PlatformIO.
  ```sh
  Build
  ```

### Installation

Installation is performed with **Upload** or **Upload and Monitor** commands in PlatformIO while the Awtris device is connected via USB.
   ```sh
   Upload and Monitor
   ```

<!-- ROADMAP -->
## Roadmap

- [x] TODO
- [ ] Documentation
    - [ ] English Readme
    - [ ] French Readme 

See the [open issues](https://github.com/fredzo/owon-xdg-python-tools/issues) for a full list of proposed features (and known issues).

<!--p align="right">(<a href="#readme-top">back to top</a>)</p-->



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!--p align="right">(<a href="#readme-top">back to top</a>)</p-->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!--p align="right">(<a href="#readme-top">back to top</a>)</p-->



<!-- CONTACT -->
## Contact

Fredzo - [https://github.com/fredzo](https://github.com/fredzo)

Project Link: [https://github.com/fredzo/owon-xdg-python-tools](https://github.com/fredzo/owon-xdg-python-tools)

<!--p align="right">(<a href="#readme-top">back to top</a>)</p-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/fredzo/esp32-gamepad-host.svg?style=for-the-badge
[contributors-url]: https://github.com/fredzo/esp32-gamepad-host/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/fredzo/esp32-gamepad-host.svg?style=for-the-badge
[forks-url]: https://github.com/fredzo/esp32-gamepad-host/network/members
[stars-shield]: https://img.shields.io/github/stars/fredzo/esp32-gamepad-host.svg?style=for-the-badge
[stars-url]: https://github.com/fredzo/esp32-gamepad-host/stargazers
[issues-shield]: https://img.shields.io/github/issues/fredzo/esp32-gamepad-host.svg?style=for-the-badge
[issues-url]: https://github.com/fredzo/esp32-gamepad-host/issues
