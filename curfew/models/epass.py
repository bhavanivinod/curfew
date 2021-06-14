from odoo import models, fields, api
import smtplib
from email.message import EmailMessage
from string import Template
import logging  
_logger = logging.getLogger(__name__)
class curfew_epass(models.Model):
    _name='curfew.epass'
    _description='Curfew E-pass Application Model'
    _rec_name = 'epass_app_no'
    
    epass_app_no = fields.Integer(string="Application number")
    curfew_epass_category = fields.Many2one('curfew.category', string='Epass category')
    citizen_name=fields.Text(string="Name: ")
    citizen_dob=fields.Date('Date of Birth')
    citizen_address=fields.Text(string='Address')
    district_name=fields.Text(string='District Name')
    citizen_email = fields.Text(string='Email')
    citizen_vehicle_no = fields.Text(string='Vehicle No')
    citizen_vehicle_type = fields.Text(string='Vehicle Type')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')
    from_place=fields.Text(string='Start Place')
    to_place=fields.Text(string='Destination')
    state = fields.Selection([
        ('Pending Approval','Pending Approval'),
        ('rejected','Rejected'),
        ('approved','Approved')
        ], string='status', readonly=True, index=True, default='Pending Approval')
    
    
    @api.multi
    def batch_approve_epass(self):
        if self.state == 'confirm':
            self.sudo().update({
            
            'state': 'approved'
            
            })
        #using external mail system   
#         html = Template("""<!doctype html> <html> <head></head><body><br>Dear $name,
#                     <br>
#                     <br>
#                     Your Epass has been approved, visit website and download it.
#                     <br>
#                     <br>
#                     <br>Thanks and Regards
#                     <br>Curfew E-Pass - Administration
#                     </body>
#                     </html>""")
#         email = EmailMessage()
#         email['from'] = 'Epass Approval'
#         email['to'] = self.citizen_email
#         email['subject'] = 'E-Pass Details'
#                 
#         email.set_content(html.substitute({'name':self.citizen_name}), 'html')
#                 
#         with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#             smtp.ehlo()
#             smtp.starttls()
#             smtp.login('*********', '**********')
#             smtp.send_message(email)
#         
        # using internal mail system
        #mail_epass_request = {
 
        #'email_from':'tn_gov@gov.in',
         
        #'email_to': self.citizen_email,
         
        #'subject': ' Appointment request approved ',
         
        #'body_html': 'Dear ' +self.citizen_name+', <br><br> Your E-pass has been approved. <br> Please visit website and download the epass  <br>Thanks & Regards<br>TN Epass Management',
         
         
        #}
         
        #mail = self.env['mail.mail'].create(mail_epass_request)
         
        #mail.send()
    
    @api.multi
    def batch_reject_epass(self):
        if self.state == 'confirm':
            self.sudo().update({
            
            'state': 'rejected'
            
            })
            
    @api.model
    def create_epass_application(self,dicts):
        epass_app_no=self.env['ir.sequence'].next_by_code('increment_epass_app_no')
        #dicts[0]['epass_app_no']=epass_app_no
        dicts["epass_app_no"] = epass_app_no
        _logger.info(str(dicts))
        self.create(dicts)  
        return epass_app_no
        
        