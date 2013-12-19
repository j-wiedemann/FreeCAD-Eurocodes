# -*- coding: utf-8 -*-
# FreeCAD init script of the Eurocodes module
# (c) 2013 Jonathan Wiedemann

#***************************************************************************
#*   (c) Jonathan Wiedemann (jonatan@wiedemann.fr) 2013                    *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#*   Jonathan Wiedemann 2013                                               *
#***************************************************************************/



class EurocodesWorkbench ( Workbench ):
    "Eurocodes workbench object"
    Icon = """
/* XPM */
static char * infologo_xpm[] = {
"16 16 33 1",
" 	c None",
".	c #61320B",
"+	c #5D420B",
"@	c #4F4C09",
"#	c #564930",
"$	c #754513",
"%	c #815106",
"&	c #666509",
"*	c #875F55",
"=	c #6E7000",
"-	c #756A53",
";	c #717037",
">	c #946637",
",	c #92710E",
"'	c #797A0A",
")	c #7C7720",
"!	c #8A8603",
"~	c #88886F",
"{	c #AF8181",
"]	c #999908",
"^	c #BB8D8D",
"/	c #AAAA00",
"(	c #A9A880",
"_	c #B5B419",
":	c #C1A9A9",
"<	c #B1B19A",
"[	c #BEBE00",
"}	c #B9B8B4",
"|	c #CACC00",
"1	c #D4D4BC",
"2	c #DBD2D0",
"3	c #EEEEED",
"4	c None",
"4444444444444444",
"4444443113444444",
"4444<;']]!;<^^24",
"444(&@!]]]=&#^{3",
"44<']')@++)!&*{^",
"44)]/[|//[/]'@{{",
"42=/_|||||[]!&*{",
"4(&][|||||[/'@#}",
"3-..,|||||[)&&~4",
"^*$%.!|||[!+/](4",
"^{%%%._[[_&/[_14",
":{>%%.!//])_[_44",
"2{{%%+!]!!)]]344",
"4:{{#@&=&&@#3444",
"44224}~--~}44444",
"4444444444444444"};
"""
    MenuText = "Eurocodes"
    ToolTip = "Eurocodes workbench"
    
    def Initialize(self) :
        import EC5Flexion
        self.appendToolbar("EurocodesTools",['EC5_Poutre'])
        self.appendMenu('EurocodesTools',['EC5_Poutre'])
        import EC1Neige
        self.appendToolbar("EurocodesTools",['EC1_Neige'])
        self.appendMenu('EurocodesTools',['EC1_Neige'])
        #self.appendMenu('EurocodesTools',['EC5_Widget'])
    
        ###self.appendCommandbar("&Generic Tools",["ColorCodeShape"])
    def GetClassName(self):
        #return "InfoGui::Workbench"
        return "Gui::PythonWorkbench"

Gui.addWorkbench(EurocodesWorkbench())
#App.addImportType("OpenSCAD CSG Format (*.csg)","importCSG")
#App.addExportType("OpenSCAD CSG Format (*.csg)","exportCSG") 
#App.addExportType("OpenSCAD Format (*.scad)","exportCSG")
#App.addImportType("OpenSCAD CSG prototype (*.csg)","prototype") #prototype

