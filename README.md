## riden

This is a package to collect operating information from the Riden RD60XX powersupply.  It uses this [RIDEN RD6006](https://github.com/Baldanos/rd6006) python module wrapped in a class that implements this [Instrument](https://github.com/natecostello/instrument_logger) interface to allow easy logging.

## Getting Started

Note, this code requires a Riden RD60XX connected via usb serial to run.  It will also install a few dependencies.  See `setup.py` for details.

```
%python3 -m pip install git+https://github.com/natecostello/riden-status.git
```
```
%python3
>>> import riden-status
