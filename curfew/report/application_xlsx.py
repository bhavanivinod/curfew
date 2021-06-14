from odoo import models
import logging  
_logger = logging.getLogger(__name__)

class ApplicationXlsx(models.AbstractModel):
    _name = 'report.curfew.application_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        cr = self.env.cr
        query="""SELECT district_name, COUNT(epass_app_no) AS applied ,
        CASE
        WHEN state='approved' THEN COUNT(epass_app_no)
        END approved,
        CASE
        WHEN state='rejected' THEN COUNT(epass_app_no)
        END rejected
        FROM curfew_epass GROUP BY state, district_name
        """
        cr.execute(query)
        datas=cr.fetchall()
        sheet = workbook.add_worksheet('Epass_Report')
        sheet.write(0,0,'District Name')
        sheet.write(0,1,'Applied')
        sheet.write(0,2,'Approved')
        sheet.write(0,3,'Rejected')
        
        i=0
        for data in datas:
            sheet.write(i+1,0,data[0])
            sheet.write(i+1,1,data[1])
            sheet.write(i+1,2,data[2])
            sheet.write(i+1,3,data[3])
            i=i+1
                
        chart1 = workbook.add_chart({'type': 'bar', 'subtype': 'stacked'})
        chart1.add_series({
            'name':       '=Epass_Report!$C$1',
            'categories': '=Epass_Report!$A$2:$A$7',
            'values':     '=Epass_Report!$C$2:$C$7',
        })
        chart1.add_series({
            'name':       '=Epass_Report!$D$1',
            'categories': '=Epass_Report!$A$2:$A$7',
            'values':     '=Epass_Report!$D$2:$D$7',
        })

        
        # Add a title.
        chart1.set_title({'name': 'Epass Status'})
        chart1.set_x_axis({'name': 'Number of passes approved'}) 
          
        # Add y-axis label 
        chart1.set_y_axis({'name': 'District Name'}) 
          
        # Set an Excel chart style. 
        chart1.set_style(12) 
        # Insert the chart into the worksheet (with an offset).
        sheet.insert_chart('C10', chart1, {'x_offset': 25, 'y_offset': 10})