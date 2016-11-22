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

form1 = """ 
<form action="http://www.Google.com/search">
    <input name="q">
    <input type="submit">
</form>
"""

form2 = """ 
<form action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

form3 = """ 
<form method="post" action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

form4 = """ 
<form >
    <input type="password" name="q">
    <input type="submit">
</form>
"""

form5 = """ 
<form >
    <input type="checkbox" name="q">
    <input type="checkbox" name="r">
    <input type="checkbox" name="s">
    <br>
    <input type="submit">
</form>
"""
form6 = """ 
<form >
    <lable>
        One
        <input type="radio" name="q" value="one">
    </lable>

    <lable>
        Two
        <input type="radio" name="q" value="two">
    </lable>

    <lable>
        There
        <input type="radio" name="q" value="three">
    </lable>
    <br>
    <input type="submit">
</form>
"""

form7 = """ 
<form >
    <select name="q">
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
    </select>
        
    <br>
    <input type="submit">
</form>
"""
form = """
<form method = "post">
    
    <h2>Type some text here</h2>

    <textarea name = "text" style="height: 100px; width: 400px;">
        
    </textarea>

    <br>
    <br>

    <input type = "submit" value="Submit 1">
    <input type = "submit" value="Submit 2">  
    <!--How to use multiple post requests with multiple submit buttons?-->

</form>
"""

outform = """
<p name = text>%(input_text)s<p>
<h3>King is here</h3>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, input_text=""):
        self.response.out.write(outform %{"input_text":input_text})

    def get(self):
        self.response.out.write(form)

    def post(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        text = self.request.get("text")
        text1 = cgi.escape(text, quote = True)
        #self.response.out.write(text)
        #self.response.out.write(text1)
        #self.write_form(text)
        self.response.out.write(outform)  #prints %(input_text)s. 
        self.response.out.write(text1)
        #self.response.out.write(self.request)

class TestHandler(webapp2.RequestHandler):
    def post(self):
    	#q = self.request.get("q")
        #self.response.out.write(q)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/testform', TestHandler)], 
   								 debug=True)
