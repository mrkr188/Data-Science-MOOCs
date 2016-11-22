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
import cgi
import string
import re


form = """
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(unerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(pwerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(vererror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            %(emerror)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

welcomeform = """
<!DOCTYPE html>
<html>
  <head>
    <title>Welcome</title>
  </head>
  <body>
    <h2>Welcome, %s!</h2>
  </body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
	return not email or EMAIL_RE.match(email)   #Cool Technique. Required to make email optional


class Welcome(webapp2.RequestHandler):
    def get(self):
        un = self.request.get("username")
        self.response.out.write(welcomeform %un)


class SignUp(webapp2.RequestHandler):

    def write_form(self, usn="", eml="", usne="", emle="", pwe="", ver=""):
        self.response.out.write(form %{"username": usn,
                                       "email": eml,
                                       "unerror": usne,
                                       "emerror": emle,
                                       "pwerror": pwe,
                                       "vererror": ver})

    def get(self):
        self.write_form()

    def post(self):
    	username = self.request.get("username")
    	email    = self.request.get("email")
    	password = self.request.get("password")
    	verify   = self.request.get("verify")

    	unerror  = ""
    	emerror  = ""
    	pwerror  = ""
    	vererror = ""

    	check_username = True
    	check_email    = True
    	check_password = True
    	check_verify   = True

    	if not valid_username(username):
    		check_username = False
    		unerror = "That's not a valid username."

    	if not valid_email(email):
    		check_email = False
    		emerror = "That's not a valid email."

    	if not valid_password(password):
    		check_password = False
    		pwerror = "That's not a valid password."

    	if valid_password(verify):
    		if password != verify:
    			check_verify = False
    			vererror = "Your Passwords didn't match"

    	if check_username and check_email and check_password and check_verify:
    		self.redirect("/welcome?username=%s" %username)
    	else:
    		self.write_form(username, email, unerror, emerror, pwerror, vererror)



app = webapp2.WSGIApplication([('/', SignUp),
							 ('/welcome', Welcome)], debug=True)
        
