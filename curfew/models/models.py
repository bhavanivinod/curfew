# -*- coding: utf-8 -*-

from odoo import models, fields, api

class curfew(models.Model):
    _name = 'curfew.citizen'
    _rec_name='citizen_name'
    _description='Citizen Model'
    citizen_name=fields.Many2one('res.users',string="Name: ",delegate=True)
    citizen_dob=fields.Date('Date of Birth')

