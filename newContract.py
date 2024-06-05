from PyQt5.QtWidgets import (
    QDialog, QLabel, QPushButton, QVBoxLayout,
    QLineEdit, QDateEdit, QHBoxLayout, QMessageBox, QComboBox, QSpinBox
)
from style import button_style, dialog_style
import re
from modulDB import add_contract_to_db, load_contract_data
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Company

class AddContractDialog(QDialog):
    def __init__(self, table_widget):
        super().__init__()
        self.company_dict = None
        self.table_widget = table_widget
        self.setWindowTitle("Добавление договора")

        # Создание меток и полей для ввода данных
        self.contract_label = QLabel("Компания:")
        self.contract_combo = QComboBox()
        self.contract_combo.addItem("")  # По умолчанию пустой элемент
        self.load_company()

        self.start_date_label = QLabel("Дата начала:")
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setDisplayFormat("dd.MM.yyyy")

        self.end_date_label = QLabel("Дата окончания:")
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setDisplayFormat("dd.MM.yyyy")

        self.worker_count_label = QLabel("Количество сотрудников:")
        self.worker_count_edit = QSpinBox()
        self.worker_count_edit.setRange(1, 10000)

        self.total_cost_label = QLabel("Сумма:")
        self.total_cost_edit = QSpinBox()
        self.total_cost_edit.setRange(1, 100000000)


        self.add_button = QPushButton("Добавить")
        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.setStyleSheet(button_style)
        self.add_button.setStyleSheet(button_style)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout()
        layout.addWidget(self.contract_label)
        layout.addWidget(self.contract_combo)
        layout.addWidget(self.start_date_label)
        layout.addWidget(self.start_date_edit)
        layout.addWidget(self.end_date_label)
        layout.addWidget(self.end_date_edit)
        layout.addWidget(self.worker_count_label)
        layout.addWidget(self.worker_count_edit)
        layout.addWidget(self.total_cost_label)
        layout.addWidget(self.total_cost_edit)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_patient)
        self.cancel_button.clicked.connect(self.close_dialog)
        self.setStyleSheet(dialog_style)

    def load_company(self):
        engine = create_engine('mysql://gen_user:^wVTtDGXXsiF36@147.45.140.206:3306/PRAKTIKA')
        Session = sessionmaker(bind=engine)
        session = Session()

        company_list =[]

        Companies = session.query(Company).all()
        for company in Companies:
            company_list.append([company.name, company.id])
            self.contract_combo.addItem(company.name)

        self.company_dict = dict(company_list)
        session.close()

    def add_patient(self):
        start_date = self.start_date_edit.date().toPyDate()
        end_date = self.end_date_edit.date().toPyDate()
        worker_count = self.worker_count_edit.text()
        total_cost = self.total_cost_edit.text()

        if self.contract_combo.currentText() == "":
            QMessageBox.warning(self, "Ошибка", "Необходимо выбрать компанию.")
            return

        company = self.company_dict[self.contract_combo.currentText()]

        if start_date >= end_date:
            QMessageBox.warning(self, "Ошибка", "Дата окончания договора должна быть больше даты начала.")
            return

        add_contract_to_db(company=company, start=start_date, end=end_date, worker_count=worker_count, total_cost=total_cost)
        QMessageBox.information(self, "Успех", "Договор успешно добавлен.")
        print(f"{start_date}, {end_date}, {company}")
        self.close()
        load_contract_data(self.table_widget)

    def close_dialog(self):
        self.close()
