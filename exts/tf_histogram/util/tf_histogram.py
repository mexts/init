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

import pandas as pd
import matplotlib.pyplot as plt
import nltk
import re

from collections import Counter
from nltk.corpus import stopwords

class main:

	def __init__(self, docs: 'documents', form: 'documet form. e.g html'):
		""" show histogram plot of web term frequency """
		self.framework = main.framework
		self.docs = docs.lower()
		self.form = form.lower()
		self.words = []

	def remove_stopwords(self, without_punc=True):
		stops = stopwords.words('english')
		if self.form == 'html':
			self._remove_html_tags()
		if without_punc:
			self._punc()
		split = self.docs.split()
		self.words = [x for x in split if x not in stops]

	def _punc(self):
		self.docs = ' '.join(re.findall(r"[\w\-_#]+", self.docs))

	def _remove_html_tags(self):
		""" Remove html tags with regex"""
		scripts = re.compile(r"<script[^>]*>.*?</script>", 
				flags=re.DOTALL)
		styles = re.compile(r"<style[^>]*>.*?</style>",
				flags=re.DOTALL)
		tags = re.compile(r'<[^>]+>|&nbsp|&amp|&lt|&gt|&quot|&apos')
		self.docs = re.sub(tags, '', re.sub(styles, '', re.sub(scripts, '', self.docs)))

	def _counter(self, last):
		""" last: number of terms to show in plot """
		bow = Counter(self.words)
		return bow.most_common(last)

	def plot_histogram(self, title, last):
		most_common = self._counter(last)
		clean_tweets_no_urls = pd.DataFrame(most_common,
						columns=['words', 'count'])
		fig, ax = plt.subplots(figsize=(25, 25))
		clean_tweets_no_urls.sort_values(by='count').plot.barh(x='words',
									y='count',
									ax=ax,
									color="black")
		ax.set_title(title)
		plt.show()
