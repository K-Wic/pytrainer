# -*- coding: iso-8859-1 -*-

#Copyright (C) Fiz Vazquez vud1@sindominio.net
# Modified by dgranda

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import logging
import os, sys, commands
from lxml import etree

class garmintools():
	def __init__(self, parent = None, data_path = None):
		self.parent = parent
		self.pytrainer_main = parent.parent
		self.tmpdir = self.pytrainer_main.profile.tmpdir
		self.main_data_path = data_path
		self.data_path = os.path.dirname(__file__)

	def getName(self):
		return _("Garmintools")

	def getVersion(self):
		outstatus = commands.getstatusoutput('which garmin_save_runs')
		if outstatus[0] == 0: #Found garmin_save_runs in path 
			path = "Unknown"
			return path
		else:
			return None

	def getSourceLocation(self):
		return "http://code.google.com/p/garmintools/"

	def deviceExists(self):
		outstatus = commands.getstatusoutput('garmin_get_info')
		if outstatus[0] is not 0 or outstatus[1].startswith("garmin unit could not be opened"):
			return False
		else:
			return True

	def isPresent(self):
		if self.getVersion():
			return True
		else:
			return False
