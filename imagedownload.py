import random
import urllib

def downloadImage(url):
    name = str(random.randrange(1,1000)) + '.jpeg'
    urllib.urlretrieve(url, name)

downloadImage('https://scontent-sjc3-1.xx.fbcdn.net/v/t1.0-9/33596805_10215800832791925_6354776105844473856_n.jpg?_nc_cat=100&_nc_ht=scontent-sjc3-1.xx&oh=d116f0db16fb2ce2b5f730d6dc4c6c34&oe=5CDE4FBB')
