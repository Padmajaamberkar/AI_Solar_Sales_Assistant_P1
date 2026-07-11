
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(customer, mobile, city, result):

    file_name = "reports/Solar_Proposal.pdf"

    doc = SimpleDocTemplate(file_name)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Solar Sales Assistant</b>", styles["Title"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Customer Name:</b> {customer}", styles["Normal"]))
    story.append(Paragraph(f"<b>Mobile:</b> {mobile}", styles["Normal"]))
    story.append(Paragraph(f"<b>City:</b> {city}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Solar Recommendation</b>", styles["Heading2"]))

    story.append(Paragraph(f"System Size : {result['system_kw']} kW", styles["Normal"]))
    story.append(Paragraph(f"Panels Required : {result['panels']}", styles["Normal"]))
    story.append(Paragraph(f"Roof Area Required : {result['roof_required']} sq.ft", styles["Normal"]))
    story.append(Paragraph(f"Installation Cost : ₹{result['installation_cost']:,}", styles["Normal"]))
    story.append(Paragraph(f"Government Subsidy : ₹{result['subsidy']:,}", styles["Normal"]))
    story.append(Paragraph(f"Final Cost : ₹{result['final_cost']:,}", styles["Normal"]))
    story.append(Paragraph(f"Monthly Generation : {result['monthly_generation']} Units", styles["Normal"]))
    story.append(Paragraph(f"Monthly Savings : ₹{result['monthly_savings']:,}", styles["Normal"]))
    story.append(Paragraph(f"Yearly Savings : ₹{result['yearly_savings']:,}", styles["Normal"]))
    story.append(Paragraph(f"Payback Period : {result['payback']} Years", styles["Normal"]))

    doc.build(story)

    return file_name
