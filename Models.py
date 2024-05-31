from sqlalchemy import create_engine, Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Модель Пациента
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    middlename = Column(String(100), nullable=True)  # Отчество может быть null
    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    passport = Column(String(20), nullable=False)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    contract = relationship("Contract", back_populates="patients")

# Модель Контракта
class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    contract_number = Column(String(50), nullable=False)  # Номер договора
    company_id = Column(Integer, ForeignKey('companies.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    worker_count = Column(Integer, nullable=False)
    total_cost = Column(Integer, nullable=False)
    patients = relationship("Patient", back_populates="contract")
    company = relationship("Company", back_populates="contracts")

# Модель Компании
class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    info = Column(String(255), nullable=False)
    delegate = Column(String(100), nullable=False)
    delegate_phone_number = Column(String(20), nullable=False)
    contracts = relationship("Contract", back_populates="company")

# Модель Работника
class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    middlename = Column(String(100), nullable=True)  # Отчество может быть null
    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    passport = Column(String(20), nullable=False)
    post = Column(String(100), nullable=False)
    procedures = relationship("Procedure", back_populates="worker")

# Модель Процедуры
class Procedure(Base):
    __tablename__ = 'procedures'
    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey('workers.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    date = Column(Date, nullable=False)
    worker = relationship("Worker", back_populates="procedures")
    patient = relationship("Patient")
    type_procedure_id = Column(Integer, ForeignKey('type_procedures.id'))
    type_procedure = relationship("TypeProcedure", back_populates="procedures")

# Модель Типа Процедуры
class TypeProcedure(Base):
    __tablename__ = 'type_procedures'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    cost = Column(Float, nullable=False)
    procedures = relationship("Procedure", back_populates="type_procedure")
