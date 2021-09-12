# ofxstatement-nl-argenta 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Argenta Netherlands plugin for ofxstatement 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project provides a custom plugin for [ofxstatement](https://github.com/kedder/ofxstatement) for Argenta (NL). It is based
on the work done by TheoMarescaux (https://github.com/TheoMarescaux/ofxstatement-be-ing), jbbandos (https://github.com/jbbandos/ofxstatement-be-ing)
and on the work done by rhbvkleef (https://github.com/rhbvkleef/ofxstatement-ing-nl).

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash. Plugin for ofxstatement parses a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

Users of ofxstatement have developed several plugins for their banks. They are
listed on main [`ofxstatement`](https://github.com/kedder/ofxstatement) site. If your bank is missing, you can develop
your own plugin.

## Installation

### From PyPI repositories
```
pip3 install ofxstatement-nl-argenta
```

### From source
```
git clone https://github.com/arnouddekker/ofxstatement-nl-argenta.git
python3 setup.py install
```

## Usage
```
$ ofxstatement convert -t argentanl input.csv output.ofx
```
