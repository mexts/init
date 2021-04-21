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

from pytesseract import image_to_string
import cv2
import re

class main:

	def __init__(self, img):
		""" Convert image to text with pytesseract
		
			query		: image source
		"""
		self.framework = main.framework
		self.img = img

	def img2text(self):
		if self._is_readable(self.img):
			img = imread(self.img)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
			rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
			dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
			contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
															cv2.CHAIN_APPROX_NONE)
			im2 = img.copy()
			chrs = ''
			for cnt in contours:
				x, y, w, h = cv2.boundingRect(cnt)
				rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
				cropped = im2[y:y + h, x:x + w]
				text = image_to_string(cropped)
				chrs += text
			chrs = re.sub(r"[\s]+", ' ', chrs.strip())
			return chrs
		else:
			self.error(f"Could not find file {self.img}", 'img2text', 'img2text_with_peytesseract')
