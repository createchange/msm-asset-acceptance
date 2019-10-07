#for python 3 install fpdf package "pip install fpdf".
from fpdf import FPDF, HTMLMixin
#class object FPDF() which is predefiend in side the package fpdf.

# Sample data - delete when transferring to actual script
user_name = "Jonathan Weaver"
selected_assets = [{"000000": ["laptop", "serial1", "Dell", "Precision 7970"]}, {"000001": ["monitor","serial2","Dell","P2717H"]}]

# These are the bullet pointed terms and conditions
terms_and_conditions = """
<ul><li><font size='14'>Prior to being issued an MSM laptop or computer, staff members will sign the Loaned Hardware Acceptance Form and agree to all outlined policies</font></li></ul>
<ul><li><font size='14'>Staff members should not attempt to install software or hardware or change the configuration including network settings without prior approval from the IT Tech Services Department.</font></li></ul>
<ul><li><font size='14'>Staff members are expected to protect MSM's laptop from damage and theft.</font></li></ul>
<ul><li><font size='14'>Each staff member is monetarily responsible for any hardware damaage that occurs off of business premises.</font></li></ul>
<ul><li><font size='14'>Staff members will not be held liable for computer problems due to regular business-related use.</font></li></ul>
"""

# This compiles a list containing each selected asset. Each list items is a single line table, used for an argument to PDF.write_html(arg)
asset_table_entries = []
for asset in selected_assets:
    for k,v in asset.items():
        asset = f'<table border="0" align="left" width="100%"><thead><tr><th width="60%"><th width="20%"><th width="20%"></th></tr></thead><tbody><tr><td><font size="14"><b>Manufacturer/Model: {v[2]} {v[3]}</font></td><td><font size="14"><b>SN: {v[1]}</b></font></td><td><font size="14"><b>Asset Tag: {k}</b></font></td></tr></tbody></table>'
        asset_table_entries.append(asset)

def create_pdf(user_name, selected_assets):
    class PDF(FPDF, HTMLMixin):
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

#    document=PDF()
    document=PDF(orientation='P', unit='mm', format='A4')
    document.add_page()

    #font size setting of the page 
    document.set_font("Arial", size=10)
    document.write_html(f"<font size='16'><b>{user_name},</b></font>")
    document.ln()
    document.write_html("<font size='14'><p>Laptops and other loaned hardware resources are to be used primarily as a productivity tool for MSM related business, research and communications. All laptops, as well as related equipment and accessories, are MSM's sole property and are provided to staff members for a period of time as deemed appropriate by MSM's administration. Equipment must be returned prior to departure or upon termination. Staff members may use MSM's laptops for limited personal purposes subject to the policy. As a condition of their use of MSM's laptop computers, staff members must agree to, and comply with, all of the following:</p></font>")
    document.ln()
    document.write_html(terms_and_conditions)
    document.ln()
#    document.cell(200, 10, txt="Description of loaned hardware:",ln=1, align="L")
#    document.write_html('<h2 style="color:#000">Description of loaned hardware:</h2>')
    document.ln()
    document.write_html('<p><font size="16"><b>Description of loaned hardware:</b></text></p>')
    document.ln()
    document.ln()
    for asset in asset_table_entries:
        document.write_html(asset)
#    document.cell(200, 20, txt="Please sign to acknowledge that you are accepting responsiblity for these assets.",ln=1, align="L")
    document.write_html("<font size='14'><p>Please sign to acknowledge that you are accepting responsibility for these assets.</p></font>")
    document.ln()
    document.write_html("<font size='14'><p>Sincerely,</p></font>")
    document.write_html("<font size='14'><p>INT Technical Services</p></font>")
#    document.write_html(asset_list)
    #pdf file naming.
    document.output("output/%s-asset-agreement.pdf" % user_name.lower().replace(' ',"-"))
    #creating page format A4 Or A3 Or ...
    document=FPDF(orientation='P', unit='mm', format='A4')

create_pdf(user_name, selected_assets)
