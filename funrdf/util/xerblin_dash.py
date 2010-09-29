from webout import *


stack_div = DIV('Stack...', Class='stack_div')

dict_div = DIV('Dictionary...', Class='dict_div')

div = DIV(Class='cli_div')

div <= FORM(
    Class='cli_form',
    method='post',
    action='%(action_url)s'
    ) \
    <= TABLE(Class='cli_table') \
        <= (
            TR(TD(INPUT(name='cli', id='cli', Type='entry'), COLSPAN=2))
            + TR(
                TD(INPUT(value='Post Text', Type='button'))
                +
                TD(INPUT(value='Run Command', Type='button'))
               )
            )


print DIV(stack_div + dict_div + div, Class='shell_div')

