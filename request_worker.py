from PyQt5.QtCore import pyqtSignal, pyqtSlot, QRunnable, QObject

class RequestWorker(QRunnable):
    class Signals(QObject):
        finished = pyqtSignal()
        result = pyqtSignal(dict)
        error = pyqtSignal(str)

        def __init__(self, parent=None):
                return super().__init__(parent=parent)

    def __init__(self, request, parent=None):
        super(RequestWorker, self).__init__()
        self.request = request
        self.signals = RequestWorker.Signals(parent=parent)

    @pyqtSlot()
    def run(self):
        try:
            result = self.request()
            self.signals.result.emit(result)
        except Exception as err:
            self.signals.error.emit(str(err))
        self.signals.finished.emit()