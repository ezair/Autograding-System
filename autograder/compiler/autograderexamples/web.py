import webbrowser
new = 2 # open in a new tab, if possible

url = "http://docs.python.org/library/webbrowser.html"
webbrowser.open(url,new=new)

url = "file://d/testdata.html"
webbrowser.open(url,new=new)
