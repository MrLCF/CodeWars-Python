"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

import re
def validate_pin(pin):
    #return true or false
    if(re.search('[a-zA-Z]', pin)) or len(pin) != 4 and len(pin) != 6 or not pin.isdigit():
        return False
    else:
        return True