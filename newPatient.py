from PyQt5.QtWidgets import (
    QDialog, QLabel, QPushButton, QVBoxLayout,
    QLineEdit, QDateEdit, QHBoxLayout, QMessageBox, QComboBox
)
from style import button_style, dialog_style
import re
from modulDB import add_patient_to_db, load_data
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Contract

class AddPatientDialog(QDialog):
    def __init__(self, table_widget):
        super().__init__()
        self.table_widget = table_widget
        self.setWindowTitle("Добавление пациента")

        # Создание меток и полей для ввода данных
        self.full_name_label = QLabel("ФИО:")
        self.full_name_edit = QLineEdit()

        self.date_of_birth_label = QLabel("Дата рождения:")
        self.date_of_birth_edit = QDateEdit()
        self.date_of_birth_edit.setDisplayFormat("dd.MM.yyyy")

        self.address_label = QLabel("Адрес:")
        self.address_edit = QLineEdit()

        self.phone_number_label = QLabel("Номер телефона:")
        self.phone_number_edit = QLineEdit()

        self.passport_label = QLabel("Паспорт:")
        self.passport_edit = QLineEdit()

        self.contract_label = QLabel("Номер договора:")
        self.contract_combo = QComboBox()
        self.contract_combo.addItem("")  # По умолчанию пустой элемент
        self.load_contracts()

        self.add_button = QPushButton("Добавить")
        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.setStyleSheet(button_style)
        self.add_button.setStyleSheet(button_style)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout()
        layout.addWidget(self.full_name_label)
        layout.addWidget(self.full_name_edit)
        layout.addWidget(self.date_of_birth_label)
        layout.addWidget(self.date_of_birth_edit)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_edit)
        layout.addWidget(self.phone_number_label)
        layout.addWidget(self.phone_number_edit)
        layout.addWidget(self.passport_label)
        layout.addWidget(self.passport_edit)
        layout.addWidget(self.contract_label)
        layout.addWidget(self.contract_combo)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_patient)
        self.cancel_button.clicked.connect(self.close_dialog)
        self.setStyleSheet(dialog_style)

    def load_contracts(self):
        engine = create_engine('mysql://gen_user:^wVTtDGXXsiF36@147.45.140.206:3306/PRAKTIKA')
        Session = sessionmaker(bind=engine)
        session = Session()

        contracts = session.query(Contract).all()
        for contract in contracts:
            self.contract_combo.addItem(contract.contract_number)

        session.close()

    def add_patient(self):
        full_name = self.full_name_edit.text()
        date_of_birth = self.date_of_birth_edit.date().toString("yyyy-MM-dd")
        address = self.address_edit.text()
        phone_number = self.phone_number_edit.text()
        passport = self.passport_edit.text()
        contract_number = self.contract_combo.currentText()

        full_name_pattern = re.compile(r'^[А-Яа-яёЁ]+(?:\s[А-Яа-яёЁ]+){1,2}$')
        if not full_name_pattern.match(full_name):
            QMessageBox.warning(self, "Ошибка", "ФИО должно состоять из 2 или 3 слов, содержащих только русские буквы.")
            return

        phone_pattern = re.compile(r'^(\+7|8)?\d{10}$')
        if not phone_pattern.match(phone_number):
            QMessageBox.warning(self, "Ошибка",
                                "Номер телефона должен быть российским (начинаться на +7 или 8) и состоять из 11 цифр.")
            return

        passport_pattern = re.compile(r'^\d{10}$')
        if not passport_pattern.match(passport):
            QMessageBox.warning(self, "Ошибка", "Паспорт должен состоять из 10 цифр.")
            return

        add_patient_to_db(full_name, date_of_birth, address, phone_number, passport, contract_number)
        QMessageBox.information(self, "Успех", "Пациент успешно добавлен в базу данных.")
        self.close()
        load_data(self.table_widget)

    def close_dialog(self):
        self.close()
