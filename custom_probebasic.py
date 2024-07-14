from probe_basic.probe_basic import ProbeBasic
from PyQt5 import QtCore # , QtGui, QtWidgets

class CustomProbeBasic(ProbeBasic):
    """Main window class for the ProbeBasic VCP.


    save this file as custom_probebasic.py in you config directory
    then your custom_config.yml add the provider: line below to the mainwidow: section

    ```
    windows:
      mainwindow:
        provider: custom_probebasic:CustomProbeBasic
    ```       

    """

    def __init__(self, *args, **kwargs):
        super(CustomProbeBasic, self).__init__(*args, **kwargs)
        _translate = QtCore.QCoreApplication.translate

        # Set Default tab
        self.tabWidget.setCurrentIndex(0)


        atc_tab_index = self.tabWidget.indexOf(self.atc_tab)
        self.tabWidget.removeTab(atc_tab_index)

        status_tab_index = self.tabWidget.indexOf(self.status_tab)
        self.tabWidget.removeTab(status_tab_index)


        # rename the Flood button
        self.flood_button.setText("MQL")

        # rename the Mist button
        self.mist_button.setText("Air")