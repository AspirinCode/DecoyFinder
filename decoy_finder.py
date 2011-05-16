#!/usr/bin/python -OO
#-*- coding:utf-8 -*-
#
#       decoy_finder.py is part of Decoy Finder
#
#       Copyright 2011 Adrià Cereto Massagué <adrian.cereto@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sys

from PySide.QtGui import QApplication
from PySide.QtCore import QTranslator, QLocale

ORGNAME = u'Universitat Rovira i Virgili - Grup de recerca en nutrigenòmica'
NAME = 'Decoy Finder'
VERSION = '0.3~alfa'

def main():
    """
    """
    from MainWindow import MainWindow

    translator = QTranslator() #Build the translator
    translator.load(":/locales/df_%s" % QLocale.system().name())
    qttranslator = QTranslator()#A translator for Qt standard strings
    qttranslator.load("qt_%s" % (QLocale.system().name()))
    App = QApplication(sys.argv) #Creating the app
    App.setOrganizationName(ORGNAME) #Setting organization and application's
    App.setApplicationName(NAME)#name. It's only useful for QSettings
    App.setApplicationVersion(VERSION)
    App.installTranslator(translator)#Install translators into the application.
    App.installTranslator(qttranslator)
    mw = MainWindow() #Now it's time to instantiate the main window
    mw.show() #And show it
    sys.exit(App.exec_()) #When the app finishes, exit.

if __name__ == '__main__':
    main()
