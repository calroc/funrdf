from webout import *
'''
Simple demonstration of the webout tool.

Build a page with a form.
'''


title = 'Post a Fact'
action_url = 'http://foo/bar'


head = HEAD(TITLE(title))

body = BODY()
body <= H1(title)
body <= 'This is where you enter facts:\n'

div = DIV(Class='fact_post_form_div')
div <= FORM(
    Class='fact_post_form',
    method="post",
    action=action_url
    ) \
    <= TABLE(Class='fact_post_form_table') \
        <= (

            # Two different ways to build cells:
            #
            # 1. explicit inner_HTML at construction time, or...
            TR(TD(INPUT(name='subj', id='subj', Type='entry')))

            # 2. Built up using '<=' operator (mind the order.)
            + (TR() <= (
                TD() <= INPUT(name='pred', id='pred', Type='entry')
                )
               )
            + (TR() <= (
                TD() <= INPUT(name='obj', id='obj', Type='entry')
                )
               )
            )

body <= div

print HTML(head + body)
