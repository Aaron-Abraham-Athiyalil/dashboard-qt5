from itertools import cycle

light_bg_pics = ["light_bg_pic_01.png","light_bg_pic_02.png","light_bg_pic_03.png"]

stylesheet = """
QPushButton#btn_thread 
{
    background-color: rgb(170, 255, 0);
}

QPushButton#btn_thread:hover
{ 
    background-color: blue;
    color: #31363B;
}

QPushButton#btn_thread:pressed
{
    background-color: red;
    color: #31363B;
}
QToolTip
{
    background-color: black;
    color: white;
    padding: 0.5ex;
}

QWidget
{
    color: #31363B;
    background-color: #EFF0F1;
    selection-background-color:#33A4DF;
    selection-color: #31363B;
    background-clip: border;
    border-image: none;
    border: 0px transparent black;
    outline: 0;
}
QWidget#centralwidget
{
    border-image: url(":themes/backgrounds/light_bg/bg_pic.format") 0 0 0 0 stretch stretch; 
    border-radius: 15px;
}

QWidget:item:hover
{
    background-color: #33A4DF;
    color: #31363B;
}

QWidget:item:selected
{
    background-color: #33A4DF;
}

QCheckBox
{
    spacing: 0.5ex;
    outline: none;
    color: #31363B;
    margin-bottom: 0.2ex;
    opacity: 200;
}

QCheckBox:disabled
{
    color: #BAB9B8;
}

QGroupBox::indicator
{
    margin-left: 0.2ex;
    margin-left: 0.2ex;
}

QCheckBox::indicator:unchecked,
QCheckBox::indicator:unchecked:focus
{
    border-image: url(:themes/light/checkbox_unchecked_disabled.svg);
}

QCheckBox::indicator:unchecked:hover,
QCheckBox::indicator:unchecked:pressed,
QGroupBox::indicator:unchecked:hover,
QGroupBox::indicator:unchecked:focus,
QGroupBox::indicator:unchecked:pressed
{
    border: none;
    border-image: url(:themes/light/checkbox_unchecked-hover.svg);
}

QCheckBox::indicator:checked
{
    border-image: url(:themes/light/checkbox_checked.svg);
}

QCheckBox::indicator:checked:focus,
QCheckBox::indicator:checked:pressed,
QGroupBox::indicator:checked:focus,
QGroupBox::indicator:checked:pressed
{
    border: none;
    border-image: url(:themes/light/checkbox_checked.svg);
}

QCheckBox::indicator:checked:hover,
QGroupBox::indicator:checked:hover
{
    border-image: url(:themes/light/checkbox_checked-hover.svg);
}

QCheckBox::indicator:indeterminate
{
    border-image: url(:themes/light/checkbox_indeterminate.svg);
}

QCheckBox::indicator:indeterminate:hover
{
    border-image: url(:themes/light/checkbox_indeterminate-hover.svg);
}

QCheckBox::indicator:indeterminate:focus,
QCheckBox::indicator:indeterminate:pressed
{
}

QCheckBox::indicator:indeterminate:disabled
{
    border-image: url(:themes/light/checkbox_indeterminate_disabled.svg);
}

QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled
{
    border-image: url(:themes/light/checkbox_checked_disabled.svg);
}

QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled
{
    border-image: url(:themes/light/checkbox_unchecked_disabled.svg);
}

QRadioButton
{
    spacing: 0.5ex;
    outline: none;
    color: #31363B;
    margin-bottom: 0.2ex;
}

QRadioButton:disabled
{
    color: #BAB9B8;
}

QRadioButton::indicator:unchecked,
QRadioButton::indicator:unchecked:focus
{
    border-image: url(:themes/light/radio_unchecked_disabled.svg);
}

QRadioButton::indicator:unchecked:hover,
QRadioButton::indicator:unchecked:pressed
{
    border: none;
    outline: none;
    border-image: url(:themes/light/radio_unchecked-hover.svg);
}

QRadioButton::indicator:checked
{
    border: none;
    outline: none;
    border-image: url(:themes/light/radio_checked.svg);
}

QRadioButton::indicator:checked:focus,
QRadioButton::indicator:checked:pressed
{
    border: none;
    outline: none;
    border-image: url(:themes/light/radio_checked.svg);
}

QRadioButton::indicator:checked:hover
{
    border-image: url(:themes/light/radio_checked-hover.svg);
}

QRadioButton::indicator:checked:disabled
{
    outline: none;
    border-image: url(:themes/light/radio_checked_disabled.svg);
}

QRadioButton::indicator:unchecked:disabled
{
    border-image: url(:themes/light/radio_unchecked_disabled.svg);
}

QMenuBar
{
    background-color: #EFF0F1;
    color: #31363B;
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 0.1ex solid #BAB9B8;
}

QMenuBar::item:pressed
{
    border: 0.1ex solid #BAB9B8;
    background-color: #33A4DF;
    color: #31363B;
    margin-bottom: -0.1ex;
    padding-bottom: 0.1ex;
}

QMenu
{
    border: 0.1ex solid #BAB9B8;
    color: #31363B;
    margin: 2px;
}

QMenu::icon
{
    margin: 2px;
}

QMenu::item
{
    padding: 5px 3ex 5px 25px;
    margin-left: 0.5ex;
    border: 0.1ex solid transparent; /* reserve space for selection border */
}

QMenu::item:selected
{
    color: #31363B;
}

QMenu:separator
{
    height: 2px;
    width : 2px;
    background: black;
    margin-left: 10x;
    margin-right: 5px;
}

/* non-exclusive indicator = check box style indicator
(see QActionGroup::setExclusive) */
QMenu::indicator:non-exclusive:unchecked
{
    border-image: url(:themes/light/checkbox_unchecked_disabled.svg);
}

QMenu::indicator:non-exclusive:unchecked:selected
{
    border-image: url(:themes/light/checkbox_unchecked_disabled.svg);
}

QMenu::indicator:non-exclusive:checked
{
    border-image: url(:themes/light/checkbox_checked.svg);
}

QMenu::indicator:non-exclusive:checked:selected
{
    border-image: url(:themes/light/checkbox_checked.svg);
}

/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
QMenu::indicator:exclusive:unchecked
{
    border-image: url(:themes/light/radio_unchecked_disabled.svg);
}

QMenu::indicator:exclusive:unchecked:selected
{
    border-image: url(:themes/light/radio_unchecked_disabled.svg);
}

QMenu::indicator:exclusive:checked
{
    border-image: url(:themes/light/radio_checked.svg);
}

QMenu::indicator:exclusive:checked:selected
{
    border-image: url(:themes/light/radio_checked.svg);
}

QMenu::right-arrow
{
    margin: 0.5ex;
    border-image: url(:themes/light/right_arrow.svg);
    width: 0.6ex;
    height: 0.9ex;
}


QWidget:disabled
{
    color: #454545;
    background-color: #EFF0F1;
}

QAbstractItemView
{
    alternate-background-color: #EFF0F1;
    color: #31363B;
    border: 0.1ex solid 3A3939;
    border-radius: 0.2ex;
}

QWidget:focus,
QMenuBar:focus
{
    border: 0.1ex solid #33A4DF;
}

QTabWidget:focus,
QCheckBox:focus,
QRadioButton:focus,
QSlider:focus
{
    border: none;
}

QLineEdit
{
    background-color: #FCFCFC;
    padding: 0.5ex;
    border-style: solid;
    border: 0.1ex solid #BAB9B8;
    border-radius: 0.2ex;
    color: #31363B;
}

QGroupBox
{
    border: 0.1ex solid #BAB9B8;
    border-radius: 0.2ex;
    padding-top: 1ex;
    margin-top: 1ex;
}

QGroupBox::title
{
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 0.1ex;
    padding-right: 0.1ex;
    margin-top: -0.7ex;
}

QAbstractScrollArea
{
    border-radius: 0.2ex;
    border: 0.1ex solid #BAB9B8;
    background-color: transparent;
}

QScrollBar:horizontal
{
    height: 1.5ex;
    margin: 0.3ex 1.5ex 0.3ex 1.5ex;
    border: 0.1ex transparent #2A2929;
    border-radius: 0.4ex;
    background-color: #2A2929;
}

QScrollBar::handle:horizontal
{
    background-color: #605F5F;
    min-width: 0.5ex;
    border-radius: 0.4ex;
}

QScrollBar::add-line:horizontal
{
    margin: 0ex 0.3ex 0ex 0.3ex;
    border-image: url(:themes/light/right_arrow_disabled.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    margin: 0px 0.3ex 0px 0.3ex;
    border-image: url(:themes/light/left_arrow_disabled.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
{
    border-image: url(:themes/light/right_arrow.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
{
    border-image: url(:themes/light/left_arrow.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    background-color: #2A2929;
    width: 1.5ex;
    margin: 1.5ex 0.3ex 1.5ex 0.3ex;
    border: 0.1ex transparent #2A2929;
    border-radius: 0.4ex;
}

QScrollBar::handle:vertical
{
    background-color: #605F5F;
    min-height: 0.5ex;
    border-radius: 0.4ex;
}

QScrollBar::sub-line:vertical
{
    margin: 0.3ex 0ex 0.3ex 0ex;
    border-image: url(:themes/light/up_arrow_disabled.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{
    margin: 0.3ex 0ex 0.3ex 0ex;
    border-image: url(:themes/light/down_arrow_disabled.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,
QScrollBar::sub-line:vertical:on
{

    border-image: url(:themes/light/up_arrow.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover,
QScrollBar::add-line:vertical:on
{
    border-image: url(:themes/light/down_arrow.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical
{
    background: none;
}

QTextEdit
{
    background-color: #EFF0F1;
    color: #31363B;
    border: 0.1ex solid #BAB9B8;
}

QPlainTextEdit
{
    background-color: #FCFCFC;
    color: #31363B;
    border-radius: 0.2ex;
    border: 0.1ex solid #BAB9B8;
}

QHeaderView::section
{
    background-color: #BAB9B8;
    color: #31363B;
    padding: 0.5ex;
    border: 0.1ex solid #BAB9B8;
}

QSizeGrip#size_grip
{
    border-image: url(:buttons/light/btn_resize.png);
    width: 20px;
    height: 20px;
}

QMainWindow
{
    border-style : none;
}

QMainWindow::separator
{
    background-color: #EFF0F1;
    color: white;
    padding-left: 0.4ex;
    spacing: 0.2ex;
    border: 0.1ex dashed #BAB9B8;
}

QMainWindow::separator:hover
{

    background-color: #787876;
    color: white;
    padding-left: 0.4ex;
    border: 0.1ex solid #BAB9B8;
    spacing: 0.2x;
}

QMenu::separator
{
    height: 0.1ex;
    background-color: #BAB9B8;
    color: white;
    padding-left: 0.4ex;
    margin-left: 1ex;
    margin-right: 0.5ex;
}

QFrame[frameShape="2"],  /* QFrame::Panel == 0x0003 */
QFrame[frameShape="3"],  /* QFrame::WinPanel == 0x0003 */
QFrame[frameShape="4"],  /* QFrame::HLine == 0x0004 */
QFrame[frameShape="5"],  /* QFrame::VLine == 0x0005 */
QFrame[frameShape="6"]  /* QFrame::StyledPanel == 0x0006 */
{
    border-width: 0.1ex;
    padding: 0.1ex;
    border-style: solid;
    border-color: #EFF0F1;
    background-color: #bcbfc2;
    border-radius: 0.5ex;
}


QStackedWidget
{
    border: transparent;
    border-radius: 15px;
    background : rgba(255,255,255, 120)
}

QWidget#page_1
{
    border: transparent;
    background : rgba(230,230,230,150);
}

QWidget#page_3
{
    border: transparent;
    background : rgba(230,230,230,150);
}

QWidget#page_2
{
    border: transparent;
    background : rgba(230,230,230,150);
}

QWidget#page_4
{
    border: transparent;
    background : rgba(230,230,230,150);
}

QFrame#title_bar
{
    background : rgba(230,230,230,255);
}

QFrame#settings_toolbar
{    
    background : rgba(255,255,255,220);
}

QFrame#Snake
{
    border : 2px solid black;
    background : transparent;
    background-color : transparent;
}

QFrame#Tetris
{
    border : 2px solid black;
    background : transparent;
    background-color : transparent;
}

QFrame#line_2_3
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#line_3_4
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#line_1_2
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QDialog
{
    border : 1px solid black;
}


QPushButton#btn_dialog_yes
{
    border : 1px solid black;
}

QPushButton#btn_dialog_no
{
    border : 1px solid black;
}

QPushButton#btn_dialog_kill_self
{
    border : 1px solid black;
}

QPushButton#btn_toolbar_1
{   
    background: transparent;
    border-image: url(:buttons/light/btn_toolbar_1.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_toolbar_1:hover,QPushButton#btn_toolbar_2:hover, QPushButton#btn_toolbar_3:hover,
QPushButton#btn_toolbar_4:hover
{   
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #4cbdff, stop: 0.5 #33a4e8);
    border: 0.1ex solid #3daef3;
    color: #31363B;
}

QPushButton#btn_toolbar_1:focus:pressed,QPushButton#btn_toolbar_2:focus:pressed, QPushButton#btn_toolbar_3:focus:pressed,
QPushButton#btn_toolbar_4:focus:pressed,
QPushButton#btn_toolbar_1:pressed,QPushButton#btn_toolbar_2:pressed, QPushButton#btn_toolbar_3:pressed,
QPushButton#btn_toolbar_4:pressed
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #bedfec, stop: 0.5 #b9dae7);
    color: #31363B;
}

QPushButton#btn_toolbar_1:checked,QPushButton#btn_toolbar_2:checked, QPushButton#btn_toolbar_3:checked,
QPushButton#btn_toolbar_4:checked
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #96d8ff, stop: 0.5 #73caff);
    border-color: #6A6969;
}

QPushButton#btn_toolbar_2
{   
    background: transparent;
    border-image: url(:buttons/light/btn_toolbar_2.png) 0 0 0 0 stretch stretch;
}
QPushButton#btn_toolbar_3
{   
    background: transparent;
    border-image: url(:buttons/light/btn_toolbar_3.png) 0 0 0 0 stretch stretch;
}
QPushButton#btn_toolbar_4
{   
    background: transparent;
    border-image: url(:buttons/light/btn_toolbar_4.png) 0 0 0 0 stretch stretch;
}
QPushButton#btn_settings_tetris
{   
    background: transparent;
    border-image: url(:buttons/light/btn_tetris.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_tetris:hover, QPushButton#btn_settings_snake:hover, QPushButton#btn_settings_add_bck:hover,
QPushButton#btn_settings_chg_bck:hover, QPushButton#btn_settings_open_chat:hover, QPushButton#btn_settings_chg_font:hover
{   
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #4cbdff, stop: 0.5 #33a4e8);
    border: 0.1ex solid #3daef3;
    color: #31363B;
}

QPushButton#btn_settings_tetris:focus:pressed, QPushButton#btn_settings_snake:focus:pressed, QPushButton#btn_settings_add_bck:focus:pressed,
QPushButton#btn_settings_chg_bck:focus:pressed, QPushButton#btn_settings_open_chat:focus:pressed, QPushButton#btn_settings_chg_font:focus:pressed,
QPushButton#btn_settings_tetris:pressed, QPushButton#btn_settings_snake:pressed, QPushButton#btn_settings_add_bck:pressed,
QPushButton#btn_settings_chg_bck:pressed, QPushButton#btn_settings_open_chat:pressed, QPushButton#btn_settings_chg_font:pressed
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #bedfec, stop: 0.5 #b9dae7);
    color: #31363B;
}

QPushButton:checked
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #96d8ff, stop: 0.5 #73caff);
    border-color: #6A6969;
}


QPushButton#btn_settings_snake
{   
    background: transparent;
    border-image: url(:buttons/light/btn_snake.png) 0 0 0 0 stretch stretch;
}
QPushButton#btn_settings_open_chat
{   
    background: transparent;
    border-image: url(:buttons/light/btn_settings_chat.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_toggle_win_settings, QPushButton#btn_settings_toggle_custom, QPushButton#btn_settings_toggle_games
{   
    font: bold 11pt "Segoe UI" ;
    color :  #aaaaaa;
}

QPushButton#btn_settings_toggle_win_settings:hover, QPushButton#btn_settings_toggle_win_settings:checked,
QPushButton#btn_settings_toggle_custom:hover, QPushButton#btn_settings_toggle_custom:checked,
QPushButton#btn_settings_toggle_games:hover, QPushButton#btn_settings_toggle_games:checked
{   
    font: bold 11pt "Segoe UI";
    color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #00017e, stop: 0.5 #000170);
}

QToolBar
{
    border: 0.1ex transparent #393838;
    background: 0.1ex solid #EFF0F1;
    font-weight: bold;
}

QToolBar::handle:horizontal
{
    border-image: url(:themes/light/hmovetoolbar.svg);
    width = 1.6ex;
    height = 6.4ex;
}

QToolBar::handle:vertical
{
    border-image: url(:themes/light/vmovetoolbar.svg);
    width = 5.4ex;
    height = 1ex;
}

QToolBar::separator:horizontal
{
    border-image: url(:themes/light/hsepartoolbar.svg);
    width = 0.7ex;
    height = 6.3ex;
}

QToolBar::separator:vertical
{
    border-image: url(:themes/light/vsepartoolbars.svg);
    width = 6.3ex;
    height = 0.7ex;
}

QPushButton
{
    color: #31363B;
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #EFF0F1, stop: 0.5 #eaebec);
    border-width: 0.1ex;
    border-color: #BAB9B8;
    border-style: solid;
    padding: 0.5ex;
    border-radius: 6px;
    outline: none;
}

QPushButton:disabled
{
    background-color: #e0e1e2;
    border-width: 0.1ex;
    border-color: #b4b4b4;
    border-style: solid;
    padding-top: 0.5ex;
    padding-bottom: 0.5ex;
    padding-left: 1ex;
    padding-right: 1ex;
    border-radius: 0.2ex;
    color: #b4b4b4;
}
QPushButton:focus
{
    color: black;
}
QPushButton:focus:pressed,
QPushButton:pressed
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #bedfec, stop: 0.5 #b9dae7);
    color: #31363B;
}

QPushButton:checked
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #96d8ff, stop: 0.5 #73caff);
    border-color: #6A6969;
}

QPushButton:hover
{
    
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #4cbdff, stop: 0.5 #33a4e8);
    border: 0.1ex solid #3daef3;
    color: #31363B;
}

QPushButton:focus:hover
{

    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #379eff, stop: 0.5 #277bff);    color: #31363B;
}

QPushButton#btn_toggle_toolbar
{   
    border-image: url(:buttons/light/btn_show_toolbar.png) 0 0 0 0 stretch stretch;
    background : transparent;

}

QPushButton#btn_toggle_toolbar:hover
{   
    border-image: url(:buttons/light/btn_show_toolbar_hover.png) 0 0 0 0 stretch stretch;
    background : transparent;
}

QPushButton#btn_toggle_toolbar:checked
{   
    border-image: url(:buttons/light/btn_hide_toolbar.png) 0 0 0 0 stretch stretch;
    background : transparent;
}

QPushButton#btn_settings_chg_bck
{   
    background : transparent;
    border-image: url(:buttons/light/btn_settings_change_bckg.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_add_bck
{   
    background : transparent;
    border-image: url(:buttons/light/btn_settings_add_bckg.png) 0 0 0 0 stretch stretch;

}
QPushButton#btn_settings_chg_font
{   
    background : transparent;
    border-image: url(:buttons/light/btn_settings_change_font.png) 0 0 0 0 stretch stretch;
}

QComboBox:hover,
QAbstractSpinBox:hover,
QLineEdit:hover,
QTextEdit:hover,
QPlainTextEdit:hover,
QAbstractView:hover,
QTreeView:hover
{
    border: 0.1ex solid #33A4DF;
    color: #31363B;
}

QComboBox:hover:pressed,
QPushButton:hover:pressed,
QAbstractSpinBox:hover:pressed,
QLineEdit:hover:pressed,
QTextEdit:hover:pressed,
QPlainTextEdit:hover:pressed,
QAbstractView:hover:pressed,
QTreeView:hover:pressed
{
    background-color: #EFF0F1;
}

QComboBox
{
    selection-background-color: #33A4DF;
    border-style: solid;
    border: 0.1ex solid #BAB9B8;
    border-radius: 0.2ex;
    padding: 0.5ex;
    min-width: 7.5ex;
}

QComboBox:on
{
    padding-top: 0.3ex;
    padding-left: 0.4ex;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView
{
    background-color: #FCFCFC;
    border-radius: 0.2ex;
    border: 0.1ex solid #BAB9B8;
    selection-background-color: #33A4DF;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 1.5ex;

    border-left-width: 0ex;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 0.3ex;
    border-bottom-right-radius: 0.3ex;
}

QComboBox::down-arrow
{
    border-image: url(:themes/light/down_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QComboBox::down-arrow:on,
QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    border-image: url(:themes/light/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox
{
    padding: 0.5ex;
    border: 0.1ex solid #BAB9B8;
    background-color: #D9D8D7;
    color: #31363B;
    border-radius: 0.2ex;
    min-width: 7.5ex;
}

QAbstractSpinBox:up-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center right;
}

QAbstractSpinBox:down-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center left;
}

QAbstractSpinBox::up-arrow,
QAbstractSpinBox::up-arrow:disabled,
QAbstractSpinBox::up-arrow:off
{
    border-image: url(:themes/light/up_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::up-arrow:hover
{
    border-image: url(:themes/light/up_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::down-arrow,
QAbstractSpinBox::down-arrow:disabled,
QAbstractSpinBox::down-arrow:off
{
    border-image: url(:themes/light/down_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::down-arrow:hover
{
    border-image: url(:themes/light/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QLabel
{
    border: 0ex solid black;
}


QTabWidget{
    border: 0.1ex solid #BAB9B8;
}

/* BORDERS */
QTabWidget::pane
{
    padding: 0.5ex;
    margin: 0.1ex;
}

QTabWidget::pane:top
{
    border: 0.1ex solid #BAB9B8;
    top: -0.1ex;
}

QTabWidget::pane:bottom
{
    border: 0.1ex solid #BAB9B8;
    bottom: -0.1ex;
}

QTabWidget::pane:left
{
    border: 0.1ex solid #BAB9B8;
    right: -0.1ex;
}

QTabWidget::pane:right
{
    border: 0.1ex solid #BAB9B8;
    left: -0.1ex;
}

QTabBar
{
    qproperty-drawBase: 0;
    left: 0.5ex; /* move to the right by 0.5ex */
    border-radius: 0.3ex;
}

QTabBar:focus
{
    border: 0ex transparent black;
}

QTabBar::close-button
{
    border-image: url(:themes/light/close.svg);
    width: 1.2ex;
    height: 1.2ex;
    background: transparent;
}

QTabBar::close-button:hover
{
    border-image: url(:themes/light/close-hover.svg);
    width: 1.2ex;
    height: 1.2ex;
    background: transparent;
}

QTabBar::close-button:pressed
{
    border-image: url(:themes/light/close-pressed.svg);
    width: 1.2ex;
    height: 1.2ex;
    background: transparent;
}

/* TOP TABS */
QTabBar::tab:top
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #BAB9B8;
    border-top: 0.1ex solid #BAB9B8;
    background-color: #EFF0F1;
    padding: 0.5ex;
    min-width: 5ex;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:last,
QTabBar::tab:top:only-one
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #BAB9B8;
    border-right: 0.1ex solid #BAB9B8;
    border-top: 0.1ex solid #BAB9B8;
    background-color: #EFF0F1;
    padding: 0.5ex;
    min-width: 5ex;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:!selected
{
    color: #31363B;
    background-color: #D9D8D7;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #BAB9B8;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:first:!selected
{
    color: #31363B;
    background-color: #D9D8D7;
    border: 0.1ex transparent black;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
    border-left: 0.1ex solid #BAB9B8;
}

QTabBar::tab:top:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
}

/* BOTTOM TABS */
QTabBar::tab:bottom
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #BAB9B8;
    border-bottom: 0.1ex solid #BAB9B8;
    background-color: #EFF0F1;
    padding: 0.5ex;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-width: 5ex;
}

QTabBar::tab:bottom:last,
QTabBar::tab:bottom:only-one
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #BAB9B8;
    border-right: 0.1ex solid #BAB9B8;
    border-bottom: 0.1ex solid #BAB9B8;
    background-color: #EFF0F1;
    padding: 0.5ex;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-width: 5ex;
}

QTabBar::tab:bottom:!selected
{
    color: #31363B;
    background-color: #D9D8D7;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #BAB9B8;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
}

QTabBar::tab:bottom:first:!selected
{
    color: #31363B;
    background-color: #D9D8D7;
    border: 0.1ex transparent black;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
}

QTabBar::tab:bottom:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
    border-left: 0.1ex solid #BAB9B8;
}

QTabBar::tab:bottom:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
}

/* LEFT TABS */
QTabBar::tab:left
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #BAB9B8;
    border-right: 0.1ex solid #BAB9B8;
    background-color: #EFF0F1;
    padding: 0.5ex;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-height: 5ex;
}

QTabBar::tab:left:last,
QTabBar::tab:left:only-one
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #BAB9B8;
    border-bottom: 0.1ex solid #BAB9B8;
    border-right: 0.1ex solid #BAB9B8;
    background-color: #EFF0F1;
    padding: 0.5ex;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-height: 5ex;
}

QTabBar::tab:left:!selected
{
    color: #31363B;
    background-color: #D9D8D7;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #BAB9B8;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
}

QTabBar::tab:left:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
    border-top: 0.1ex solid #BAB9B8;
}

QTabBar::tab:left:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
}

/* RIGHT TABS */
QTabBar::tab:right
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #BAB9B8;
    border-left: 0.1ex solid #BAB9B8;
    background-color: #D9D8D7;
    padding: 0.5ex;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
    min-height: 5ex;
}

QTabBar::tab:right:last,
QTabBar::tab:right:only-one
{
    color: #31363B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #BAB9B8;
    border-bottom: 0.1ex solid #BAB9B8;
    border-left: 0.1ex solid #BAB9B8;
    background-color: #D9D8D7;
    padding: 0.5ex;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
    min-height: 5ex;
}

QTabBar::tab:right:!selected
{
    color: #31363B;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #BAB9B8;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
}

QTabBar::tab:right:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
    border-top: 0.1ex solid #BAB9B8;
}

QTabBar::tab:right:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    border: 0.1ex rgba(61, 173, 232, 0.1);
}

QTabBar QToolButton::right-arrow:enabled
{
    border-image: url(:themes/light/right_arrow.svg);
}

QTabBar QToolButton::left-arrow:enabled
{
    border-image: url(:themes/light/left_arrow.svg);
}

QTabBar QToolButton::right-arrow:disabled
{
    border-image: url(:themes/light/right_arrow_disabled.svg);
}

QTabBar QToolButton::left-arrow:disabled
{
    border-image: url(:themes/light/left_arrow_disabled.svg);
}

QDockWidget
{
    background: #EFF0F1;
    border: 0.1ex solid #403F3F;
    titlebar-close-icon: url(:themes/light/transparent.svg);
    titlebar-normal-icon: url(:themes/light/transparent.svg);
}

QDockWidget::close-button,
QDockWidget::float-button
{
    border: 0.1ex solid transparent;
    border-radius: 0.2ex;
    background: transparent;
}


QDockWidget::float-button
{
    border-image: url(:themes/dark/undock.svg);
}

QDockWidget::float-button:hover
{
    border-image: url(:themes/dark/undock-hover.svg) ;
}

QDockWidget::close-button
{
    border-image: url(:themes/dark/close.svg) ;
}

QDockWidget::close-button:hover
{
    border-image: url(:themes/dark/close-hover.svg) ;
}

QDockWidget::close-button:pressed
{
    border-image: url(:themes/dark/close-pressed.svg) ;
}

QTreeView,
QListView
{
    border: 0.1ex solid #BAB9B8;
    background-color: #FCFCFC;
}


QTreeView::branch:has-siblings:!adjoins-item
{
    border-image: url(:themes/light/stylesheet-vline.svg) 0;
}

QTreeView::branch:has-siblings:adjoins-item
{
    border-image: url(:themes/light/stylesheet-branch-more.svg) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item
{
    border-image: url(:themes/light/stylesheet-branch-end.svg) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings
{
    border-image: url(:themes/light/stylesheet-branch-end-closed.svg) 0;
    image: url(:themes/light/branch_closed.svg);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings
{
    border-image: url(:themes/light/stylesheet-branch-end-open.svg) 0;
    image: url(:themes/light/branch_open.svg);
}

QTableView::item,
QListView::item,
QTreeView::item
{
    padding: 0.3ex;
}

QTableView::item:!selected:hover,
QListView::item:!selected:hover,
QTreeView::item:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.1);
    outline: 0;
    color: #31363B;
    padding: 0.3ex;
}

QSlider::groove:horizontal
{
    border: 0.1ex solid #EFF0F1;
    height: 0.4ex;
    background: #9CA0A4;
    margin: 0px;
    border-radius: 0.2ex;
}

QSlider::handle:horizontal
{
    background: #D9D8D7;
    border: 0.1ex solid #BABEC2;
    width: 1.6ex;
    height: 1.6ex;
    margin: -0.8ex 0;
    border-radius: 0.9ex;
}

QSlider::groove:vertical
{
    border: 0.1ex solid #EFF0F1;
    width: 0.4ex;
    background: #9CA0A4;
    margin: 0ex;
    border-radius: 0.3ex;
}

QSlider::handle:vertical
{
    background: #D9D8D7;
    border: 0.1ex solid #BABEC2;
    width: 1.6ex;
    height: 1.6ex;
    margin: 0 -0.8ex;
    border-radius: 0.9ex;
}

QSlider::handle:horizontal:focus,
QSlider::handle:vertical:focus
{
    border: 0.1ex solid #33A4DF;
}

QSlider::handle:horizontal:hover,
QSlider::handle:vertical:hover
{
    border: 0.1ex solid #51c2fc;
}

QSlider::sub-page:horizontal,
QSlider::add-page:vertical
{
    background: #33A4DF;
    border-radius: 0.3ex;
}

QSlider::add-page:horizontal,
QSlider::sub-page:vertical
{
    background: #BABEC2;
    border-radius: 0.3ex;
}

QToolButton
{
    background-color: transparent;
    border: 0.1ex solid #BAB9B8;
    border-radius: 0.2ex;
    margin: 0.3ex;
    padding: 0.5ex;
}

QToolButton[popupMode="1"] /* only for MenuButtonPopup */
{
    padding-right: 2ex; /* make way for the popup button */
}

QToolButton[popupMode="2"] /* only for InstantPopup */
{
    padding-right: 1ex; /* make way for the popup button */
}

QToolButton::menu-indicator
{
    border-image: url(:themes/light/down_arrow.svg);
    top: -0.7ex; left: -0.2ex; /* shift it a bit */
    width = 0.9ex;
    height = 0.6ex;
}

QToolButton::menu-arrow
{
    border-image: url(:themes/light/down_arrow.svg);
    width = 0.9ex;
    height = 0.6ex;
}

QToolButton:hover,
QToolButton::menu-button:hover
{
    background-color: transparent;
    border: 0.1ex solid #33A4DF;
}

QToolButton:checked,
QToolButton:pressed,
QToolButton::menu-button:pressed
{
    background-color: #47b8fc;
    border: 0.1ex solid #47b8fc;
    padding: 0.5ex;
}

QToolButton::menu-button
{
    border: 0.1ex solid #BAB9B8;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* 1ex width + 0.4ex for border + no text = 2ex allocated above */
    width: 1ex;
    padding: 0.5ex;
    outline: none;
}

QToolButton::menu-arrow:open
{
    border: 0.1ex solid #BAB9B8;
}

QPushButton::menu-indicator
{
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    left: 0.8ex;
}

QTableView
{
    border: 0.1ex solid #BAB9B8;
    gridline-color: #BAB9B8;
    background-color: #FCFCFC;
}


QTableView,
QHeaderView
{
    border-radius: 0px;
}

QTableView::item:pressed
{
    background: #33A4DF;
    color: #31363B;
}

QTableView::item:selected:active
{
    background: #33A4DF;
    color: #31363B;
}

QTableView::item:selected:hover
{
    background-color: #47b8f3;
    color: #31363B;
}

QListView::item:pressed,
QTreeView::item:pressed
{
    background: #3daee9;
    color: #31363B;
}

QTreeView::item:selected:active,
QListView::item:selected:active
{
    background: #3daee9;
    color: #31363B;
}

QListView::item:selected:hover,
QTreeView::item:selected:hover
{
    background-color: #51c2fc;
    color: #31363B;
}


QHeaderView
{
    background-color: #EFF0F1;
    border: 0.1ex transparent;
    border-radius: 0px;
    margin: 0px;
    padding: 0px;

}

QHeaderView::section
{
    background-color: #EFF0F1;
    color: #31363B;
    padding: 0.5ex;
    border: 0.1ex solid #BAB9B8;
    border-radius: 0px;
    text-align: center;
}

QHeaderView::section::vertical::first,
QHeaderView::section::vertical::only-one
{
    border-top: 0.1ex solid #BAB9B8;
}

QHeaderView::section::vertical
{
    border-top: transparent;
}

QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one
{
    border-left: 0.1ex solid #BAB9B8;
}

QHeaderView::section::horizontal
{
    border-left: transparent;
}


QHeaderView::section:checked

{
    color: black;
    background-color: #b9dae7;
}

/* style the sort indicator */
QHeaderView::down-arrow
{
    image: url(:themes/light/down_arrow.svg);
}

QHeaderView::up-arrow
{
    image: url(:themes/light/up_arrow.svg);
}

QTableCornerButton::section
{
    background-color: #EFF0F1;
    border: 0.1ex transparent #BAB9B8;
    border-radius: 0px;
}

QToolBox
{
    padding: 0.5ex;
    border: 0.1ex transparent black;
}

QToolBox:selected
{
    background-color: #EFF0F1;
    border-color: #33A4DF;
}

QToolBox:hover
{
    border-color: #33A4DF;
}

QToolBox::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border-radius: 7px;
    color: darkgrey;
}

QToolBox::tab:selected { /* italicize selected tabs */
    font: bold italic;
    color: black;
}
QStatusBar
{
    background-color : transparent;
}

QStatusBar::item
{
    border: 0px transparent dark;
}


QFrame#drop_shadow_frame
{
    border-radius: 10px;
    background-color: transparent;
}

QFrame#content_bar
{
    background-color: transparent;
}

QFrame#toolbar
{
    background : rgba(255,255,255,200);
}

QFrame#vertical_line_page_1
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#vertical_line_page_1_2
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#line_win_set_top
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#line_games_bot
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#line_label_customize
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#line_label_games
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
}

QFrame#line_label_window_settings
{
    border : 1px solid #aaaaaa;
    background : #aaaaaa;
} 

QFrame#frame_customize, QFrame#frame_games, QFrame#mini_frame_window
{
    background : qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.539773, stop:0 rgba(112, 204, 255, 168), stop:1 rgba(153, 223, 255, 162));
    border : 1px solid #2a2aff;
}

QSplitter::handle
{
    border: 0.1ex dashed #BAB9B8;
}

QSplitter::handle:hover
{
    background-color: #787876;
    border: 0.1ex solid #BAB9B8;
}

QSplitter::handle:horizontal
{
    width: 0.1ex;
}

QSplitter::handle:vertical
{
    height: 0.1ex;
}

QProgressBar:horizontal
{
    background-color: #BABEC2;
    border: 0.1ex solid #EFF0F1;
    border-radius: 0.3ex;
    height: 0.5ex;
    text-align: right;
    margin-top: 0.5ex;
    margin-bottom: 0.5ex;
    margin-right: 5ex;
    padding: 0px;
}

QProgressBar::chunk:horizontal
{
    background-color: #33A4DF;
    border: 0.1ex transparent;
    border-radius: 0.3ex;
}

QProgressBar#progressBar {	
	background-color: rgb(98, 114, 164);
	color: rgb(0,255,255);
	border-style: none;
	border-radius: 10px;
	text-align: center;
}
QProgressBar#progressBar::chunk{
	border-radius: 10px;
	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(0, 230, 255, 255), stop:1 rgba(170, 85, 255, 255));}

QProgressBar#main_window_progress {
	
	background-color: rgb(188, 188, 188);
	color: black;
	border: 1px solid grey;
	border-radius: 5px;
	text-align: center;
	font: bold 11pt "Segoe UI";
}
QProgressBar#main_window_progress::chunk{
	border-radius: 10px;
	background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.539773, stop:0 rgba(0, 163, 255, 255), stop:1 rgba(64, 195, 255, 255)) ;
}

QAbstractSpinBox
{
    background-color: #EFF0F1;
}

QSpinBox,
QDoubleSpinBox
{
    padding-right: 1.5ex;
}

QSpinBox::up-button,
QDoubleSpinBox::up-button
{
    subcontrol-origin: content;
    subcontrol-position: right top;

    width: 1.6ex;
    border-width: 0.1ex;
}

QSpinBox::up-arrow,
QDoubleSpinBox::up-arrow
{
    border-image: url(:themes/light/up_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::up-arrow:hover,
QSpinBox::up-arrow:pressed,
QDoubleSpinBox::up-arrow:hover,
QDoubleSpinBox::up-arrow:pressed
{
    border-image: url(:themes/light/up_arrow-hover.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::up-arrow:disabled,
QSpinBox::up-arrow:off,
QDoubleSpinBox::up-arrow:disabled,
QDoubleSpinBox::up-arrow:off
{
border-image: url(:themes/light/up_arrow_disabled.svg);
}

QSpinBox::down-button,
QDoubleSpinBox::down-button
{
    subcontrol-origin: content;
    subcontrol-position: right bottom;

    width: 1.6ex;
    border-width: 0.1ex;
}

QSpinBox::down-arrow,
QDoubleSpinBox::down-arrow
{
    border-image: url(:themes/light/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::down-arrow:hover,
QSpinBox::down-arrow:pressed,
QDoubleSpinBox::down-arrow:hover,
QDoubleSpinBox::down-arrow:pressed
{
    border-image: url(:themes/light/down_arrow-hover.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::down-arrow:disabled,
QSpinBox::down-arrow:off,
QDoubleSpinBox::down-arrow:disabled,
QDoubleSpinBox::down-arrow:off
{
border-image: url(:themes/light/down_arrow_disabled.svg);
}

"""
light_bg_pics_cycle = cycle(light_bg_pics)

def dynamic_main_bg_stylesheet(i_default_stylesheet=stylesheet, i_bg_list=light_bg_pics, i_placeholder="bg_pic.format"):

    # if list isn't empty, process to return style with replaced string
    if i_bg_list:
        return i_default_stylesheet.replace(i_placeholder, i_bg_list[-1])

def change_background(i_default_stylesheet=stylesheet, i_placeholder="bg_pic.format"):
    next_bg = next(light_bg_pics_cycle)
    return i_default_stylesheet.replace(i_placeholder, next_bg)

def set_custom_back(custom_bg, i_default_stylesheet=stylesheet, i_placeholder=":themes/backgrounds/light_bg/bg_pic.format"):
    return i_default_stylesheet.replace(i_placeholder, custom_bg)
"""
def change_global_font_via_qss (new_font, stylesheet=stylesheet, placeholder=["pointSize", "yourFont"]):
    return stylesheet.replace(placeholder[0], f'{new_font.pointSize()}').replace(placeholder[1], f'{new_font.family()}')
"""