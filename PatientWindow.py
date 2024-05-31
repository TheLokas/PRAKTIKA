from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout

class PatientInfoDialog(QDialog):
    def __init__(self, full_name, address, phone_number):
        super().__init__()

        self.setWindowTitle("Информация о пациенте")

        # Создание меток для отображения информации о пациенте
        self.full_name_label = QLabel(f"ФИО: {full_name}")
        self.address_label = QLabel(f"Адрес: {address}")
        self.phone_number_label = QLabel(f"Номер телефона: {phone_number}")

        # Создание вертикального макета для размещения меток
        layout = QVBoxLayout()
        layout.addWidget(self.full_name_label)
        layout.addWidget(self.address_label)
        layout.addWidget(self.phone_number_label)
        self.setLayout(layout)
