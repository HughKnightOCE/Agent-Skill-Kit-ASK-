#!/usr/bin/env python3
"""
Agent-Skill-Kit Desktop GUI Application
Modern PyQt6 interface for discovering and executing skills
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QTextEdit, QPushButton, QLabel,
    QLineEdit, QSplitter, QTabWidget, QTableWidget, QTableWidgetItem,
    QDialog, QFormLayout, QScrollArea, QMessageBox, QSpinBox, QDoubleSpinBox
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt6.QtGui import QIcon, QFont, QColor
from PyQt6.QtCore import QTimer

from core.ask import SkillManager


class SkillExecutorThread(QThread):
    """Thread to execute skills without blocking UI."""
    
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()
    
    def __init__(self, skill_name: str, args: List[str] = None):
        super().__init__()
        self.skill_name = skill_name
        self.args = args or []
    
    def run(self):
        """Execute the skill in a background thread."""
        try:
            manager = SkillManager()
            result = manager.run_skill(self.skill_name, self.args)
            
            if result == 0:
                self.output_signal.emit(f"\n✅ Skill '{self.skill_name}' completed successfully!")
            else:
                self.error_signal.emit(f"❌ Skill execution returned error code: {result}")
        
        except Exception as e:
            self.error_signal.emit(f"❌ Error executing skill: {str(e)}")
        
        finally:
            self.finished_signal.emit()


class SkillDetailDialog(QDialog):
    """Dialog showing detailed skill information and execution form."""
    
    def __init__(self, skill_name: str, skill_data: Dict, parent=None):
        super().__init__(parent)
        self.skill_name = skill_name
        self.skill_data = skill_data
        self.manifest = skill_data['manifest']
        self.executor_thread = None
        
        self.setWindowTitle(f"Execute: {self.manifest.get('name', skill_name)}")
        self.setGeometry(100, 100, 600, 500)
        self.init_ui()
    
    def init_ui(self):
        """Initialize the dialog UI."""
        layout = QVBoxLayout()
        
        # Skill info
        info_layout = QVBoxLayout()
        
        title = QLabel(self.manifest.get('name', self.skill_name))
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        info_layout.addWidget(title)
        
        description = QLabel(self.manifest.get('description', 'No description'))
        description.setWordWrap(True)
        info_layout.addWidget(description)
        
        version = QLabel(f"Version: {self.manifest.get('version', '?')}")
        version.setStyleSheet("color: gray;")
        info_layout.addWidget(version)
        
        layout.addLayout(info_layout)
        layout.addWidget(QLabel("─" * 50))
        
        # Arguments form
        form_layout = QFormLayout()
        self.arg_inputs = {}
        
        args = self.manifest.get('arguments', [])
        if args:
            for arg in args:
                if isinstance(arg, dict):
                    arg_name = arg.get('name', 'arg')
                    arg_type = arg.get('type', 'string')
                    arg_default = arg.get('default', '')
                    
                    if arg_type == 'integer':
                        widget = QSpinBox()
                        widget.setValue(int(arg_default) if arg_default else 0)
                    elif arg_type == 'float':
                        widget = QDoubleSpinBox()
                        widget.setValue(float(arg_default) if arg_default else 0.0)
                    else:
                        widget = QLineEdit()
                        widget.setText(str(arg_default))
                        widget.setPlaceholderText(arg.get('description', ''))
                    
                    self.arg_inputs[arg_name] = widget
                    form_layout.addRow(arg_name, widget)
        else:
            form_layout.addRow(QLabel("No arguments required"))
        
        layout.addLayout(form_layout)
        
        # Output area
        output_label = QLabel("Output:")
        output_font = QFont()
        output_font.setBold(True)
        output_label.setFont(output_font)
        layout.addWidget(output_label)
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setMinimumHeight(150)
        self.output_text.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #00ff00;
                font-family: Courier New;
                font-size: 10pt;
            }
        """)
        layout.addWidget(self.output_text)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.run_button = QPushButton("▶ Execute Skill")
        self.run_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.run_button.clicked.connect(self.execute_skill)
        button_layout.addWidget(self.run_button)
        
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def execute_skill(self):
        """Execute the skill with provided arguments."""
        args = [str(widget.text() if hasattr(widget, 'text') else widget.value()) 
                for widget in self.arg_inputs.values()]
        
        self.output_text.clear()
        self.output_text.setText("🚀 Executing skill...\n")
        self.run_button.setEnabled(False)
        
        self.executor_thread = SkillExecutorThread(self.skill_name, args)
        self.executor_thread.output_signal.connect(self.on_output)
        self.executor_thread.error_signal.connect(self.on_error)
        self.executor_thread.finished_signal.connect(self.on_finished)
        self.executor_thread.start()
    
    def on_output(self, message: str):
        """Handle output from skill execution."""
        self.output_text.append(message)
    
    def on_error(self, message: str):
        """Handle error from skill execution."""
        self.output_text.append(f"\n{message}")
    
    def on_finished(self):
        """Handle skill execution completion."""
        self.run_button.setEnabled(True)


class ASKDesktopGUI(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🤖 Agent-Skill-Kit - Desktop")
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet(self.get_stylesheet())
        
        # Try to find skills with explicit path resolution
        skills_dir = None
        
        # First try: site-packages installation
        site_skills = Path(__file__).parent.parent / "skills"
        if site_skills.exists():
            skills_dir = site_skills
        # Second try: Development/local installation
        else:
            local_skills = Path(__file__).resolve().parent.parent / "skills"
            if local_skills.exists():
                skills_dir = local_skills
        
        self.manager = SkillManager(str(skills_dir) if skills_dir else None)
        self.execution_history = []
        
        # Debug: Check if skills are loaded
        if not self.manager.skills:
            print(f"Warning: No skills found! Skills dir: {self.manager.skills_dir}")
            print(f"Skills dir exists: {self.manager.skills_dir.exists()}")
        else:
            print(f"✓ Loaded {len(self.manager.skills)} skills from {self.manager.skills_dir}")
        
        self.init_ui()
        self.load_skills()
    
    def init_ui(self):
        """Initialize the main UI."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QHBoxLayout()
        
        # Left sidebar - Skill list
        left_layout = QVBoxLayout()
        
        search_label = QLabel("🔍 Search Skills:")
        search_label_font = QFont()
        search_label_font.setBold(True)
        search_label.setFont(search_label_font)
        left_layout.addWidget(search_label)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Type to filter skills...")
        self.search_input.textChanged.connect(self.filter_skills)
        left_layout.addWidget(self.search_input)
        
        self.skills_list = QListWidget()
        self.skills_list.itemSelectionChanged.connect(self.on_skill_selected)
        left_layout.addWidget(self.skills_list)
        
        left_panel = QWidget()
        left_panel.setLayout(left_layout)
        left_panel.setMaximumWidth(300)
        
        # Right side - Tabs for detail/history
        self.tabs = QTabWidget()
        
        # Detail tab
        detail_widget = QWidget()
        detail_layout = QVBoxLayout()
        
        self.detail_text = QTextEdit()
        self.detail_text.setReadOnly(True)
        detail_layout.addWidget(self.detail_text)
        
        self.run_button = QPushButton("▶ Run Selected Skill")
        self.run_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        self.run_button.clicked.connect(self.run_selected_skill)
        detail_layout.addWidget(self.run_button)
        
        detail_widget.setLayout(detail_layout)
        self.tabs.addTab(detail_widget, "📋 Details")
        
        # History tab
        history_widget = QWidget()
        history_layout = QVBoxLayout()
        
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(4)
        self.history_table.setHorizontalHeaderLabels(["Skill", "Arguments", "Status", "Time"])
        self.history_table.horizontalHeader().setStretchLastSection(False)
        history_layout.addWidget(self.history_table)
        
        clear_history_btn = QPushButton("Clear History")
        clear_history_btn.clicked.connect(self.clear_history)
        history_layout.addWidget(clear_history_btn)
        
        history_widget.setLayout(history_layout)
        self.tabs.addTab(history_widget, "⏱️ History")
        
        # Dashboard tab
        dashboard_widget = QWidget()
        dashboard_layout = QVBoxLayout()
        
        self.stats_label = QLabel()
        self.stats_label.setFont(QFont("Arial", 11))
        dashboard_layout.addWidget(self.stats_label)
        
        dashboard_widget.setLayout(dashboard_layout)
        self.tabs.addTab(dashboard_widget, "📊 Dashboard")
        
        # Splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(self.tabs)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        
        layout.addWidget(splitter)
        central_widget.setLayout(layout)
        
        # Status bar
        self.statusBar().showMessage("Ready")
    
    def load_skills(self):
        """Load and display available skills."""
        self.skills_list.clear()
        
        try:
            skills = self.manager.skills
            if not skills:
                self.detail_text.setText("""
                <h2>⚠️ No Skills Found</h2>
                <p>The skills directory appears to be empty or not accessible.</p>
                <p><b>Skills Directory:</b> {}</p>
                <p>Please ensure ASK is properly installed.</p>
                <p>Try running: <code>ask dashboard</code> to verify.</p>
                """.format(self.manager.skills_dir))
                self.statusBar().showMessage("No skills found - check installation")
                return
            
            for skill_name in sorted(skills.keys()):
                item = QListWidgetItem(skill_name)
                item.setData(Qt.ItemDataRole.UserRole, skill_name)
                self.skills_list.addItem(item)
            
            # Auto-select first skill
            if self.skills_list.count() > 0:
                self.skills_list.setCurrentRow(0)
                self.on_skill_selected()
            
            self.statusBar().showMessage(f"Loaded {len(skills)} skills")
            self.update_stats()
        
        except Exception as e:
            error_msg = f"Error loading skills: {str(e)}"
            print(f"ERROR: {error_msg}")
            self.detail_text.setText(f"""
            <h2>❌ Error Loading Skills</h2>
            <p>{error_msg}</p>
            """)
            self.statusBar().showMessage(f"Error: {str(e)}")
    
    def filter_skills(self, text: str):
        """Filter skills based on search text."""
        for i in range(self.skills_list.count()):
            item = self.skills_list.item(i)
            item.setHidden(text.lower() not in item.text().lower())
    
    def on_skill_selected(self):
        """Handle skill selection."""
        selected = self.skills_list.selectedItems()
        if not selected:
            return
        
        skill_name = selected[0].text()
        skill_data = self.manager.skills.get(skill_name)
        
        if skill_data:
            manifest = skill_data['manifest']
            detail_html = f"""
            <h2>{manifest.get('name', skill_name)}</h2>
            <p><b>Version:</b> {manifest.get('version', '?')}</p>
            <p><b>Description:</b></p>
            <p>{manifest.get('description', 'No description')}</p>
            <p><b>API Keys Required:</b> {'Yes ❌' if manifest.get('api_keys_required') else 'No ✅'}</p>
            <p><b>Category:</b> {manifest.get('category', 'General')}</p>
            """
            
            if manifest.get('arguments'):
                detail_html += "<p><b>Arguments:</b></p><ul>"
                for arg in manifest.get('arguments', []):
                    if isinstance(arg, dict):
                        detail_html += f"<li>{arg.get('name', 'arg')} ({arg.get('type', 'string')})</li>"
                detail_html += "</ul>"
            
            self.detail_text.setHtml(detail_html)
            self.statusBar().showMessage(f"Selected: {skill_name}")
    
    def run_selected_skill(self):
        """Run the selected skill."""
        selected = self.skills_list.selectedItems()
        if not selected:
            QMessageBox.warning(self, "No Selection", "Please select a skill first")
            return
        
        skill_name = selected[0].text()
        skill_data = self.manager.skills.get(skill_name)
        
        if skill_data:
            dialog = SkillDetailDialog(skill_name, skill_data, self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                # Add to history
                self.add_to_history(skill_name, "Success")
    
    def add_to_history(self, skill_name: str, status: str):
        """Add execution to history."""
        row = self.history_table.rowCount()
        self.history_table.insertRow(row)
        
        self.history_table.setItem(row, 0, QTableWidgetItem(skill_name))
        self.history_table.setItem(row, 1, QTableWidgetItem(""))
        self.history_table.setItem(row, 2, QTableWidgetItem(status))
        self.history_table.setItem(row, 3, QTableWidgetItem(datetime.now().strftime("%H:%M:%S")))
    
    def clear_history(self):
        """Clear execution history."""
        self.history_table.setRowCount(0)
    
    def update_stats(self):
        """Update dashboard statistics."""
        total_skills = len(self.manager.skills)
        no_key_skills = sum(1 for s in self.manager.skills.values() 
                          if not s['manifest'].get('api_keys_required', False))
        
        stats_text = f"""
        <h2>🎯 Dashboard</h2>
        <p><b>Total Skills Available:</b> {total_skills}</p>
        <p><b>Free Skills (No API Keys):</b> {no_key_skills}</p>
        <p><b>Skill Categories:</b></p>
        <ul>
        """
        
        categories = set()
        for skill in self.manager.skills.values():
            category = skill['manifest'].get('category', 'Other')
            categories.add(category)
        
        for cat in sorted(categories):
            stats_text += f"<li>{cat}</li>"
        
        stats_text += "</ul>"
        
        self.stats_label.setText(stats_text)
    
    @staticmethod
    def get_stylesheet() -> str:
        """Return the application stylesheet."""
        return """
        QMainWindow {
            background-color: #f5f5f5;
        }
        
        QLabel {
            color: #333333;
        }
        
        QLineEdit {
            padding: 5px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            background-color: white;
        }
        
        QListWidget {
            border: 1px solid #cccccc;
            border-radius: 4px;
            background-color: white;
        }
        
        QListWidget::item:selected {
            background-color: #2196F3;
            color: white;
        }
        
        QTextEdit {
            border: 1px solid #cccccc;
            border-radius: 4px;
            background-color: white;
            padding: 5px;
        }
        
        QPushButton {
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
            border: none;
        }
        
        QTabWidget::pane {
            border: 1px solid #cccccc;
        }
        
        QTabBar::tab {
            background-color: #e0e0e0;
            padding: 5px 15px;
            margin-right: 2px;
        }
        
        QTabBar::tab:selected {
            background-color: white;
            border-bottom: 2px solid #2196F3;
        }
        """


def main():
    """Main entry point for the GUI."""
    app = QApplication(sys.argv)
    app.setApplicationName("Agent-Skill-Kit Desktop")
    app.setApplicationVersion("2.0.0")
    
    window = ASKDesktopGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
