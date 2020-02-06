# -*- coding: utf-8 -*-

###########################################################################
# # Python code generated with wxFormBuilder (version Oct 29 2018)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
from AppsSDS.TempListbox import TempListbox

###########################################################################
# # Class Page2
###########################################################################


class Page2 (wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__ (self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"OCCUPATIONAL DAYDREAM", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        bSizer10.Add(self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        fgSizer71 = wx.FlexGridSizer(0, 4, 0, 0)
        fgSizer71.AddGrowableCol(1)
        fgSizer71.SetFlexibleDirection(wx.BOTH)
        fgSizer71.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        fgSizer71.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.textctrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        fgSizer71.Add(self.textctrl1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.openlistbox1 = wx.Button(self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.openlistbox1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.label1 = wx.StaticText(self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label1.Wrap(-1)

        fgSizer71.Add(self.label1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        fgSizer71.Add(self.m_staticText10, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.textctrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        fgSizer71.Add(self.textctrl2, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.openlistbox2 = wx.Button(self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.openlistbox2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.label2 = wx.StaticText(self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label2.Wrap(-1)

        fgSizer71.Add(self.label2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText132 = wx.StaticText(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText132.Wrap(-1)

        fgSizer71.Add(self.m_staticText132, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.textctrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.textctrl3, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.openlistbox3 = wx.Button(self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.openlistbox3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.label3 = wx.StaticText(self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label3.Wrap(-1)

        fgSizer71.Add(self.label3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText134 = wx.StaticText(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText134.Wrap(-1)

        fgSizer71.Add(self.m_staticText134, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textctrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.textctrl4, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.openlistbox4 = wx.Button(self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.openlistbox4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.label4 = wx.StaticText(self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label4.Wrap(-1)

        fgSizer71.Add(self.label4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText138 = wx.StaticText(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText138.Wrap(-1)

        fgSizer71.Add(self.m_staticText138, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textctrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.textctrl5, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.openlistbox5 = wx.Button(self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.openlistbox5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.label5 = wx.StaticText(self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label5.Wrap(-1)

        fgSizer71.Add(self.label5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText139 = wx.StaticText(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText139.Wrap(-1)

        fgSizer71.Add(self.m_staticText139, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.textctrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.textctrl6, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        self.openlistbox6 = wx.Button(self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer71.Add(self.openlistbox6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.label6 = wx.StaticText(self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label6.Wrap(-1)

        fgSizer71.Add(self.label6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer10.Add(fgSizer71, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer10)
        self.Layout()

        # Connect Events
        self.textctrl1.Bind(wx.EVT_TEXT, self.textctrl1OnText)
        self.openlistbox1.Bind(wx.EVT_BUTTON, self.openlistbox1OnButtonClick)
        self.textctrl2.Bind(wx.EVT_TEXT, self.textctrl2OnText)
        self.openlistbox2.Bind(wx.EVT_BUTTON, self.openlistbox2OnButtonClick)
        self.textctrl3.Bind(wx.EVT_TEXT, self.textctrl3OnText)
        self.openlistbox3.Bind(wx.EVT_BUTTON, self.openlistbox3OnButtonClick)
        self.textctrl4.Bind(wx.EVT_TEXT, self.textctrl4OnText)
        self.openlistbox4.Bind(wx.EVT_BUTTON, self.openlistbox4OnButtonClick)
        self.textctrl5.Bind(wx.EVT_TEXT, self.textctrl5OnText)
        self.openlistbox5.Bind(wx.EVT_BUTTON, self.openlistbox5OnButtonClick)
        self.textctrl6.Bind(wx.EVT_TEXT, self.textctrl6OnText)
        self.openlistbox6.Bind(wx.EVT_BUTTON, self.openlistbox6OnButtonClick)

        self.listprofesiona = {'Abstractor': 'CSI', 'Academic Advisor': 'SEC', 'Account Executive': 'AES', 'Accountant': 'CSI', 'Accountant, Cost': 'CIE', 'Accountant, Property': 'CER', 'Accountant, Systems': 'CSE', 'Accountant, Tax': 'ECS', 'Accountant Clerk': 'CSR', 'Acquisitions Librarian': 'SAI', 'Auditor, Internal': 'ICR', 'Auto Design Detailer': 'IRE', 'Automobile Body Repair Supervisor': 'SER', 'Automobile Body Repairer': 'RIE', 'Automobile Detailer': 'RCE', 'Automobile Mechanic': 'RCI', 'Automobile Racer': 'RES', 'Automobile Rental Clerk': 'ESC', 'Automobile Service Station Attendant': 'RES', 'Automobile Service Station Mechanic': 'RIC', 'Automobile Tester, Governmental Services': 'RCE', 'Automobile Engineering Technician': 'RIC', 'B': None, 'Baggage and Mail Agent': 'ERS', 'Baggage Handler': 'REC', 'Bailiff': 'ESR', 'Baker': 'RSE', 'Ballistics Expert, Forensic': 'IRE', 'Bank Examiner': 'EIC', 'Bank Teller': 'CSE', 'Bank Teller Supervisor': 'SEC', 'Barber': 'ESR', 'Barista': 'ECS', 'Bartender': 'SEC', 'Bibliographer': 'CSR', 'Bicycle Repairer': 'RSC', 'Billing Clerk': 'CRS', 'Bindery Worker, Printing and Publishing': 'REC', 'Biochemist': 'IRS', 'Biofuel Processing Technician': 'RCI', 'Bioinformatics Scientist': 'ICR', 'Bioinformatics Technician': 'ICS', 'Biological Aide': 'RSI', 'Biological Scientist': 'IRC', 'Biologist': 'IAR', 'Biomass Plant Technician': 'RCI', 'Biomedical Equipment Technician': 'RIE', 'Biophysicist': 'IRE', 'Biostatistician': 'IRC', 'Blaster': 'RIE', 'Blind Aide': 'SCE', 'Boat Outfitter': 'REI', 'Boat Repairer': 'RES', 'Bodyguard': 'ESC', 'Boilermaker': 'RCE', 'Bookbinder': 'RES', 'Border Guard': 'SRE', 'Botanist': 'IRS', 'Bricklayer': 'REI', 'Bricklayer Supervisor': 'ERS', 'Bridge Inspector': 'RSI', 'Broadcast Checker': 'CER', 'Broadcast News Analyst': 'AES', 'Broadcast Technician': 'RCS', 'Brokerage Clerk': 'CSR', 'Budget Analyst': 'CER', 'Budget Clerk': 'CSR', 'Budget Officer': 'ESI', 'Building Cleaner': 'RCS', 'Building Inspector': 'CIE', 'Building Insulation Supervisor': 'ECS', 'Building Superintendent': 'RES', 'Bulldozer Operator': 'REC', 'Bureau Chief': 'AES', 'Business Consultant': 'IER', 'Business Continuity Planner': 'EIC', 'Business Enterprise Officer': 'EIR', 'Business Intelligence Analyst': 'IEC', 'Business Manager, College or University': 'ESR', 'Business Representative, Labor Union': 'ESA', 'Butcher': 'RSE', 'Buyer': 'ESC', 'Buyer, Farm Products': 'EIS', 'C': None, 'Cabinet Assembler': 'CSR', 'Cabinetmaker': 'RIS', 'Cable Splicer': 'RCS', 'Cake Decorator': 'ARE', 'Calibration Laboratory Technician': 'RCI', 'Camera Operator, Television, Video, and Film': 'RIC', 'Camera Repairer': 'RCE', 'Camp Director': 'ERS', 'Cardiologist': 'ISE', 'Cardiopulmonary Technologist': 'ISR', 'Casdiovascular Technologist and Technician': 'SIR', 'Career Counselor': 'SAR', 'Cargo and Freight Agent': 'CSE', 'Carpenter': 'RCE', 'Carpet Layer': 'REI', 'Cartoonist': 'AES', 'Philebotomist ': 'SRI', 'Photo Technician': 'RCI', 'Photogrammetrist': 'IRC', 'Photograph Retoucher': 'RCA', 'Photographer, Still': 'ARS', 'Photographic Process Worker': 'REI', 'Photojournalist': 'AEC', 'Physitrist': 'IRE', 'Physical Eeductaion Instructor': 'SER', 'Physical Therapist': 'SIE', 'Physical Therapist Assistant': 'SCR', 'Physical Therapy Aide': 'ESC', 'Physician Assistant': 'ISA', 'Physician, General Practioner': 'ISE', 'Physician, Internist': 'ISA', 'Physician, Naturopathic': 'SIR', 'Physician, Nuclear Medicine': 'SIE', 'Physician, Occupational ': 'ISC', 'Physician, Osteopathic Medicine': 'ISR', 'Physician, Preventive Medicine': 'ISA', 'Physician, Sports Medicine': 'ISR', 'Physicist': 'IRE', 'Physiologist': 'IRE', 'Piano Technician': 'RAE', 'Piano Tuner': 'RCS', 'Picture Framer': 'RCE', 'Pilot, Airplane': 'IRE', 'Pilot, Commercial Airplane': 'RIE', 'Pilot, Executive': 'RIE', 'Pilot, Helicopter': 'RIS', 'Pilot, Highway Patrol': 'ERS', 'Pipe Fitter': 'RCE', 'Pipelayer': 'RCE', 'Pipelines Supervisor': 'REC', 'Placement Director': 'ESA', 'Planetarium Technician': 'RCI', 'Plant Pathologist': 'IRS', 'Plant Supervisor': 'SRE', 'Plasterer and Stucco Mason': 'RES', 'Plating and Coating Machine Operator': 'RIE', 'Playwright': 'ASE', 'Plumber': 'REI', 'Podiatrist': 'SIR', 'Poet': 'AES', 'Police Captain, Precinct': 'ERS', 'Police Officer': 'SER', 'Police Officer, Crime Prevention': 'SCR', 'Police Officer, Safety Instruction': 'SCE', 'Police Officer, State Highway': 'RSE', 'Political Scientist': 'SEI', 'Politician': 'ESA', 'Pllution Control Technician': 'RSI', 'Polygrapgh Examiner': 'CIS', 'Post Office Clerk': 'CSE', 'Postal Service Mail Carrier': 'CRS', 'Pstmaster': 'ESR', 'Precision Agriculture Technician': 'RIC', 'Preparation Plant Supervisor': 'EAR', 'Prepress Technician': 'ARE', 'President, Educational Institution': 'ESR', 'President, Financial Institution': 'SEI', 'Press Operator': 'RSC', 'Preventive Maintenance Coordinator': 'CRE', 'Print Binding and Finishing Worker': 'RCA', 'Printed Circuit Desiger': 'IRC', 'Printing Machine Operator': 'RCI', 'Printmaker': 'AES', 'Private  Investigator': 'ESI', 'Probation/Parole Officer': 'SIE', 'Process Artist, Printing and Publishing ': 'REA', 'Process Server': 'ESC', 'Procurement Clerk': 'CES', 'Producer, Film': 'ESA', 'Producer, Radio and TV': 'SEA', 'Production Clerk': 'CSR', 'Production Coordinator': 'ESR', 'Production Laborer': 'RCS', 'Production Manager': 'ERC', 'Production Manager, Advertising': 'ASE', 'Production Planner': 'REI', 'Production Superintendent, Agriculture': 'EIR', 'Program Administrator, Alcohol and Drug Abuse Assistance': 'ESR', 'Program Coordinator, Amusement and Recreation': 'AES', 'Program Manager': 'EIR', 'Program Services Planner': 'EIS', 'Project Manager, Environmental Research': 'EIS', 'Projectionist, Chief': 'SCR', 'Proofreader': 'CSI', 'Property Clerk': 'CRS', 'Prospector': 'RIS', 'Prosthetics Technician': 'RIE', 'Prosthetist': 'RSE', 'Prosthodontist': 'ISR', 'Psychiatric Aide': 'SEC', 'Psychiatric Aide Instructor': 'SCE', 'Psychiatric Aide, Mentally Challenged': 'SRI', 'Psychiatric Technician': 'SIE', 'Psychiatrist': 'ISA', 'Psychologist, Chief': 'ISE', 'Psychologist, Clinical': 'SIA', 'Psychologist, Counseling': 'SIA', 'Psychologist, Educational': 'IES', 'Psychologist, Experimental': 'IES', 'Psychologist, Industrial-Organizational': 'IES', 'Psychologist, School': 'SEI', 'Psychometrist': 'IES', 'Public Health Service Officer': 'IES', 'Public Relations Representative': 'ASE', 'Public Relations Specialist': 'AES', 'Pulmonary Function Technician': 'IRC', 'Puppeteer': 'AEI', 'Purchasing Agent': 'ESR', 'Purification Operator': 'RSE', 'Q': None, 'Quality Assurance Analyst/Tester': 'RIC', 'Quality Control Analyst': 'IRC', 'Quality Control Clerk, Drug Preparation and Relate prodducts': 'CSR', 'Quality Control Coordinator': 'CES', 'Quality Control Technician, Food Preparation': 'REI', 'Quality Control Technician, Manufactured Products': 'RCI', 'R': None, 'Radiation Monitor': 'RCS', 'Radiation Protection Specialist': 'IRS', 'Radiation Therapy Technologist': 'RIS', 'Radio Frequency Identification Device Specialist': 'RIC', 'Radio Operator': 'RCE', 'Radio Cellular, and Tower Equipment Installer and Repairer': 'RIE', 'Radiologic Technician': 'SRI', 'Radiologic Technologist': 'SRI', 'Radiologic Technologist, Chief': 'ISE', 'Radiological Equipment Specialist': 'RES', 'Radiologist': 'IRS', 'Radiopharmacist': 'IRC', 'Railway Equipment Operator': 'ERA', 'Range Manager': 'IRS', 'Rate Analyst, Freight': 'CSE', 'Real Estate Broker': 'ECS', 'Receipt and Report Clerk': 'CRI', 'Receptionist': 'CSE', 'Recreation Aide': 'SCR', 'Recreation Leader': 'SEI', 'Recreation Supervisor': 'ESA', 'Recreational Therapist': 'SEC', 'Recruiter': 'SRE', 'Recycling and Reclamation Worker': 'RCS', 'Recycling Coordinator': 'ERC', 'Referral Clerk, Temporary Employment Agency': 'CES', 'Refinery Operator, Grain': 'RES', 'Refrigeration Mechanic': 'RES', 'Refuse and Recyclable Material Collector': 'RCS', 'Registrar, College or University': 'ESC', 'Registrar, Museum': 'CER', 'Regulatory Affairs Specialists': 'CEI', 'Reinforcing Iron and Rebar Worker': 'RCI', 'Remote Sensing Scientist/Technologist': 'IRC', 'Remote Sensing Technician ': 'IRC', 'Repairer, Art Objects': 'RCE', 'Repairer, Electronics and Computers ': 'RIS', 'Repairer, Welding Equipment': 'REI', 'Reporter/News Correspondent': 'ASI', 'Research Contracts Supervisor': 'SEI', 'Research Director': 'SEA', 'Reservation Clerk': 'CES', 'Reservations Agent, Air Transportation': 'CES', 'Residental Advisor': 'SEC', 'Respiratory Therapist': 'SIR', 'Respiratory Therapy Aide': 'SRC', 'Respiratory Therapy Technician': 'SRI', 'Restorer, Ceramic': 'ASI', 'Restorer, Paintings': 'ASR', 'Restorer, Paper and Prints': 'AIS', 'Revenue Agent': 'ERI', 'Rigger': 'RSC', 'Risk Management Specialist': 'EIC', 'Road Supervisor': 'ERI', 'Robot Technician': 'IRS', 'Roofer ': 'REC', 'Roustabout, Oil and Gas': 'RCI', 'Route Supervisor': 'SER', 'S': None, 'Safety Clothing and Equipment Designer': 'AER', 'Safety Inspector': 'RCS', 'Safety Inspector, Truck': 'REC', 'Safety Manager, Medical Services': 'SEC', 'Sales Agent, Financial Services': 'ESC', 'Sales Agent, Insurance': 'ESC', 'Sales Agent, Real Estate': 'ESC', 'Sales Agent, Securities and Commodities': 'EAS', 'Sales Clerk': 'ESR', 'Sales Correspondent': 'ERS', 'Sales Representative , Advertising': 'ESR', 'Sales Representative, Farm and Garden Equipment and Supplies': 'ESR', 'Sales Representative, Footwear': 'ESA', 'Sales Representative, Graphic Art': 'AES', 'Sales Representative, Hobbies and Crafts': 'ESR', 'Sales Representative, Household Appliances': 'ESA', 'Sales Representative, Office Machines': 'ESR', 'Sales Representative, Security Systems': 'ERI', 'Sales Representative, Technical and Scientific Products': 'ESR', 'Salesperson, Apparel and Accessories': 'EAS', 'Salesperson, Automobiles': 'ESR', 'Salesperson, Books': 'ESC', 'Salesperson, Cosmetics and Toiletries': 'ESA', 'Salesperson, Flowers': 'AER', 'Salesperson, General Merchandise': 'ESA', 'Salesperson, Musical Instruments and Accessories': 'ESA', 'Salesperson, Pianos and Organs': 'ESR', 'Salesperson, Sporting Goods': 'ESA', 'Sampler, Minerals and Eraths': 'ECR', 'Sanitarian': 'ISR', 'Sanitation Inspector': 'ERS', 'Sanitation Superintendent': 'ESI', 'Sanitation Supervisor': 'ERI', 'Satellite Communications Technician': 'RCI', 'Sawing Machine Operator': 'RIC', 'Scenic Arts Supervisor': 'AES', 'Schedule Maker': 'ERI', 'School Crossing Guard': 'ESC', 'School Principal': 'SEI', 'School/Guidance Counselor': 'SCE', 'Screen Writer': 'AEI', 'Scuba Diver': 'REI', 'Sculptor': 'AER', 'Search Marketing Strategist': 'EIS', 'Secretary': 'CSE', 'Securities Clerk': 'CSE', 'Securities Trader, Financial': 'ECS', 'Security and Fire Alarm Systems Installer': 'RCS', 'Security Consultant ': 'ESC', 'Security Guard': 'SEC', 'Security Manager': 'EIC', 'Seismologist': 'IRE', 'Semiconductor Technician': 'ERC', 'Service Manager, Automobile Services': 'ESR', 'Service Unit Operator, Oil, Gas, and Mining': 'RCI', 'Set Decorator, Theater and Film': 'AES', 'Set Designer, Theater and Film': 'AIE', 'Sewer System Supervisor': 'EIR', 'Sewing Machine Operator': 'CSR', 'Sheet Metal Worker': 'REI', 'Sheriff/Deputy Sheriff': 'REC', 'Ship Captain': 'ERI', 'Ship Mate': 'ERS', 'Ship Pilot': 'REI', 'Shipfitter': 'RIE', 'Shipping and Receiving Clerk': 'REI', 'Shipping anf Receiving, Order Clerk': 'CES', 'Shoe Repairer': 'RSE', 'Shopping Investigator': 'ESC', 'Show Operations Supervisor': 'ASE', 'Sign Shop Supervisor': 'AES', 'Silversmith': 'RSC', 'Siger': 'AES', 'Singing Messenger': 'ASC', 'Skin Care Specialist': 'RSA', 'Small Engine Mechanic': 'REC', 'Social Director': 'ESC', 'Social Science Research Assistant': 'CIS', 'Social Services Aide': 'SCE', 'Social Welfare Administrator': 'ESA', 'Social Worker ': 'SEC', 'Sociologist': 'IES', 'Software Developer': 'IRC', 'Software Quality Assurance Engineer and Tester': 'ICR', 'Soil Conservation Technician': 'IRC', 'Soil Conservationist': 'IRE', 'Solar Energy Systems Designer': 'RIC', 'Solar Fabrication Technician': 'RCI', 'Solar Photovoltaic Installer': 'RCI', 'Solar Sales Representative and Assessor': 'ESC', 'Solar Thermal Installer/Technician': 'RCI', 'Solderer and Brazer': 'CRS', 'Sound Effects Technician': 'RAE', 'Sound Mixer ': 'RCS', 'Sound Technician': 'RIE', 'Special Agent, Customs': 'SRI', 'Special Agent, Governmental Services': 'ERI', 'Special Education Supervisor': 'SEC', 'Speech-Language Pathologist': 'SAI', 'Speech-Language Pathology Assistant': 'SRC', 'Stage Manager': 'ESC', 'Stage Technician': 'ARS', 'Statement Clerk': 'CSE', 'Station Manager, Radio and TV': 'ESR', 'Station Manager, Railroad': 'ESC', 'Statistical Assistant': 'ICS', 'Statistician': 'IRE', 'Stock Clerk': 'RCE', 'Stock Control Clerk': 'CRI', 'Stock Transfer Clerk': 'CER', 'Stockbroker': 'EAS', 'Stone Carver': 'ARE', 'Stonemason': 'RCE', 'Stress Analyst': 'IRC', 'Structural Metal Fabricator and Fitter': 'RIS', 'Substance Abuse Counselor': 'SEA', 'Substation Operator, Utilities': 'RIS', 'Superintendent of Schools': 'SEI', 'Surgeon': 'IRA', 'Surgical Assistant': 'IRS', 'Surveillance System Monitor': 'CSR', 'Survey Researcher': 'ICE', 'Survey Worker Supervisor': 'SEC', 'Surveyor, Geodetic': 'IRE', 'Surveyor, Hydrographic': 'IER', 'Surveyor, Land': 'IER', 'Surveyor, Ship': 'REC', 'Sustainability Specialist': 'ICE', 'Switchboard Operator/Answering Service Operator': 'CSE', 'systems Analyst': 'IER', 'T': None, 'Tailor': 'RIE', 'Talent Manager': 'ESC', 'Taper/Finisher': 'RCS', 'Tax Preparer': 'CES', 'Taxicab Coordinator': 'SCE', 'Teacher Aide': 'SCE', 'Teacher, Adult Education': 'SER', 'Teacher, Art': 'ASE', 'Teacher, Drama': 'ASE', 'Teacher, Elementary School': 'SAE', 'Teacher, Elementary School, Special Education': 'SEC', 'Teacher, Industrial Arts': 'REI', 'Teacher, Kindergarten': 'SEC', 'Teacher, Middle School, Special Education': 'SEC', 'Teacher, Music': 'AES', 'Teacher, Preschool': 'SAE', 'Teacher, Preschool, Special Education': 'SEC', 'Teacher, Secondary School': 'SAE', 'Teacher, Secondaru School, Special Education': 'SEC', 'Techical Support Specialist': 'SER', 'Technical Writer': 'IRS', 'Technician, Dialysis': 'ISC', 'Technician, Surgical': 'ISR', 'Telecommunications Engineering Specialist': 'REI', 'Telecommunications Equipment Installer and Repairer': 'REI', 'Telecommunications Line Installer and Repairer': 'REI', 'Telecommunications Specialist': 'ECS', 'Telecommunications Technician': 'RIS', 'Telecommunicator Supervisor': 'ECS', 'Telemarketer': 'ESC', 'Television Production Clerk': 'CRS', 'Television Technician': 'RIA', 'Terrazo Worker and Finisher': 'REC', 'Test Technician': 'IRE', 'Ticket Sales Agent': 'CSE', 'Ticket Sales Supervisor': 'ESR', 'Tire Repairer and Changer': 'RCE', 'Tissue Technologist': 'IRE', 'Title Examiner': 'CSE', 'Tool and Die Maker': 'RCI', 'Tools Designer': 'RIS', 'Tools Programmer, Numerical Control': 'IRE', 'Town Clerk': 'ECI', 'Toxicologist': 'IRC', 'Toxicologist, Chief': 'IRE', 'Tractor Operator': 'RCE', 'Traffic Checker': 'ERC', 'Traffer Clerk': 'CRS', 'Traffic Maintenance Supervisor': 'ERI', 'Traffic Manager': 'ESR', 'Traffic Technician': 'REI', 'Train Dispatcher': 'ECS', 'Training and Development Specialist': 'SIE', 'Transportation Director': 'ESR', 'Transportation Inspector': 'CRS', 'Transportation Manager': 'ERA', 'Transportation Planner': 'ICR', 'Transportation Security Officer': 'REC', 'Travel Agent': 'ECS', 'Tree Surgeon': 'REI', 'Tree Trimmer/Pruner': 'RCE', 'Tutor': 'SEC', 'Typist/Transcriptionist': 'CRS', 'U': None, 'Ultrasound Technologist': 'RSI', 'Umpire/Referee': 'ESR', 'Underwriter': 'CSE', 'Upholsterer': 'RCS', 'Upholsterer, Chair and Furiture': 'RSC', 'Urban Planner': 'ESI', 'Urologist': 'ISR', 'Usher, Lobby Attendant, and Ticket Taker': 'SCR', 'Utilities Service Investigator': 'EIR', 'Utility Clerk': 'CER', 'V': None, 'Vendor Quality Supervisor': 'EIA', 'Veteranian': 'IRS', 'Veterinary Assistant': 'RSI', 'Veterinary Livestock Inspector': 'IRE', 'Veterinary Technologist and Technician': 'IRS', 'Video Game Designer': 'AIE', 'Video Game Programmer': 'IRE', 'Vision Rehabilitation Therapist': 'SER', 'Vocational Rehabilitation Consultant': 'ESR', 'Vocational Rehabilitation Counselor': 'SEC', 'Voice Pathologist': 'IER', 'Volunteer Services Supervisor': 'ESR', 'W': None, 'Waiter/Waitress': 'ESC', 'Waiter/Waitress, Head': 'ESR', 'Warehouse Supervisor': 'ESR', 'Watch Repairer': 'REI', 'Water Quality Tester': 'REI', 'Water Resources Specialist': 'IRC', 'Water Treatment Plant Operator': 'RCE', 'Water Treatment Plant Supervisor': 'EIR', 'Water/Sewer Systems Superintendent': 'IER', 'Weather Observer ': 'RIE', 'Weatherization Installer/Technician': 'RIC', 'Weaver, Carpet and Rug': 'RCE', 'Web Administrator': 'IER', 'Web Developer/Designer': 'ACI', 'Wedding Consultant': 'SEC', 'Welder': 'RIS', 'Welding Machine Operator': 'RIE', 'Welfare Director': 'SEC', 'Wholesaler': 'ESA', 'Wildlife Control Agent': 'RSE', 'Wind Energy Project Manager': 'IRC', 'Wind Turbine Service Technician': 'RIC', 'Wine Maker': 'EIR', 'Woodworking Machine Operator': 'RIC', 'Winter, Fiction and Nonfiction': 'AIE', 'Y': None, 'Yard Manager, Railroad Transportation': 'ESC', 'Z': None, 'Zoo Veterinarian': 'ISE', 'Zoologist': 'IRE'}

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def openlistbox1OnButtonClick(self, event):
        print("tes")
        self.op_tomb = 1

        self.runList = TempListbox(self)
        self.runList.Show()
        
        event.Skip()
        
    def openlistbox2OnButtonClick(self, event):
        print("tes2")
        self.op_tomb = 2

        self.runList = TempListbox(self)
        self.runList.Show()
        event.Skip()

    def openlistbox3OnButtonClick(self, event):
        print("tes3")

        self.op_tomb = 3

        self.runList = TempListbox(self)
        self.runList.Show()
        event.Skip()

    def openlistbox4OnButtonClick(self, event):
        print("tes4")
        self.op_tomb = 4

        self.runList = TempListbox(self)
        self.runList.Show()
        event.Skip()

    def openlistbox5OnButtonClick(self, event):
        print("tes5")
        self.op_tomb = 5

        self.runList = TempListbox(self)
        self.runList.Show()
        event.Skip()
    
    def openlistbox6OnButtonClick(self, event):
        print("tes6")
        self.op_tomb = 6
        self.runList = TempListbox(self)
        self.runList.Show()
        event.Skip()
        
    def textctrl1OnText(self, event):
        self.a1 = self.textctrl1.GetValue()
        self.b1 = self.listprofesiona.get(self.a1)
#         print (self.listprofesiona.get(self.a1))
        self.label1.SetLabel(self.b1)
        self.Layout()
        pass
    
    def textctrl2OnText(self, event):
        self.a2 = self.textctrl2.GetValue()
        self.b1 = self.listprofesiona.get(self.a2)
#         print (self.listprofesiona.get(self.a1))
        self.label2.SetLabel(self.b1)
        self.Layout()
        pass
    
    def textctrl3OnText(self, event):
        self.a3 = self.textctrl3.GetValue()
        self.b1 = self.listprofesiona.get(self.a3)
#         print (self.listprofesiona.get(self.a1))
        self.label3.SetLabel(self.b1)
        self.Layout()
        pass
    
    def textctrl4OnText(self, event):
        self.a4 = self.textctrl4.GetValue()
        self.b1 = self.listprofesiona.get(self.a4)
#         print (self.listprofesiona.get(self.a1))
        self.label4.SetLabel(self.b1)
        self.Layout()
        pass
    
    def textctrl5OnText(self, event):
        self.a5 = self.textctrl5.GetValue()
        self.b1 = self.listprofesiona.get(self.a5)
#         print (self.listprofesiona.get(self.a1))
        self.label5.SetLabel(self.b1)
        self.Layout()
        pass
    
    def textctrl6OnText(self, event):
        self.a6 = self.textctrl6.GetValue()
        self.b1 = self.listprofesiona.get(self.a6)
#         print (self.listprofesiona.get(self.a1))
        self.label6.SetLabel(self.b1)
        self.Layout()
        pass
    
