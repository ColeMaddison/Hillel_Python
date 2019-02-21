# Write a Python program to make a chain of function decorators (bold, italic, underline etc.).

# "<b>" "</b>"
# "<i>" "</i>"
# "<u>" "</u>"



def decor_bold(to_decor):
    def wrapper(arg):
        modified_str = "{}{}{}".format("<b>", arg, "</b>")
        print('Modified bold')
        return to_decor(modified_str)
    return wrapper

def decor_italic(to_decor):
    def wrapper(arg):
        modified_str = "{}{}{}".format("<i>", arg, "</i>")
        print('Modified italic')
        return to_decor(modified_str)
    return wrapper

def decor_underline(to_decor):
    def wrapper(arg):
        modified_str = "{}{}{}".format("<u>", arg, "</u>")
        print('Modified underline')
        return to_decor(modified_str)
    return wrapper

@decor_bold
@decor_italic
@decor_underline
def sm_string(string):
    return string

print(sm_string('Hey'))