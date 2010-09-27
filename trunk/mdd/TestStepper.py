

class TestStepper:

  def __call__(self, aname, args, modelResult):
    method = getattr(self, aname + '_handler')
    if not method:
      raise ValueError(aname)
    result = method(*args)
    if result != modelResult:
      raise ValueError('%s != %s' % (result, modelResult))


class WebAppStepper(TestStepper):

  def __init__(self):
    self.session = {}

  def Initialize_handler(self):
    self.session.clear()

  def Login_handler(self, username, password):
    user = users[username]
    if user not in self.session:
      self.session[user] = Session()

    password = passwords[user] if password == 'Correct' else wrongPassword
    postArgs = urllib.urlencode({'username':user, 'password':password})

    # GET login page
    page = session[user].opener.open(webAppUrl).read()
    if show_page:
      print page

    # POST username, password
    page = session[user].opener.open(webAppUrl, postArgs).read()
    if show_page:
      print page

    # Check conformance, reproduce NModel WebApplication Stepper logic:
    # check for login failed message, no check for positive indication of login
    if loginFailed(page):
      return 'Failure'
    return 'Success'

  def Logout_handler(self, username):
    user = users[username]
    page = session[user].opener.open(logoutUrl).read()
    del self.session[user] # clear out cookie/session ID
    if show_page:
      print page

  def UpdateInt_handler(self, username, number):
    user = users[username]
    numArg = urllib.urlencode({'num':number})
    page = self.session[user].opener.open("%s?%s" % (webAppUrl, numArg)).read()
    if show_page:
      print page

  def ReadInt_handler(self, username):
    user = users[username]
    page = self.session[user].opener.open(webAppUrl).read()
    if show_page:
      print page
    numInPage = intContents(page)    
    return numInPage

