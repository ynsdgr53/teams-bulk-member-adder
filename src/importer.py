"""
Data Importer Module
Handles loading Excel (.xlsx, .xls) and CSV files, and performs smart column detection.
"""

import os
import csv
import openpyxl

class MemberDataImporter:
    def __init__(self):
        self.current_filepath = None
        self.sheets = []
        self.raw_rows = []
        
    def get_sheets(self, filepath):
        """Returns the list of sheets for a given file."""
        self.current_filepath = filepath
        if filepath.lower().endswith(".csv"):
            self.sheets = ["Default"]
            return self.sheets
            
        try:
            wb = openpyxl.load_workbook(filepath, read_only=True, data_only=True)
            self.sheets = wb.sheetnames
            wb.close()
            return self.sheets
        except Exception as e:
            raise RuntimeError(f"Failed to read sheets: {e}")

    def load_rows(self, filepath, sheet_name=None):
        """Loads non-empty rows from the given file and sheet."""
        self.current_filepath = filepath
        rows = []
        
        if filepath.lower().endswith(".csv"):
            for enc in ["utf-8-sig", "utf-8", "windows-1254", "iso-8859-9", "latin-1"]:
                try:
                    with open(filepath, "r", encoding=enc) as f:
                        reader = csv.reader(f)
                        rows = list(reader)
                    break
                except Exception:
                    continue
        else:
            wb = openpyxl.load_workbook(filepath, data_only=True)
            target_sheet = sheet_name if sheet_name and sheet_name in wb.sheetnames else wb.sheetnames[0]
            ws = wb[target_sheet]
            rows = list(ws.iter_rows(values_only=True))
            wb.close()

        # Clean empty rows
        cleaned = []
        for r in rows:
            if any(cell is not None and str(cell).strip() != "" for cell in r):
                cleaned.append([str(c).strip() if c is not None else "" for c in r])
                
        self.raw_rows = cleaned
        return self.raw_rows

    def detect_columns(self):
        """
        Intelligently identifies the indices for:
        (email_idx, id_idx, name_idx, surname_idx)
        Works internationally across EN, TR, ES, FR, DE headers and data patterns.
        """
        if not self.raw_rows:
            return None, None, None, None

        first_row = self.raw_rows[0]
        max_cols = max(len(r) for r in self.raw_rows[:10])

        email_idx = None
        id_idx = None
        name_idx = None
        surname_idx = None

        # 1. Header Text Inspection (Multi-lingual)
        for i, h in enumerate(first_row):
            h_str = str(h).lower().strip()

            # Email keywords (EN, TR, ES, FR, DE)
            if any(k in h_str for k in ["email", "e-mail", "posta", "mail", "correo", "courriel"]):
                email_idx = i

            # ID keywords (Exclude "not", "grade", "note", "nota" to avoid matching grade columns)
            is_grade_col = any(g in h_str for g in ["not", "grade", "note", "nota", "fak", "prog", "dept"])
            if not is_grade_col:
                if any(k in h_str for k in [
                    "renci no", "ogrenci no", "öğrenci no", "student id", "student no", 
                    "member id", "matricule", "matrícula", "matrikel", "roll no", "ogr no"
                ]):
                    id_idx = i
                elif id_idx is None and (h_str == "no" or h_str.startswith("no_") or h_str.startswith("no ") or h_str.endswith("_no") or h_str == "id"):
                    id_idx = i

            # Surname
            if any(k in h_str for k in ["surname", "last name", "soyad", "apellido", "nachname"]):
                surname_idx = i
            # First Name / Full Name
            else:
                is_email_like = any(m in h_str for m in ["email", "mail", "posta", "correo", "courriel"])
                if not is_email_like:
                    is_tr_ad = h_str in ["ad", "adı", "isim"] or h_str.startswith("ad_") or h_str.startswith("ad ") or h_str.endswith("_ad")
                    is_intl_name = any(k in h_str for k in ["name", "first name", "full name", "nombre", "prénom", "vorname"])
                    if is_tr_ad or is_intl_name:
                        name_idx = i

        # 2. Cell Content Fallback
        sample_rows = self.raw_rows[1:15]

        # ID fallback: Look for columns with numbers length >= 6 (typical student/employee IDs)
        if id_idx is None:
            for col_i in range(max_cols):
                if col_i == email_idx:
                    continue
                num_count = sum(1 for r in sample_rows if len(r) > col_i and str(r[col_i]).strip().isdigit() and len(str(r[col_i]).strip()) >= 6)
                if num_count >= 3:
                    id_idx = col_i
                    break

        # Email fallback: Look for columns containing '@' and '.'
        if email_idx is None:
            for col_i in range(max_cols):
                if any(len(r) > col_i and "@" in str(r[col_i]) and "." in str(r[col_i]) for r in sample_rows):
                    email_idx = col_i
                    break

        return email_idx, id_idx, name_idx, surname_idx

    def parse_members(self, email_col, id_col=None, name_col=None, surname_col=None):
        """Extracts cleaned member dictionaries with {'id': ..., 'name': ..., 'email': ...}."""
        if email_col is None or not self.raw_rows:
            return []

        start_row = 1 if "@" not in self.raw_rows[0][email_col] else 0
        members = []

        for r in self.raw_rows[start_row:]:
            if len(r) <= email_col:
                continue
            email = r[email_col].strip()
            if not email or "@" not in email:
                continue

            member_id = r[id_col].strip() if id_col is not None and len(r) > id_col else ""
            
            name = r[name_col].strip() if name_col is not None and len(r) > name_col else ""
            if surname_col is not None and len(r) > surname_col:
                surname = r[surname_col].strip()
                if surname and surname not in name:
                    name = f"{name} {surname}".strip()

            members.append({
                "id": member_id,
                "name": name,
                "email": email
            })

        return members
