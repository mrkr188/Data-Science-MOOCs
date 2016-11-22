#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import string
import cgi

rot13form="""
<h2>Type some text to see magic</h2>
<br>
<form method="post">
  <textarea name="text" style="height: 100px; width: 400px;">%(input_text)s</textarea>
  <br>
  <input type="submit">
</form>
"""


def rot13(s):
    s2=""
    for c in s:
        if c in string.ascii_lowercase:
            s2 += chr((( ord(c) - ord("a") + 13 ) % 26 ) + ord("a"))
        elif c in string.ascii_uppercase:
            s2 += chr((( ord(c) - ord("A") + 13 ) % 26 ) + ord("A"))
        else:
            s2 += c
    return s2

class MainHandler(webapp2.RequestHandler):
    def write_form(self, input_text=""):
        self.response.out.write(rot13form % {"input_text": input_text })

    def get(self):
        self.write_form()
        
    def post(self):
        user_rotten = rot13( self.request.get('text') )
        user_rotten = cgi.escape( user_rotten, quote = True )
        self.write_form(user_rotten)

app = webapp2.WSGIApplication([('/rot13', MainHandler)], debug=True)


