///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 29 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

Listbox1::Listbox1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );

	m_panel1 = new wxPanel( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	m_panel1->SetFont( wxFont( 14, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("Tw Cen MT") ) );

	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxHORIZONTAL );


	bSizer3->Add( 0, 0, 1, wxEXPAND, 5 );

	m_staticText1 = new wxStaticText( m_panel1, wxID_ANY, wxT("Cari"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer3->Add( m_staticText1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );

	m_textCtrl1 = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl1->SetFont( wxFont( 14, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("Tw Cen MT") ) );

	bSizer3->Add( m_textCtrl1, 1, wxALL|wxALIGN_CENTER_VERTICAL, 5 );

	m_button3 = new wxButton( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer3->Add( m_button3, 0, wxALL, 5 );


	bSizer2->Add( bSizer3, 0, wxEXPAND, 5 );

	m_listBox1 = new wxListBox( m_panel1, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, wxLB_NEEDED_SB|wxLB_SORT );
	m_listBox1->Append( wxT("list&of&occupation") );
	m_listBox1->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	bSizer2->Add( m_listBox1, 1, wxALL|wxEXPAND, 5 );

	m_listCtrl1 = new wxListCtrl( m_panel1, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLC_EDIT_LABELS|wxLC_REPORT );
	bSizer2->Add( m_listCtrl1, 1, wxALL|wxEXPAND, 5 );

	wxFlexGridSizer* fgSizer1;
	fgSizer1 = new wxFlexGridSizer( 0, 2, 0, 0 );
	fgSizer1->AddGrowableCol( 0 );
	fgSizer1->AddGrowableCol( 1 );
	fgSizer1->AddGrowableRow( 0 );
	fgSizer1->SetFlexibleDirection( wxBOTH );
	fgSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );

	cancel = new wxButton( m_panel1, wxID_ANY, wxT("Cancel"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( cancel, 0, wxALL|wxALIGN_CENTER_VERTICAL|wxALIGN_RIGHT, 5 );

	ok = new wxButton( m_panel1, wxID_ANY, wxT("Ok"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( ok, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );


	bSizer2->Add( fgSizer1, 0, wxEXPAND|wxALIGN_RIGHT, 5 );


	m_panel1->SetSizer( bSizer2 );
	m_panel1->Layout();
	bSizer2->Fit( m_panel1 );
	bSizer1->Add( m_panel1, 1, wxEXPAND | wxALL, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_textCtrl1->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( Listbox1::m_textCtrl1OnText ), NULL, this );
	m_button3->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( Listbox1::m_button3OnButtonClick ), NULL, this );
	m_listCtrl1->Connect( wxEVT_LEFT_DCLICK, wxMouseEventHandler( Listbox1::m_listCtrl1OnLeftDClick ), NULL, this );
}

Listbox1::~Listbox1()
{
	// Disconnect Events
	m_textCtrl1->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( Listbox1::m_textCtrl1OnText ), NULL, this );
	m_button3->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( Listbox1::m_button3OnButtonClick ), NULL, this );
	m_listCtrl1->Disconnect( wxEVT_LEFT_DCLICK, wxMouseEventHandler( Listbox1::m_listCtrl1OnLeftDClick ), NULL, this );

}
