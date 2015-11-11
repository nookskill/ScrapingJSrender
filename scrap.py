import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 

class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit() 

url = 'http://pantip.com/topic/34187841'
#This does the magic.Loads everything
r = Render(url)  
#result is a QString.
result = r.frame.toHtml()

#QString should be converted to string before processed by lxml
formatted_result = str(result.toUtf8())

#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

#Now using correct Xpath we are fetching URL of archives
archive_links = tree.xpath('//div[@class="display-post-story"]/text()')
x = ''.join(archive_links)
print (x.encode("utf-8"))

#f = open("out.csv","w")
#f.write(str(archive_links))
#f.close() 
