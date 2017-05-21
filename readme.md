# OpenAutomation.py (python3)
## A command line application to automate the opening of files in python.

### Synopsis
I wanted to be able to automate the opening of specific files in a given directory with their default program. This idea arose when I was faced with a problem.

From time to time, I make my own graphics for client sites. Sometimes, many times, I make mistakes in illustrator. Mistakes such as forgetting to make the background transparent on every image in a given set. So I am faced with an issue, an easy one but a rather time consuming one. All I need to do is open the given file in illustrator and edit the opacity of the first layer.

 But how will I keep track of my progress? With a pen and paper or memory? I'm talking about like 50 SVGs. And manually opening each file would be such a pain. Thats why I made this quick little script.

### Usage:
1. Run the program with python 3.
2. Type a the directory of files you wish to iterate over.
3. Type the extension of files you wish to iterate over.
4. A file will open. Do what you wish, and when finished head back to the terminal and type anything to continue.
5. Repeat for all subsequent files in the directory.
6. Enjoy the boost in efficiency!

### Example IO:
```
Charless-iMac:file automation charles$ python3 openAutomation.py
please enter a valid directory and file extension to iterate over.

file extension: .svg
directory: /users/charles/desktop/icons
[+] opening file at path: /users/charles/desktop/icons/Facebook.svg
enter anything to continue... d
[+] opening file at path: /users/charles/desktop/icons/Github.svg
enter anything to continue... f
[+] opening file at path: /users/charles/desktop/lit/Instagram.svg
enter anything to continue...
```

### Notes:
This script only functions in unix! I haven't used windows in a long time.

### License (MIT)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
