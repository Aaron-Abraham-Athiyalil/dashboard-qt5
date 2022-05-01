# PyQt5 Dashboard
A fully operational dashboard made with PyQt5, with a custom splashscreen (followed [this tutorial](https://www.youtube.com/watch?v=Ap865V3sAdw)), modified light and dark breeze themes (courtesy of [Alexhuszagh](https://github.com/Alexhuszagh/BreezeStyleSheets)), custom modern animated toggles in lieu of checkboxes (followed [this tutorial](https://www.youtube.com/watch?v=NnJFi285s3M)), background changer, custom background option and even some basic games too (snake + tetris)!

This is my very first fully operational app using Python PyQt5, I made it when we needed a sort of AIO dashboard at work. Obviously I removed anything relating to work and just made it as a template, you will have to add functionality to it depending on your needs. Of course, there is a lot to improve, many things are messy, so if you can enhance it even more that would be awesome !
# Screenshots
Also check the screeshots folder for a video preview and for more pictures.
<br/><br/>
<img src="/screenshots/dash_07.PNG" width="400" height="240"/> <img src="/screenshots/dash_11.PNG" width="500" height="350"/>
<img src="/screenshots/dash_06.PNG" width="500" height="350"/> <img src="/screenshots/dash_05.PNG" width="500" height="350"/>

# Notes about .ui changes
If you decide to modify the .ui files with QtDesigner, do not forget to change the imports from pyside2 to pyqt5 after you're done. Also, you will have to modify some things to get the new UI elements :
1. Copy the new ui from QtDesigner into "ui_main.py".
2. Replace imports and add this to them:
``` python
from interface_scripts.check_box import check_box
from interface_scripts.clickable_frame import clickable_frame
from ressources import ressources
```
2. Now you need to update the checkboxes with the updated toggles, for example :<br/>Replace this :
``` python
self.chkbox_settings_chg_theme = QCheckBox(self.frame_label_dark_theme)
```
With this :
``` python
self.chkbox_settings_chg_theme = check_box()
```
3. You will also need to update the the title bar frame and make it clickable or the code won't work :<br/>Replace this :
``` python
self.frame_title = QFrame(self.title_bar)
```
With this :
``` python
self.frame_title = clickable_frame(self.title_bar)
```
To be honest I made a script that automatically makes these changes, I was just too lazy doing it each and every time I made a small change in the ui!

# Notes about ressources
If you need to change or update some ressources, for example icons or background pictures, make sure you update the "ressources.qrc" file with appropriate names, then you will need to generate a new "ressources.py" file, this is done by using pyrcc5, in a cmd window type:<br/>
``` cmd
pyrcc5 -o path\to\ressources.py path\to\ressources.qrc
```
Another thing is not to forget to update the stylsheets (both "dark_stylesheets.py" and "light_stylesheets.py") with your new ressources !
<br/>
If you need any help on how to perform any of these changes just get in touch and we'll figure it out.
# Requirements
pip install PyQt5
