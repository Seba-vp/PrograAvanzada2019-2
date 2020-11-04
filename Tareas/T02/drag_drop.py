import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import QMimeData, Qt
import parametros_generales

class DraggableLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        
        drag.setMimeData(mimedata)

        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class DropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.plantar_signal = None 

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()       
        text = event.mimeData().text()
        if text == 'Semillas Choclo':
            #self.setText('c1')
            self.setPixmap(QPixmap(parametros_generales.paths_cultivos['c1']))
            self.plantar_signal.emit([self.x(), self.y(), 'c'])
        elif text == 'Semillas Alcachofa':
            #self.setText('a1')
            self.setPixmap(QPixmap(parametros_generales.paths_cultivos['a1']))
            self.plantar_signal.emit([self.x(), self.y(), 'a'])
        event.acceptProposedAction()
