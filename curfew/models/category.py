from odoo import models, fields, api
import json
import logging

_logger = logging.getLogger(__name__)
class epass_category(models.Model):
    _name='curfew.category'
    _description='Curfew E-pass Category Model'
    _rec_name='category_name'
    category_name =fields.Text('Category Name')
    isActive = fields.Boolean('Status')
    
    
    @api.model
    def get_categoryname(self) :		
        categorylist={}
        for category in self.env['curfew.category'].search([]):			
            categorylist[category.id]={'category_name':category.category_name,'category_id':category.id}
            _logger.info(categorylist)
        return json.dumps(categorylist)