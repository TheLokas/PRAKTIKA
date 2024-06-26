import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QLineEdit, \
    QVBoxLayout, QWidget, QHeaderView, QPushButton, QHBoxLayout, QAbstractItemView
from PyQt5.QtCore import Qt
from style import selection_style, button_style
from modulDB import load_data
from newPatient import AddPatientDialog
from PatientWindow import PatientInfoDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sort_order = {}
        self.column_index = {}

        self.setWindowTitle("Приложение для работы с пациентами")

        # Получаем размеры экрана
        screen_geometry = QApplication.desktop().screenGeometry()

        # Устанавливаем размеры окна
        self.setGeometry(screen_geometry)

        # Создание и настройка виджетов
        self.table = QTableWidget()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Введите ФИО для поиска")

        # Увеличение размеров шрифтов и элементов
        font = self.font()
        font.setPointSize(12)  # Установите желаемый размер шрифта
        self.table.setFont(font)
        self.search_box.setFont(font)
        self.table.verticalHeader().setFont(font)

        # Создание вертикального макета для размещения виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.search_box)
        layout.addWidget(self.table)

        # Создание и установка центрального виджета
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Установка заголовка таблицы
        # Устанавливаем заголовки таблицы
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ФИО", "Адрес", "Номер телефона"])

        # Устанавливаем стиль для заголовков столбцов
        header_font = self.table.horizontalHeader().font()
        header_font.setBold(True)  # Жирный шрифт
        self.table.horizontalHeader().setFont(header_font)

        # Подключение обработчика событий изменения текста в поле поиска

        # Установка режима изменения размера столбцов
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Устанавливаем поведение выделения для строки
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Подключение обработчика событий двойного клика по ячейке

        # Создание горизонтального макета для кнопок
        buttons_layout = QHBoxLayout()

        # Стилизация кнопок

        # Добавление горизонтального макета кнопок в вертикальный макет
        layout.addLayout(buttons_layout)
        # Установка выравнивания кнопок справа внизу
        buttons_layout.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.table.setStyleSheet(selection_style)
        self.search_box.textChanged.connect(self.search_patients)

        # Создание кнопки "Добавить пациента"
        add_patient_button = QPushButton("Добавить пациента")

        add_patient_button.setStyleSheet(button_style)
        # Добавляем кнопку в горизонтальный макет
        buttons_layout.addWidget(add_patient_button)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Загрузка данных в таблицу
        load_data(self.table)
        # Подключение обработчика событий двойного клика по ячейке
        self.table.cellDoubleClicked.connect(self.show_patient_info)

        # Подключение обработчика событий нажатия на кнопку "Добавить пациента"
        add_patient_button.clicked.connect(self.open_add_patient_dialog)
        # Подключение обработчика событий щелчка по заголовку столбца
        self.table.horizontalHeader().sectionClicked.connect(self.sort_table)

    def show_patient_info(self, row, column):
        # Получаем данные о пациенте из выбранной строки
        full_name = self.table.item(row, 0).text()
        address = self.table.item(row, 1).text()
        phone_number = self.table.item(row, 2).text()

        # Создаем и отображаем окно с информацией о пациенте
        patient_info_dialog = PatientInfoDialog(full_name, address, phone_number)
        patient_info_dialog.exec_()

    def sort_table(self, logical_index):
        # Определение индекса столбца по которому был выполнен щелчок
        self.table.sortItems(logical_index)

    def open_add_patient_dialog(self):
        # Создание и отображение диалогового окна для добавления пациента
        dialog = AddPatientDialog(self.table)
        dialog.exec_()

    def search_patients(self):
        search_text = self.search_box.text().lower()
        for row in range(self.table.rowCount()):
            visible = False
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item and search_text in item.text().lower():
                    visible = True
                    break
            self.table.setRowHidden(row, not visible)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.showMaximized()
    sys.exit(app.exec_())
