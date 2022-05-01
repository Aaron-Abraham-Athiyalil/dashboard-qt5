from itertools import cycle

dark_bg_pics = ["dark_bg_pic_01.png","dark_bg_pic_02.png","dark_bg_pic_03.png"]

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
    border: 0.1ex solid #eff0f1;
    background-color: #111111;
    alternate-background-color: #141414;
    color: #eff0f1;
    padding: 0.5ex;
    opacity: 200;
}

QWidget
{
    color: #eff0f1;
    background-color: #111111;
    selection-background-color:#3daee9;
    selection-color: #eff0f1;
    background-clip: border;
    border-image: none;
    border: 0px transparent black;
    outline: 0;
}

QWidget#centralwidget
{
    border-image: url(":themes/backgrounds/dark_bg/bg_pic.format") 0 0 0 0 stretch stretch; 
    border-radius: 15px;
}

QWidget:item:hover
{
    background-color: #3daee9;
    color: #eff0f1;
}

QWidget:item:selected
{
    background-color: #3daee9;
}

QCheckBox
{
    spacing: 0.5ex;
    outline: none;
    color: #eff0f1;
    margin-bottom: 0.2ex;
    opacity: 200;
}

QCheckBox:disabled
{
    color: #76797c;
}

QGroupBox::indicator
{
    margin-left: 0.2ex;
}

QCheckBox::indicator:unchecked,
QCheckBox::indicator:unchecked:focus
{
    border-image: url(:themes/dark/checkbox_unchecked_disabled.svg);
}

QCheckBox::indicator:unchecked:hover,
QCheckBox::indicator:unchecked:pressed,
QGroupBox::indicator:unchecked:hover,
QGroupBox::indicator:unchecked:focus,
QGroupBox::indicator:unchecked:pressed
{
    border: none;
    border-image: url(:themes/dark/checkbox_unchecked.svg);
}

QCheckBox::indicator:checked
{
    border-image: url(:themes/dark/checkbox_checked.svg);
}

QCheckBox::indicator:checked:hover,
QCheckBox::indicator:checked:focus,
QCheckBox::indicator:checked:pressed,
QGroupBox::indicator:checked:hover,
QGroupBox::indicator:checked:focus,
QGroupBox::indicator:checked:pressed
{
    border: none;
    border-image: url(:themes/dark/checkbox_checked.svg);
}

QCheckBox::indicator:indeterminate
{
    border-image: url(:themes/dark/checkbox_indeterminate.svg);
}

QCheckBox::indicator:indeterminate:focus,
QCheckBox::indicator:indeterminate:hover,
QCheckBox::indicator:indeterminate:pressed
{
    border-image: url(:themes/dark/checkbox_indeterminate.svg);
}

QCheckBox::indicator:indeterminate:disabled
{
    border-image: url(:themes/dark/checkbox_indeterminate_disabled.svg);
}

QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled
{
    border-image: url(:themes/dark/checkbox_checked_disabled.svg);
}

QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled
{
    border-image: url(:themes/dark/checkbox_unchecked_disabled.svg);
}

QRadioButton
{
    spacing: 0.5ex;
    outline: none;
    color: #eff0f1;
    margin-bottom: 0.2ex;
}

QRadioButton:disabled
{
    color: #76797c;
}

QRadioButton::indicator:unchecked,
QRadioButton::indicator:unchecked:focus
{
    border-image: url(:themes/dark/radio_unchecked_disabled.svg);
}


QRadioButton::indicator:unchecked:hover,
QRadioButton::indicator:unchecked:pressed
{
    border: none;
    outline: none;
    border-image: url(:themes/dark/radio_unchecked.svg);
}


QRadioButton::indicator:checked
{
    border: none;
    outline: none;
    border-image: url(:themes/dark/radio_checked.svg);
}

QRadioButton::indicator:checked:hover,
QRadioButton::indicator:checked:focus,
QRadioButton::indicator:checked:pressed
{
    border: none;
    outline: none;
    border-image: url(:themes/dark/radio_checked.svg);
}

QRadioButton::indicator:checked:disabled
{
    outline: none;
    border-image: url(:themes/dark/radio_checked_disabled.svg);
}

QRadioButton::indicator:unchecked:disabled
{
    border-image: url(:themes/dark/radio_unchecked_disabled.svg);
}

QMenuBar
{
    background-color: #111111;
    color: #eff0f1;
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 0.1ex solid #76797c;
}

QMenuBar::item:pressed
{
    border: 0.1ex solid #76797c;
    background-color: #3daee9;
    color: #eff0f1;
    margin-bottom: -0.1ex;
    padding-bottom: 0.1ex;
}

QMenu
{
    border: 0.1ex solid #76797c;
    color: #eff0f1;
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
    color: #eff0f1;
}

QMenu::separator
{
    height: 2px;
    width : 2px;
    background: cyan;
    margin-left: 1ex;
    margin-right: 0.5ex;
}

/* non-exclusive indicator = check box style indicator
(see QActionGroup::setExclusive) */
QMenu::indicator:non-exclusive:unchecked
{
    border-image: url(:themes/dark/checkbox_unchecked_disabled.svg);
}

QMenu::indicator:non-exclusive:unchecked:selected
{
    border-image: url(:themes/dark/checkbox_unchecked_disabled.svg);
}

QMenu::indicator:non-exclusive:checked
{
    border-image: url(:themes/dark/checkbox_checked.svg);
}

QMenu::indicator:non-exclusive:checked:selected
{
    border-image: url(:themes/dark/checkbox_checked.svg);
}

/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
QMenu::indicator:exclusive:unchecked
{
    border-image: url(:themes/dark/radio_unchecked_disabled.svg);
}

QMenu::indicator:exclusive:unchecked:selected
{
    border-image: url(:themes/dark/radio_unchecked_disabled.svg);
}

QMenu::indicator:exclusive:checked
{
    border-image: url(:themes/dark/radio_checked.svg);
}

QMenu::indicator:exclusive:checked:selected
{
    border-image: url(:themes/dark/radio_checked.svg);
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
    background-color: #111111;
}

QAbstractItemView
{
    alternate-background-color: #111111;
    color: #eff0f1;
    border: 0.1ex solid 3A3939;
    border-radius: 0.2ex;
}

QWidget:focus,
QMenuBar:focus
{
    border: 0.1ex solid #3daee9;
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
    background-color: #232629;
    padding: 0.5ex;
    border-style: solid;
    border: 0.1ex solid #76797c;
    border-radius: 0.2ex;
    color: #eff0f1;
}

QGroupBox
{
    border: 0.1ex solid #76797c;
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
    border: 0.1ex solid #76797c;
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
    background-color: #3daee9;
    min-width: 0.5ex;
    border-radius: 0.4ex;
}

QScrollBar::add-line:horizontal
{
    margin: 0px 0.3ex 0px 0.3ex;
    border-image: url(:themes/dark/right_arrow_disabled.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    margin: 0ex 0.3ex 0ex 0.3ex;
    border-image: url(:themes/dark/left_arrow_disabled.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,
QScrollBar::add-line:horizontal:on
{
    border-image: url(:themes/dark/right_arrow.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:horizontal:hover,
QScrollBar::sub-line:horizontal:on
{
    border-image: url(:themes/dark/left_arrow.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal,
QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal
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
    background-color: #3daee9;
    min-height: 0.5ex;
    border-radius: 0.4ex;
}

QScrollBar::sub-line:vertical
{
    margin: 0.3ex 0ex 0.3ex 0ex;
    border-image: url(:themes/dark/up_arrow_disabled.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{
    margin: 0.3ex 0ex 0.3ex 0ex;
    border-image: url(:themes/dark/down_arrow_disabled.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,
QScrollBar::sub-line:vertical:on
{

    border-image: url(:themes/dark/up_arrow.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover,
QScrollBar::add-line:vertical:on
{
    border-image: url(:themes/dark/down_arrow.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}

QTextEdit
{
    background-color: #232629;
    color: #eff0f1;
    border: 0.1ex solid #76797c;
}

QPlainTextEdit
{
    background-color: #232629;
    color: #eff0f1;
    border-radius: 0.2ex;
    border: 0.1ex solid #76797c;
}

QHeaderView::section
{
    background-color: #76797c;
    color: #eff0f1;
    padding: 0.5ex;
    border: 0.1ex solid #76797c;
}

QSizeGrip#size_grip
{
    border-image: url(:buttons/dark/btn_resize.png);
    width: 20px;
    height: 20px;
    
}

QMainWindow
{
    border: none;
}


QMainWindow::separator
{
    background-color: #111111;
    color: white;
    padding-left: 0.4ex;
    spacing: 0.2ex;
    border: 0.1ex dashed #76797c;
}

QMainWindow::separator:hover
{

    background-color: #787876;
    color: white;
    padding-left: 0.4ex;
    border: 0.1ex solid #76797c;
    spacing: 0.2ex;
}

QMenu::separator
{
    height: 0.1ex;
    background-color: #76797c;
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
    border-color: #111111;
    background-color: #76797c;
    border-radius: 0.5ex;
}

QStackedWidget
{
    border: transparent;
    border-radius: 15px;
    background : rgba(0,0,0, 120)
}

QWidget#page_1
{
    border: transparent;
    background : rgba(0,0,0,150);
}

QWidget#page_2
{
    border: transparent;
    background : rgba(0,0,0,150);
}

QWidget#page_3
{
    border: transparent;
    background : rgba(0,0,0,150);
}

QWidget#page_4
{
    border: transparent;
    background : rgba(0,0,0,150);
}

QToolBar
{
    border: 0.1ex transparent #393838;
    background: 0.1ex solid #111111;
    font-weight: bold;
}

QToolBar::handle:horizontal
{
    border-image: url(:themes/dark/hmovetoolbar.svg);
    width = 1.6ex;
    height = 6.4ex;
}

QToolBar::handle:vertical
{
    border-image: url(:themes/dark/vmovetoolbar.svg);
    width = 5.4ex;
    height = 1ex;
}

QToolBar::separator:horizontal
{
    border-image: url(:themes/dark/hsepartoolbar.svg);
    width = 0.7ex;
    height = 6.3ex;
}

QToolBar::separator:vertical
{
    border-image: url(:themes/dark/vsepartoolbars.svg);
    width = 6.3ex;
    height = 0.7ex;
}

QPushButton#btn_toggle_toolbar
{   
    border-image: url(:buttons/dark/btn_show_toolbar.png) 0 0 0 0 stretch stretch;
    background : transparent;
}

QPushButton#btn_toggle_toolbar:hover
{   
    border-image: url(:buttons/dark/btn_show_toolbar_hover.png) 0 0 0 0 stretch stretch;
    background : transparent;
}

QPushButton#btn_toggle_toolbar:checked
{   
    border-image: url(:buttons/dark/btn_hide_toolbar.png) 0 0 0 0 stretch stretch;
    background : transparent;
}

QPushButton#btn_settings_chg_bck
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_settings_change_bckg.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_add_bck
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_settings_add_bckg.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_chg_font
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_settings_change_font.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_toggle_win_settings, QPushButton#btn_settings_toggle_custom, QPushButton#btn_settings_toggle_games
{   
    font: bold 11pt "Segoe UI" ;
    color :  #4b4b4b;
}

QPushButton#btn_settings_toggle_win_settings:hover, QPushButton#btn_settings_toggle_win_settings:checked,
QPushButton#btn_settings_toggle_custom:hover, QPushButton#btn_settings_toggle_custom:checked,
QPushButton#btn_settings_toggle_games:hover, QPushButton#btn_settings_toggle_games:checked 
{   
    font: bold 11pt "Segoe UI";
    color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #4cbdff, stop: 0.5 #33a4e8);
}

QPushButton
{
    color: #eff0f1;
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #141414, stop: 0.5 #111111);
    border-width: 0.1ex;
    border-color: #76797c;
    border-style: solid;
    padding: 0.5ex;
    border-radius: 6px;
    outline: none;
    
}

QPushButton:disabled
{
    background-color: #111111;
    border-width: 0.1ex;
    border-color: #454545;
    border-style: solid;
    padding-top: 0.5ex;
    padding-bottom: 0.5ex;
    padding-left: 1ex;
    padding-right: 1ex;
    border-radius: 0.2ex;
    color: #454545;
}

QPushButton:focus
{
    color: white;
}

QPushButton:focus:pressed,
QPushButton:pressed
{
    background-color: #111111;
    padding-top: -1.5ex;
    padding-bottom: -1.7ex;
}

QPushButton:checked
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #00017e, stop: 0.5 #000170);   border: 0.1ex solid #3daee9;
    border-color: #6A6969;
}

QPushButton:hover
{

    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #00017e, stop: 0.5 #000170);   border: 0.1ex solid #3daee9;
    color: #eff0f1;
}

QPushButton:checked:hover
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #00017a, stop: 0.5 #000190);   border: 0.1ex solid #3daee9;
    border: 0.1ex solid #3daee9;
    color: #eff0f1;
}

QPushButton::menu-indicator
{
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    left: 0.8ex;
}

QComboBox:hover,
QAbstractSpinBox:hover,
QLineEdit:hover,
QTextEdit:hover,
QPlainTextEdit:hover,
QAbstractView:hover,
QTreeView:hover
{
    border: 0.1ex solid #3daee9;
    color: #eff0f1;
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
    background-color: #111111;
}

QComboBox
{
    selection-background-color: #3daee9;
    border-style: solid;
    border: 0.1ex solid #76797c;
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
    background-color: #232629;
    border-radius: 0.2ex;
    border: 0.1ex solid #76797c;
    selection-background-color: #3daee9;
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
    border-image: url(:themes/dark/down_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QComboBox::down-arrow:on,
QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    border-image: url(:themes/dark/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox
{
    padding: 0.5ex;
    border: 0.1ex solid #76797c;
    background-color: #232629;
    color: #eff0f1;
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
    border-image: url(:themes/dark/up_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::up-arrow:hover
{
    border-image: url(:themes/dark/up_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::down-arrow,
QAbstractSpinBox::down-arrow:disabled,
QAbstractSpinBox::down-arrow:off
{
    border-image: url(:themes/dark/down_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::down-arrow:hover
{
    border-image: url(:themes/dark/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QLabel
{
    border: 0ex solid black;
}

/* BORDERS */
QTabWidget::pane
{
    padding: 0.5ex;
    margin: 0.1ex;
}

QTabWidget::pane:top
{
    border: 0.1ex solid #76797c;
    top: -0.1ex;
}

QTabWidget::pane:bottom
{
    border: 0.1ex solid #76797c;
    bottom: -0.1ex;
}

QTabWidget::pane:left
{
    border: 0.1ex solid #76797c;
    right: -0.1ex;
}

QTabWidget::pane:right
{
    border: 0.1ex solid #76797c;
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
    border-image: url(:themes/dark/close.svg);
    background: transparent;
}

QTabBar::close-button:hover
{
    border-image: url(:themes/dark/close-hover.svg);
    width: 1.2ex;
    height: 1.2ex;
    background: transparent;
}

QTabBar::close-button:pressed
{
    border-image: url(:themes/dark/close-pressed.svg);
    width: 1.2ex;
    height: 1.2ex;
    background: transparent;
}

/* TOP TABS */
QTabBar::tab:top
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-top: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    min-width: 50px;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:last,
QTabBar::tab:top:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    border-top: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    min-width: 50px;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:first:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-left: 0.1ex solid #76797c;
}

QTabBar::tab:top:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

/* BOTTOM TABS */

QTabBar::tab:bottom
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-width: 50px;
}

QTabBar::tab:bottom:last,
QTabBar::tab:bottom:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-width: 50px;
}

QTabBar::tab:bottom:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
}

QTabBar::tab:bottom:first:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:bottom:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-left: 0.1ex solid #76797c;
}

QTabBar::tab:bottom:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

/* LEFT TABS */
QTabBar::tab:left
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:left:last,
QTabBar::tab:left:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:left:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
}

QTabBar::tab:left:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-top: 0.1ex solid #76797c;
}

QTabBar::tab:left:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

/* RIGHT TABS */
QTabBar::tab:right
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-left: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:right:last,
QTabBar::tab:right:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    border-left: 0.1ex solid #76797c;
    background-color: #111111;
    padding: 0.5ex;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:right:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
}

QTabBar::tab:right:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-top: 0.1ex solid #76797c;
}

QTabBar::tab:right:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

QTabBar QToolButton::right-arrow:enabled
{
    border-image: url(:themes/dark/right_arrow.svg);
}

QTabBar QToolButton::left-arrow:enabled
{
    border-image: url(:themes/dark/left_arrow.svg);
}

QTabBar QToolButton::right-arrow:disabled
{
    border-image: url(:themes/dark/right_arrow_disabled.svg);
}

QTabBar QToolButton::left-arrow:disabled
{
    border-image: url(:themes/dark/left_arrow_disabled.svg);
}

QDockWidget
{
    background: #111111;
    border: 0.1ex solid #403F3F;
    titlebar-close-icon: url(:themes/dark/transparent.svg);
    titlebar-normal-icon: url(:themes/dark/transparent.svg);
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
    border: 0.1ex solid #76797c;
    background-color: #232629;
}

QTreeView::branch:has-siblings:!adjoins-item
{
    border-image: url(:themes/dark/stylesheet-vline.svg) 0;
}

QTreeView::branch:has-siblings:adjoins-item
{
    border-image: url(:themes/dark/stylesheet-branch-more.svg) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item
{
    border-image: url(:themes/dark/stylesheet-branch-end.svg) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings
{
    border-image: url(:themes/dark/stylesheet-branch-end-closed.svg) 0;
    image: url(:themes/dark/branch_closed.svg);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings
{
    border-image: url(:themes/dark/stylesheet-branch-end-open.svg) 0;
    image: url(:themes/dark/branch_open.svg);
}

/*
QTreeView::branch:has-siblings:!adjoins-item {
        background: cyan;
}

QTreeView::branch:has-siblings:adjoins-item {
        background: red;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
        background: blue;
}

QTreeView::branch:closed:has-children:has-siblings {
        background: pink;
}

QTreeView::branch:has-children:!has-siblings:closed {
        background: gray;
}

QTreeView::branch:open:has-children:has-siblings {
        background: magenta;
}

QTreeView::branch:open:has-children:!has-siblings {
        background: green;
}
*/

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
    background-color: rgba(61, 173, 232, 0.2);
    outline: 0;
    color: #eff0f1;
    padding: 0.3ex;
}


QSlider::groove:horizontal
{
    border: 0.1ex solid #111111;
    height: 0.4ex;
    background: #565a5e;
    margin: 0ex;
    border-radius: 0.2ex;
}

QSlider::handle:horizontal
{
    background: #232629;
    border: 0.1ex solid #626568;
    width: 1.6ex;
    height: 1.6ex;
    margin: -0.8ex 0;
    border-radius: 0.9ex;
}

QSlider::groove:vertical
{
    border: 0.1ex solid #111111;
    width: 0.4ex;
    background: #565a5e;
    margin: 0ex;
    border-radius: 0.3ex;
}

QSlider::handle:vertical
{
    background: #232629;
    border: 0.1ex solid #626568;
    width: 1.6ex;
    height: 1.6ex;
    margin: 0 -0.8ex;
    border-radius: 0.9ex;
}

QSlider::handle:horizontal:hover,
QSlider::handle:horizontal:focus,
QSlider::handle:vertical:hover,
QSlider::handle:vertical:focus
{
    border: 0.1ex solid #3daee9;
}

QSlider::sub-page:horizontal,
QSlider::add-page:vertical
{
    background: #3daee9;
    border-radius: 0.3ex;
}

QSlider::add-page:horizontal,
QSlider::sub-page:vertical
{
    background: #626568;
    border-radius: 0.3ex;
}

QToolButton
{
    background-color: transparent;
    border: 0.1ex solid #76797c;
    border-radius: 0.2ex;
    margin: 0.3ex;
    padding: 0.5ex;
}

QToolButton[popupMode="1"]  /* only for MenuButtonPopup */
{
    padding-right: 2ex; /* make way for the popup button */
}

QToolButton[popupMode="2"]  /* only for InstantPopup */
{
    padding-right: 1ex; /* make way for the popup button */
}

QToolButton::menu-indicator
{
    border-image: none;
    image: url(:themes/dark/down_arrow.svg);
    top: -0.7ex;
    left: -0.2ex;
}

QToolButton::menu-arrow
{
    border-image: none;
    image: url(:themes/dark/down_arrow.svg);
}

QToolButton:hover,
QToolButton::menu-button:hover
{
    background-color: transparent;
    border: 0.1ex solid #3daee9;
}

QToolButton:checked,
QToolButton:pressed,
QToolButton::menu-button:pressed
{
    background-color: #3daee9;
    border: 0.1ex solid #3daee9;
    padding: 0.5ex;
}

QToolButton::menu-button
{
    border: 0.1ex solid #76797c;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* 1ex width + 0.4ex for border + no text = 2ex allocated above */
    width: 1ex;
    padding: 0.5ex;
    outline: none;
}

QToolButton::menu-arrow:open
{
    border: 0.1ex solid #76797c;
}

QTableView
{
    border: 0.1ex solid #76797c;
    gridline-color: #111111;
    background-color: #232629;
}


QTableView,
QHeaderView
{
    border-radius: 0px;
}

QTableView::item:pressed,
QListView::item:pressed,
QTreeView::item:pressed
{
    background: #3daee9;
    color: #eff0f1;
}

QTableView::item:selected:active,
QTreeView::item:selected:active,
QListView::item:selected:active
{
    background: #3daee9;
    color: #eff0f1;
}

QListView::item:selected:hover,
QTreeView::item:selected:hover
{
    background-color: #47b8f3;
    color: #eff0f1;
}

QHeaderView
{
    background-color: #111111;
    border: 0.1ex transparent;
    border-radius: 0px;
    margin: 0px;
    padding: 0px;

}

QHeaderView::section
{
    background-color: #111111;
    color: #eff0f1;
    padding: 0.5ex;
    border: 0.1ex solid #76797c;
    border-radius: 0px;
    text-align: center;
}

QHeaderView::section::vertical::first,
QHeaderView::section::vertical::only-one
{
    border-top: 0.1ex solid #76797c;
}

QHeaderView::section::vertical
{
    border-top: transparent;
}

QHeaderView::section::horizontal::first,
QHeaderView::section::horizontal::only-one
{
    border-left: 0.1ex solid #76797c;
}

QHeaderView::section::horizontal
{
    border-left: transparent;
}


QHeaderView::section:checked
{
    color: white;
    background-color: #334e5e;
}

/* style the sort indicator */
QHeaderView::down-arrow
{
    image: url(:themes/dark/down_arrow.svg);
}

QHeaderView::up-arrow
{
    image: url(:themes/dark/up_arrow.svg);
}

QTableCornerButton::section
{
    background-color: #111111;
    border: 0.1ex transparent #76797c;
    border-radius: 0px;
}

QToolBox
{
    padding: 0.5ex;
    border: 0.1ex transparent black;
}

QToolBox:selected
{
    background-color: #111111;
    border-color: #3daee9;
}

QToolBox:hover
{
    border-color: #3daee9;
}

QStatusBar
{
    background-color : transparent;
}

QStatusBar::item
{
    border: 0px transparent dark;
}

QFrame[height="3"],
QFrame[width="3"]
{
    background-color: #76797c;
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
    background : rgba(0,0,0,200);
}

QFrame#title_bar
{
    background : rgba(0,0,0,255);
}

QFrame#settings_toolbar
{
    background : rgba(0,0,0,220);
}

QFrame#vertical_line_page_1
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#vertical_line_page_1_2
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#line_win_set_top
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#line_games_bot
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#line_label_customize
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#line_label_games
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#line_label_window_settings
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
} 


QFrame#Snake
{
    border : 2px solid cyan;
    background : transparent;
    background-color : transparent;
}

QFrame#Tetris
{
    border : 2px solid cyan;
    background : transparent;
    background-color : transparent;
}

QFrame#line_2_3
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#line_3_4
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#line_1_2
{
    border : 1px solid #4b4b4b;
    background : #4b4b4b;
}

QFrame#frame_customize, QFrame#frame_games, QFrame#mini_frame_window
{
    background : qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.539773, stop:0 rgba(0, 10, 75, 134), stop:1 rgba(14, 15, 111, 130));
    border : 1px solid #2a2aff;
}

QDialog
{
    border : 1px solid cyan;
}

QPushButton#btn_dialog_yes
{
    border : 1px solid cyan;
}

QPushButton#btn_dialog_no
{
    border : 1px solid cyan;
}

QPushButton#btn_dialog_kill_self
{
    border : 1px solid cyan;
}

QPushButton#btn_toolbar_1
{
    background : transparent;   
    border-image: url(:buttons/dark/btn_toolbar_1.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_toolbar_3
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_toolbar_3.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_toolbar_2
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_toolbar_2.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_toolbar_4
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_toolbar_4.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_toolbar_1:hover,QPushButton#btn_toolbar_3:hover, QPushButton#btn_toolbar_2:hover,
QPushButton#btn_toolbar_4:hover
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #00017e, stop: 0.5 #000170);   border: 0.1ex solid #3daee9;
    color: #eff0f1;    
}

QPushButton#btn_toolbar_1:focus:pressed,QPushButton#btn_toolbar_3:focus:pressed, QPushButton#btn_toolbar_2:focus:pressed,
QPushButton#btn_toolbar_4:focus:pressed,
QPushButton#btn_toolbar_1:pressed,QPushButton#btn_toolbar_3:pressed, QPushButton#btn_toolbar_2:pressed,
QPushButton#btn_toolbar_4:pressed
{
    background-color: #111111;
    padding-top: -1.5ex;
    padding-bottom: -1.7ex;
}

QPushButton#btn_toolbar_1:checked,QPushButton#btn_toolbar_3:checked, QPushButton#btn_toolbar_2:checked,
QPushButton#btn_toolbar_4:checked
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #00017e, stop: 0.5 #000170);   border: 0.1ex solid #3daee9;
    border-color: #6A6969;
}

QPushButton#btn_settings_tetris
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_tetris.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_snake
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_snake.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_open_chat
{   
    background : transparent;
    border-image: url(:buttons/dark/btn_settings_chat.png) 0 0 0 0 stretch stretch;
}

QPushButton#btn_settings_tetris:hover, QPushButton#btn_settings_snake:hover, QPushButton#btn_settings_add_bck:hover,
QPushButton#btn_settings_chg_bck:hover, QPushButton#btn_settings_open_chat:hover, QPushButton#btn_settings_chg_font:hover
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #00017e, stop: 0.5 #000170);
    border: 0.1ex solid #3daee9;
    color: #eff0f1;    
}


QPushButton#btn_settings_tetris:focus:pressed, QPushButton#btn_settings_snake:focus:pressed, QPushButton#btn_settings_add_bck:focus:pressed,
QPushButton#btn_settings_chg_bck:focus:pressed, QPushButton#btn_settings_open_chat:focus:pressed, QPushButton#btn_settings_chg_font:focus:pressed,
QPushButton#btn_settings_tetris:pressed, QPushButton#btn_settings_snake:pressed, QPushButton#btn_settings_add_bck:pressed,
QPushButton#btn_settings_chg_bck:pressed, QPushButton#btn_settings_open_chat:pressed, QPushButton#btn_settings_chg_font:pressed
{
    background-color: #111111;
    padding-top: -1.5ex;
    padding-bottom: -1.7ex;
}
QSplitter::handle
{
    border: 0.1ex dashed #76797c;
}

QSplitter::handle:hover
{
    background-color: #787876;
    border: 0.1ex solid #76797c;
}

QSplitter::handle:horizontal
{
    width: 0.1ex;
}

QSplitter::handle:vertical
{
    height: 0.1ex;
}

QProgressBar {	
	background-color: rgb(98, 114, 164);
	color: rgb(0,255,255);
	border-style: none;
	border-radius: 10px;
	text-align: center;
}
QProgressBar::chunk{
	border-radius: 10px;
	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(0, 230, 255, 255), stop:1 rgba(170, 85, 255, 255));
}
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


QProgressBar:horizontal
{
    background-color: #626568;
    border: 0.1ex solid #111111;
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
    background-color: #3daee9;
    border: 0.1ex transparent;
    border-radius: 0.3ex;
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
    border-image: url(:themes/dark/up_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::up-arrow:hover,
QSpinBox::up-arrow:pressed,
QDoubleSpinBox::up-arrow:hover,
QDoubleSpinBox::up-arrow:pressed
{
    border-image: url(:themes/dark/up_arrow-hover.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::up-arrow:disabled,
QSpinBox::up-arrow:off,
QDoubleSpinBox::up-arrow:disabled,
QDoubleSpinBox::up-arrow:off
{
border-image: url(:themes/dark/up_arrow_disabled.svg);
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
    border-image: url(:themes/dark/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::down-arrow:hover,
QSpinBox::down-arrow:pressed,
QDoubleSpinBox::down-arrow:hover,
QDoubleSpinBox::down-arrow:pressed
{
    border-image: url(:themes/dark/down_arrow-hover.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::down-arrow:disabled,
QSpinBox::down-arrow:off,
QDoubleSpinBox::down-arrow:disabled,
QDoubleSpinBox::down-arrow:off
{
border-image: url(:themes/dark/down_arrow_disabled.svg);
}
"""
dark_bg_pics_cycle = cycle(dark_bg_pics)

def dynamic_main_bg_stylesheet(i_default_stylesheet=stylesheet, i_bg_list=dark_bg_pics, i_placeholder="bg_pic.format"):
    return i_default_stylesheet.replace(i_placeholder, i_bg_list[-1])

def change_background(i_default_stylesheet=stylesheet, i_placeholder="bg_pic.format"):
    next_bg = next(dark_bg_pics_cycle)
    return i_default_stylesheet.replace(i_placeholder, next_bg)

def set_custom_back(custom_bg, i_default_stylesheet=stylesheet, i_placeholder=":themes/backgrounds/dark_bg/bg_pic.format"):
    return i_default_stylesheet.replace(i_placeholder, custom_bg)

"""
def change_global_font_via_qss (new_font, stylesheet=stylesheet, placeholder=["pointSize", "yourFont"]):
    return stylesheet.replace(placeholder[0], f'{new_font.pointSize()}').replace(placeholder[1], f'{new_font.family()}')

"""