# -*- coding: utf-8 -*-

###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015 Medma - http://www.medma.net
#    All Rights Reserved.
#    Medma Infomatix (info@medma.net)
#
#    Coded by: Turkesh Patel (turkesh.patel@medma.in)
#    Coded by: Ankit Gauri (ankit.gauri@medma.in)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Website Contact Us Form',
    'version': '1.0',
    "license": "AGPL-3",
    'author': 'Medma Infomatix',
    'category': 'Website',
    'website': 'http://www.medma.net',
    'summary': 'Attractive Website Contact Us Form like Material Design form for your website',
    'description': """Website Contact Us Form""",
    'data':['views/templates.xml'],
    'demo': [],
    'images': [
        'static/description/icon.png',
    ],
    'depends': ['website_crm'],
    'qweb': ['static/src/xml/*.xml'],
    'css': ['static/src/css/*.css'],
    'js': ['static/src/js/*.js'],
    'installable': 'True',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
