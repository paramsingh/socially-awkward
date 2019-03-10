# socially-awkward

A de-centralized social networking platform in order to provide more privacy and less control over the data by a single server or organization.

## Build Instructions

* Git clone the project

```
git clone https://github.com/paramsingh/socially-awkward
```

* Start a virtualenv

```
python3 -m virtualenv .
source bin/activate
```

* Install pip requirements
```
pip install -r requirements.txt
```

* Create the database
```
python create_tables.py
```

* Run the server
```
python run.py
```

## License

```
Copyright 2019 Rashi Sah <rashi.747@gmail.com>
Copyright 2019 Param Singh <paramsingh258@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
