# Customize this file for your specific configuration.
# You *must* change ACTIVATED and SECRET.
#
# The URL to use for the dump is DUMP_URL?SECRET
# If SECRET is empty, DUMP_URL is enough.
#
# *** NOTE ABOUT SECURITY ***
#
# No Zope access control is done on this URL, as it is interpreted
# before the Zope application server comes into play. That's why you
# should change the secret or filter this URL before it gets to Zope,
# for instance in Apache.

ACTIVATED = True
SECRET = '1a1dc91c907325c69271ddf0c944bc72'
DUMP_URL = '/175076f9a90d14a4823d64c7728610ae'

