# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         application
# Description:  
# Author:       Allen
# Time:         2021/1/4 16:01
# ------------------------------------------------------------------------------
from tornado import ioloop
from tornado.web import RequestHandler, Application, url


class MainHandler(RequestHandler):
    def get(self):
        self.write('<a href="%s">link to story 1</a>' %
                   self.reverse_url("story", "1"))


class StoryHandler(RequestHandler):
    def get(self, story_id):
        self.write("this is story %s" % story_id)


if __name__ == '__main__':
    app = Application([
        url(r"/", MainHandler),
        url(r"/story/([0-9]+)", StoryHandler, name="story")
    ])
    app.listen(8888)
    ioloop.IOLoop.current().start()
