# -*- coding: utf-8 -*-
import time
from src.modification_history import HistoryContainer, History
from src.database import Database
from src.observer import Observer, Announcer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QTableWidget, QHeaderView, QFileDialog
from ui.main_window_ui import Ui_MainWindow
from ui.mdi_tableWidget_ui import Ui_MDITableWidget
from ui.student_infoDialog_ui import Ui_StudentInfoInputDialog
from ui.ui_event_infoDialog import Ui_EventInfoInputDialog
from ui.table_editDialog_ui import Ui_TableEditDialog
from PySide6.QtWidgets import QMessageBox
import sys
import csv
from PySide6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QPushButton, QLabel
from PySide6.QtCore import Qt

db:Database = None
header = None
dbAnnouncer = Announcer()
categoryMap = {'C':'綜援', 'F':'全免', 'H':'半免', 'D':'經濟困難', 'S':'特殊', 'all':'所有'}

class SimpleDialog(QMessageBox):
    def __init__(self, title, text, type=QMessageBox.Information):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(type)
        self.exec()

class StudentInfoInputDialog(QWidget, Ui_StudentInfoInputDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Student Information Input")
        self.setWindowIcon(self.windowIcon())
        self.setFixedSize(640, 514)

    def accept(self):
        if self.addStudentData():
            self.close()

    def reject(self):
        self.close()

    def addStudentData(self):
        # Save the data to the database
        for line in self.plainTextEdit.toPlainText().splitlines():
            if line.strip():
                # Split the line by comma and strip whitespace
                data = [item.strip() for item in line.split(',')]
                if len(data) == 4:
                    class_name, class_number, name, category = data
                    db.addStudent(class_name, class_number, name, category)
                    dbAnnouncer.notify('student_added')
                else:
                    SimpleDialog("Input Error", "Invalid input format. Please check your input.")
                    return False
        # Show success message
        SimpleDialog("Input Successful", "Data has been successfully imported.")
        return True


class EventInfoInputDialog(QWidget, Ui_EventInfoInputDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Event Information Input")
        self.setWindowIcon(self.windowIcon())
        self.setFixedSize(640, 480)

    def accept(self):
        if self.addEventData():
            self.close()

    def reject(self):
        self.close()

    def addEventData(self):
        # First, get the event name from the line edit
        event_name = self.eventLineEdit.text()

        # Check if the event name is not empty
        if not event_name:
            SimpleDialog("Input Error", "Please enter a valid event name.")
            return False
        
        # Check if the event name already exists in the database. If yes, ask the user to confirm just add students or abort operation.
        existing_event = db.isEventExists(event_name)
        if existing_event:
            reply = QMessageBox.question(self, "Event Already Exists",
                                         f"The event '{event_name}' already exists. Do you want to add students to it?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return False
            
            eid = db.findEid(event_name)
        else:
            # Time to add the event to the database
            eid = db.addEventWithReturn(event_name)
            dbAnnouncer.notify('event_added')
            SimpleDialog("Input Successful", "Event has been successfully added.")

        # Now, let's add the students to the event, line by line.
        # The whole process will look like a stack being pop from the start of the list.
        # After processing the first line of input, we will remove it from the list.
        # The process will continue until the list is empty.
        # The input format is: class_name, class_number, name

        lines = self.plainTextEdit.toPlainText().splitlines()
        if not lines:
            SimpleDialog("Input Error", "No student data provided.")
            return False
        
        for line in lines:
            if line.strip():
                # Split the line by comma and strip whitespace
                data = [item.strip() for item in line.split(',')]
                if len(data) == 3:
                    class_name, class_number, name = data
                    sid = db.findSid(class_name, class_number, name)
                    if sid:
                        db.addRecord(sid, eid)
                        dbAnnouncer.notify('record_added')
                        lines = lines[1:]  # Remove the first line from the list
                    else:
                        SimpleDialog("Input Error", f"Student {name} not found in the database.")
                        return False
                else:                                                                                                     
                    SimpleDialog("Input Error", "Invalid input format. Please check your input.")
                    return False

            # Update the text edit to show the remaining lines
            self.plainTextEdit.setPlainText('\n'.join(lines))

        SimpleDialog("Input Successful", f"Students have been successfully added to the event '{event_name}'.")
        return True

class MDITableWidget(QWidget, Ui_MDITableWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMinimumSize(320, 240)

        self.pushButton.clicked.connect(self.saveToCSV)

    def setTableData(self, horizontal_header, data):
        self.tableWidget.setColumnCount(len(horizontal_header))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(horizontal_header)

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
                
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def saveToCSV(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv)")
        if file_name:
            with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
                # Write header
                writer = csv.writer(csvfile)
                writer.writerow([self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())])
                # Write data
                writer.writerows([
                    [self.tableWidget.item(i, j).text() if self.tableWidget.item(i, j) else '' for j in range(self.tableWidget.columnCount())]
                    for i in range(self.tableWidget.rowCount())
                ])

class FixedMDITableWidget(MDITableWidget):
    """
    A fixed table widget that does not allow closing the window.
    It is a subclass of MDITableWidget and overrides the closeEvent method.
    """
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        event.ignore()  # Ignore the close event to prevent closing the window

class DataEditDialog(QDialog, Ui_TableEditDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Data Editor")
        self.setWindowIcon(self.windowIcon())
        self.setFixedSize(640, 480)

        self.setTableData(self.studentInfoTable, ['班別', '學號', '姓名', '經濟情況'], db.getAllStudents())
        self.setTableData(self.eventInfoTable, ['活動名稱'], db.getAllEvents())

        self.keyPressEvent = self.keyPressEventHandler

        self.historyContainer = HistoryContainer()
        
    def keyPressEventHandler(self, event):
        if event.key() == Qt.Key_Delete:

            # Check which table is currently active
            if self.studentInfoTable.isCurrentWidget():
                table = self.studentInfoTable
            elif self.eventInfoTable.isCurrentWidget():
                table = self.eventInfoTable
            else:
                return

            selected_rows = table.selectionModel().selectedRows()
            for row in reversed(selected_rows): # Reverse to avoid index shifting
                row_index = row.row()
                # Data are stored in the history container, so we can delete them later
                if table == self.studentInfoTable:
                    self.historyContainer.addHistory(History(
                        action='delete',
                        table='students',
                        class_name=table.item(row_index, 0).text(),
                        class_number=table.item(row_index, 1).text(),
                        std_name=table.item(row_index, 2).text(),
                        category=table.item(row_index, 3).text()
                    ))
                elif table == self.eventInfoTable:
                    self.historyContainer.addHistory(History(
                        action='delete',
                        table='events',
                        event_name=table.item(row_index, 0).text()
                    ))
                # Remove the item from the table
                table.removeRow(row_index)  # This method removes the row from the table, causing index shifting
        else:
            super().keyPressEvent(event)

    def setTableData(self, table: QTableWidget, horizontal_header, data):
        table.setColumnCount(len(horizontal_header))
        table.setRowCount(len(data))
        table.setHorizontalHeaderLabels(horizontal_header)

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(item)))

        table.setSortingEnabled(True)
        table.setAlternatingRowColors(True)
        table.setShowGrid(True)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def accept(self):
        # Save the data to the database
        pass

    def reject(self):
        self.close()

### Competiblity class ###
class MainWindowMeta(type(QMainWindow), type(Observer)):
    pass

class MainWindow(QMainWindow, Ui_MainWindow, Observer, metaclass=MainWindowMeta):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.studentInfoWidget = StudentInfoInputDialog()
        self.eventInfoWidget = EventInfoInputDialog()

        self.actionAbout.triggered.connect(self.showAbout)

        ### Control Panel ###
        self.manualStudentInfoButton.clicked.connect(lambda: self.studentInfoWidget.show())
        self.manualEventInfoButton.clicked.connect(lambda: self.eventInfoWidget.show())
        self.manualEditInfoButton.clicked.connect(self.dataEditor)

        self.studentParticipatesButton.clicked.connect(self.studentParticipates)
        self.studentParticipatesByEventButton.clicked.connect(self.studentParticipatesByEvents)
        self.studentEventTableWithCategoryButton.clicked.connect(self.studentEventTableWithCategory)
        self.studentEventTableWithCategoryAndNameButton.clicked.connect(self.studentEventTableWithCategoryAndName)

        ### Register to the database announcer ###
        dbAnnouncer.register(self)

        ### Load the database and initialize the table widget ###
        global db
        self.studentsSubWindow = FixedMDITableWidget()
        self.mdiArea.addSubWindow(self.studentsSubWindow)
        # Map the fourth column to text using categoryMap
        students_data = db.getAllStudents()
        mapped_students_data = [
            [*row[:3], categoryMap.get(row[3], row[3])] for row in students_data
        ]
        self.studentsSubWindow.setTableData(['班別', '學號', '姓名', '經濟情況'], mapped_students_data)
        self.studentsSubWindow.show()

        self.eventsSubWindow = FixedMDITableWidget()
        self.mdiArea.addSubWindow(self.eventsSubWindow)
        self.eventsSubWindow.setTableData(['活動名稱'], db.getAllEvents())
        self.eventsSubWindow.show()

        self.recordsSubWindow = MDITableWidget()
        self.mdiArea.addSubWindow(self.recordsSubWindow)
        self.recordsSubWindow.setWindowTitle("學生活動紀錄-總數(所有經濟情況)")
        self.recordsSubWindow.setTableData(['活動名稱', '人數'], db.getStudentEventTable())
        self.recordsSubWindow.show()
    
    def dataEditor(self):
        self.tableEditDialog = DataEditDialog()
        self.tableEditDialog.show()

    def studentEventTableWithCategory(self):
        cat = self.categoryPicker() # Show the dialog first
        if cat == None:
            return
        
        self.studentEventTableWithCategorySubWindow = MDITableWidget()
        self.mdiArea.addSubWindow(self.studentEventTableWithCategorySubWindow)
        self.studentEventTableWithCategorySubWindow.setWindowTitle("活動紀錄-總數(經濟情況-" + categoryMap[cat] + ")")
        self.studentEventTableWithCategorySubWindow.setTableData(['活動名稱', '人數'], db.getStudentEventTable(cat))
        self.studentEventTableWithCategorySubWindow.show()

    def studentEventTableWithCategoryAndName(self):
        cat = self.categoryPicker()
        if cat == None:
            return
        self.studentEventTableWithCategoryAndNameSubWindow = MDITableWidget()
        self.mdiArea.addSubWindow(self.studentEventTableWithCategoryAndNameSubWindow)
        self.studentEventTableWithCategoryAndNameSubWindow.setWindowTitle("活動紀錄-姓名(經濟情況-" + categoryMap[cat] + ")")
        self.studentEventTableWithCategoryAndNameSubWindow.setTableData(['活動名稱', '學生姓名'], db.getEventParticipantWithNames(cat))
        self.studentEventTableWithCategoryAndNameSubWindow.show()

    def studentParticipates(self):
        cat = self.categoryPicker()
        if cat == None:
            return
        self.studentParticipatesSubWindow = MDITableWidget()
        self.mdiArea.addSubWindow(self.studentParticipatesSubWindow)
        self.studentParticipatesSubWindow.setWindowTitle("學生活動紀錄-個人(所有活動)-經濟情況(" + categoryMap[cat] + ")")
        self.studentParticipatesSubWindow.setTableData(['班別','學號','姓名','參與活動數目'], db.getStudentsEventCounts(cat))
        self.studentParticipatesSubWindow.show()

    def studentParticipatesByEvents(self):
        cat = self.categoryPicker()
        if cat == None:
            return
        self.studentParticipatesByEventsSubWindow = MDITableWidget()
        self.mdiArea.addSubWindow(self.studentParticipatesByEventsSubWindow)
        self.studentParticipatesByEventsSubWindow.setWindowTitle("學生活動紀錄-個人(所有活動)-經濟情況(" + categoryMap[cat] + ")")
        self.studentParticipatesByEventsSubWindow.setTableData(['班別','學號','姓名','參與活動'], db.getStudentsEventsParticipated(cat))
        self.studentParticipatesByEventsSubWindow.show()

    def notifyUpdate(self, event_type, *args, **kwargs):
        if event_type == 'student_added':
            self.studentsSubWindow.setTableData(['班別','學號','姓名','經濟情況'], db.getAllStudents())
        elif event_type == 'event_added':
            self.eventsSubWindow.setTableData(['活動名稱'], db.getAllEvents())
        elif event_type == 'record_added':
            self.recordsSubWindow.setTableData(['活動名稱', '人數'], db.getStudentEventTable())

    def showAbout(self):
        about_dialog = QMessageBox(self)
        about_dialog.setWindowTitle("About")
        about_dialog.setText("This application was developed by Harry Leung.\n© 2025 All rights reserved.")
        about_dialog.setIcon(QMessageBox.Information)
        about_dialog.exec()

    def findCategory(self, values):
        for i, value in enumerate(values):
            if value not in (None, ''):
                return header[i + 3]
        # If no valid category is found, return None or a default value
        return None # But this should not happen, as enforced by the data itself
    
    def categoryPicker(self):
        categoryPickDialog = QDialog(self)
        categoryPickDialog.setWindowTitle("Select Category")
        categoryPickDialog.setFixedSize(300, 150)
        layout = QVBoxLayout(categoryPickDialog)
        textLabel = QLabel("請選擇學生的經濟情況:", categoryPickDialog)
        layout.addWidget(textLabel)
        categoryComboBox = QComboBox(categoryPickDialog)
        categoryComboBox.addItem("所有",'all')
        categoryComboBox.addItem("綜援",'C')
        categoryComboBox.addItem("全免",'F')
        categoryComboBox.addItem("半免",'H')
        categoryComboBox.addItem("經濟困難",'D')
        categoryComboBox.addItem("特殊",'S')
        layout.addWidget(categoryComboBox)
        okButton = QPushButton("OK", categoryPickDialog)
        okButton.clicked.connect(categoryPickDialog.accept)
        layout.addWidget(okButton)
        categoryPickDialog.setLayout(layout)

        if categoryPickDialog.exec() == QDialog.Accepted:
            selected_category = categoryComboBox.currentData()
            return selected_category
        else:
            return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = Database("database.db")
    if not db.checkIfInitialized():
        db.initializeDB()
        SimpleDialog("Database Initialized", "The database has been initialized.")

    main_window = MainWindow()
    sys.exit(app.exec())