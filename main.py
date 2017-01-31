import webapp2
import re

title = ''
page_header = """
<!DOCTYPE html>
<html>
<head>
	<title>User-Signup</title>
	<style type="text/css">
		.left {
			float: left;
		}
		.right {
			float: left;
		}
		.error {
			color: red;
		}
		.title {
			text-align: center;
		}
	</style>
</head>
<body>
	<h3 class=title>User Sign up</h3>
"""

page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        body = """
			<div class='left'>
				<form action="/welcome" method="post">
				<label>
					Usernname:
					<input type="text" name="username"/>
				</label><br>
				<label>
					Password:
					<input type="password" name="password"/>
				</label><br>
				<label>
					Verify Password:
					<input type="password" name="verify"/>
				</label><br>	
				<label>
					Email:
					<input type="text" name="email"/>
				</label>	
				<input type="submit" value="Sign up!"/>
			</form>
		</div>
			"""
	title = "Sign-up" 
	error = self.request.get("error")
	error_element = "<div class ='right'><p class='error'>" + error + "</p></div>"
	self.response.write(page_header + body + error_element + page_footer)

class Loggedin(webapp2.RequestHandler):
	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")

		USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")	
		PASSWORD_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")	
		EMAIL_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")	

		def valid_username(username):
			return USER_RE.match(username)
		def valid_password(password):
			return PASSWORD_RE.match(password)
		def valid_email(email):
			return EMAIL_RE.match(email)

		username_error = ''
		password_error = ''
		email_error = ''
		verify_error = ''
		if not valid_username or not username:
			username_error = "invalid-username<br>"
		if not valid_password or not password:
			password_error = "invalid-password<br>"
		if not valid_email:
			email_error = "invalid-email<br>"
		if not password == verify or not verify:
			verify_error = "verify is not same as password<br>"
		if username_error or email_error or verify_error or password_error:
			self.redirect('/?error=' + username_error + password_error + email_error + verify_error)
		content="""
			<h2>Welcome, {}</h2>
			""".format(username)
		self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Loggedin)
], debug=True)
