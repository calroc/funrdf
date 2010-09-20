from google.appengine.ext import webapp
from google.appengine.ext.webapp.xmpp_handlers import CommandHandler
from google.appengine.ext.webapp.util import run_wsgi_app


class XMPPHandler(CommandHandler):

    def hello_command(self, message):
        message.reply('Bwah! %r' % message.body.lower())


application = webapp.WSGIApplication(
    [('/_ah/xmpp/message/chat/', XMPPHandler)],
    debug=True,
    )


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
