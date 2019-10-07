#for python 3 install fpdf package "pip install fpdf".
from fpdf import FPDF
#class object FPDF() which is predefiend in side the package fpdf.

def create_pdf(user_name, selected_assets):
    class PDF(FPDF):
        def header(self):
            # Logo
            self.image('images/INT-Logo.png', 10, 8, 33)
            # Arial bold 15
            self.set_font('Arial', 'B', 15)
            # Move to the right
            self.cell(80)
            # Title
            self.cell(30, 10, 'Inventory Acceptance Form', 0, 0, 'C')
            # Line break
            self.ln(30)

    document=PDF()
    document.add_page()

    #font size setting of the page 
    document.set_font("Arial", size=12)
    #txt message will displayed on pdf page  at the center.
    document.cell(200, 10, txt="%s," % user_name,ln=1, align="L")
    document.cell(200, 10, txt="The following assets have been assigned to you while you work from home:",ln=1, align="L")
    document.cell(200, 10, txt="",ln=1, align="L")
    for asset in selected_assets:
        for k,v in asset.items():
            document.set_font("Arial", 'B',size=12)
            document.cell(200, 10, txt="%s:" % (v[0]), ln=1, align="L")
            document.set_font("Arial", size=12)
            document.cell(200, 10, txt="Manufacturer/Model: %s %s" % (v[2], v[3]), ln=1, align="L")
            document.cell(200, 10, txt="SN: %s" % v[1], ln=1, align="R")
            document.cell(200, 10, txt="Serial: %s" % v[1], ln=1, align="L")
            document.cell(200, 10, txt="Asset Tag: %s" % k, ln=1, align="L")
            document.cell(200, 5, txt="", ln=1, align="L")
    document.cell(200, 20, txt="Please sign to acknowledge that you are accepting responsiblity for these assets.",ln=1, align="L")
    document.cell(200, 10, txt="Sincerely,",ln=1, align="L")
    document.set_font("Arial", 'B',size=12)
    document.cell(200, 10, txt="INT Technical Services",ln=1, align="L")

    #pdf file naming.
    document.output("output/%s-asset-agreement.pdf" % user_name.lower().replace(' ',"-"))
    #creating page format A4 Or A3 Or ...
    document=FPDF(orientation='P', unit='mm', format='A4')

