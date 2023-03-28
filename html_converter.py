import os
import sys
import re
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore


def debug_trace(ui=None):
    from pdb import set_trace
    QtCore.pyqtRemoveInputHook()
    set_trace()
    # QtCore.pyqtRestoreInputHook()


class HTMLConverter(QWidget):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        super(HTMLConverter, self).__init__()
        ui_path = os.path.join(self.ROOT_DIR, 'html_converter.ui')
        loadUi(ui_path, self)
        self.browse_btn.clicked.connect(self.browse)
        self.convert_to_html.clicked.connect(self.convert_html) #+
        self.send_c_program.clicked.connect(self.send_to_c) #+
        self.file_path = None

    def browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self,
                                              caption='Select file',
                                              directory='',
                                              filter="Text Files (*.txt)",
                                              options=options)
        if file:
            self.file_path = file
            self.path_line_edit.setText(file)
            print(file)

    def send_to_c(self):
        print("C button")
        self.text_rezultat.setText("C button")

    def convert_html(self):
        file = open(self.file_path, 'r')
        file_text = file.read()

        htmltext = ""

        regex = " {3,}[a-zA-Z0-9 ]+\n"
        title = re.findall(regex, file_text)[0]
        title = title.strip()

        regex = "\n[a-zA-Z0-9 .]+\n"
        paragraphs = re.findall(regex, file_text)
        paragraph_list = []
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if paragraph != title:
                paragraph_list.append(paragraph);

        htmltext += "<html>\n\t<head>\n\t\t<title>\n\t\t\t" + title + "\n\t\t</title>\n\t</head>\n\t<body>\n"
        for paragraph in paragraph_list:
            htmltext += "\t\t<p1>" + paragraph + "</p1>\n"
        htmltext += "\t</body>\n</html>"

        self.text_rezultat.setPlainText(htmltext)

        file_out = open("result.html", "w")
        file_out.write(htmltext)
        print(htmltext)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HTMLConverter()
    window.show()
    sys.exit(app.exec_())
