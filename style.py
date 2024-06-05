dialog_style = """
    QLabel {
        font-size: 16px;
        font-weight: bold;
    }
    QLineEdit, QComboBox {
        background-color: #f0f0f0; /* Light gray */
        border: 1px solid #ccc; /* Light gray border */
        border-radius: 4px;
        padding: 6px 28px 6px 8px; /* Добавляем отступ справа для стрелки */
        font-size: 16px;
    }
    QComboBox {
        selection-background-color: #0077FF; /* Blue */
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox::down-arrow {
        width: 0;
        height: 0;
        border-left: 0px solid transparent;
        border-right: 0px solid transparent;
        border-top: 0px solid transparent;
        border-bottom: 0px solid transparent;
    }
    QComboBox::down-arrow:on {
        /* when the popup is open, rotate the arrow */
        top: 1px;
        left: 1px;
    }
    QComboBox QAbstractItemView {
        selection-background-color: #0077FF; /* Blue */
        selection-color: white;
    }
    /* Новый стиль для поля ввода даты */
    QDateEdit {
        background-color: #f0f0f0; /* Light gray */
        border: 1px solid #ccc; /* Light gray border */
        border-radius: 4px;
        padding: 6px 8px; /* Отступы слева и справа */
        font-size: 16px;
    }
    QDateEdit::down-arrow {
        width: 0;
        height: 0;
    }
"""

button_style = """
    QPushButton {
        background-color: #0077FF; /* Blue */
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #2E8FFF; /* Darker Blue */
        color: white;
    }
"""

selection_style = """
    QTableWidget::item:selected {
        background-color: #0077FF; /* Синий цвет выделения */
        color: white; /* Цвет текста при выделении */
    }
    QTableWidget::item {
        selection-background-color: #0077FF; /* Синий цвет выделения */
        selection-color: white; /* Цвет текста при выделении */
    }
"""


# Стилизация меню
menu_style = """
    QMenuBar {
        background-color: #f0f0f0;
        border: 1px solid #ababab;
        font-size: 16px;
    }
    QMenuBar::item {
        spacing: 3px;
        padding: 6px 12px;
        background-color: #f0f0f0;
        color: #333;
        border-radius: 3px;
    }
    QMenuBar::item:selected {
        background-color: #d0d0d0;
    }
    QMenu {
        background-color: #f0f0f0;
        border: 1px solid #ababab;
        font-size: 16px;
    }
    QMenu::item {
        padding: 6px 20px;
        background-color: transparent;
        color: #333;
    }
    QMenu::item:selected {
        background-color: #f0f0f0;
    }
    QMenu::item:hover {
        background-color: #f0f0f0;
    }
"""
