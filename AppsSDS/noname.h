///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 29 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/listbox.h>
#include <wx/listctrl.h>
#include <wx/panel.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class Listbox1
///////////////////////////////////////////////////////////////////////////////
class Listbox1 : public wxFrame
{
	private:

	protected:
		wxPanel* m_panel1;
		wxStaticText* m_staticText1;
		wxTextCtrl* m_textCtrl1;
		wxButton* m_button3;
		wxListBox* m_listBox1;
		wxListCtrl* m_listCtrl1;
		wxButton* cancel;
		wxButton* ok;

		// Virtual event handlers, overide them in your derived class
		virtual void m_textCtrl1OnText( wxCommandEvent& event ) { event.Skip(); }
		virtual void m_button3OnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void m_listCtrl1OnLeftDClick( wxMouseEvent& event ) { event.Skip(); }


	public:

		Listbox1( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Cari Pekerjaan"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,300 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~Listbox1();

};

