# ofxstatement-be-ing 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ING Netherlands plugin for ofxstatement 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project provides a custom plugin for [ofxstatement](https://github.com/kedder/ofxstatement) for ING (BE). It is based
on the work done by TheoMarescaux (https://github.com/TheoMarescaux/ofxstatement-be-ing) and on the work done by
jbbandos (https://github.com/jbbandos/ovxstatement-be-ing).

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
pip3 install ofxstatement-nl-ing
```

### From source
```
git clone https://github.com/jbbandos/ofxstatement-nl-ing.git
python3 setup.py install
```

## Usage
```
$ ofxstatement convert -t ingnl input.csv output.ofx
```
