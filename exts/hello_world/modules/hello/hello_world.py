"""
OWASP Maryam!

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


meta = {
	'name': 'Hello World Extension',
	'author': 'example',
	'version': '0.1',
	'description': 'A simple package for demo.',
	'options': (
		('query', 'Hello World', True, 'Query string', '-q', 'store', str),
	),
	'examples': ('helloWorld -q "Hi World"',)
}

def module_api(self):
	self.hello(self.options['query'])
	output = {'results': self.options['query']}
	return output

def module_run(self):
	self.alert_results(module_api(self))
