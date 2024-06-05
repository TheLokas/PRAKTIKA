import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Patient, Contract
from PyQt5.QtWidgets import QTableWidgetItem

def load_data(table):
    engine = create_engine('mysql://gen_user:^wVTtDGXXsiF36@147.45.140.206:3306/PRAKTIKA')
    Session = sessionmaker(bind=engine)
    session = Session()

    table.setRowCount(0)
    patients = session.query(Patient).all()

    for patient in patients:
        row_position = table.rowCount()
        table.insertRow(row_position)
        if patient.middlename:
            full_name = f"{patient.surname} {patient.name} {patient.middlename}"
        else:
            full_name = f"{patient.surname} {patient.name}"
        table.setItem(row_position, 0, QTableWidgetItem(full_name))
        table.setItem(row_position, 1, QTableWidgetItem(patient.address))
        table.setItem(row_position, 2, QTableWidgetItem(patient.phone_number))

    session.close()

def add_patient_to_db(full_name, address, phone_number, passport, contract_number):
    engine = create_engine('mysql://gen_user:^wVTtDGXXsiF36@147.45.140.206:3306/PRAKTIKA')
    Session = sessionmaker(bind=engine)
    session = Session()

    name_parts = full_name.split()
    surname = name_parts[0]
    name = name_parts[1]
    middlename = name_parts[2] if len(name_parts) > 2 else None

    contract = session.query(Contract).filter_by(contract_number=contract_number).first()

    new_patient = Patient(
        name=name,
        surname=surname,
        middlename=middlename,
        address=address,
        phone_number=phone_number,
        passport=passport,
        contract=contract
    )

    session.add(new_patient)
    session.commit()
    session.close()

def load_contract_data(table):
    engine = create_engine('mysql://gen_user:^wVTtDGXXsiF36@147.45.140.206:3306/PRAKTIKA')
    Session = sessionmaker(bind=engine)
    session = Session()

    table.setRowCount(0)
    contracts = session.query(Contract).all()

    for contract in contracts:
        #print(contract.company.name)
        row_position = table.rowCount()
        table.insertRow(row_position)
        table.setItem(row_position, 0, QTableWidgetItem(contract.contract_number))
        table.setItem(row_position, 1, QTableWidgetItem(str(contract.company.name)))
        table.setItem(row_position, 2, QTableWidgetItem(str(contract.start_date)))
        table.setItem(row_position, 3, QTableWidgetItem(str(contract.end_date)))

    session.close()

def add_contract_to_db(start: datetime.date, end: datetime.date, worker_count: int, total_cost: int, company: int):
    engine = create_engine('mysql://gen_user:^wVTtDGXXsiF36@147.45.140.206:3306/PRAKTIKA')
    Session = sessionmaker(bind=engine)
    session = Session()

    new_contract = Contract(company_id=company,
                            start_date=start, end_date=end,
                            worker_count=worker_count, total_cost=total_cost)

    session.add(new_contract)
    session.commit()

    new_contract.contract_number= new_contract.id + 1000

    session.commit()
    session.close()
