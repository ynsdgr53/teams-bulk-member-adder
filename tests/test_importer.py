"""
Unit tests for MemberDataImporter.
Uses 100% fictitious, synthetic mock data with RFC 2606 reserved example domains.
"""

import os
import unittest
import tempfile
import csv

from src.importer import MemberDataImporter

class TestMemberDataImporter(unittest.TestCase):
    def setUp(self):
        self.importer = MemberDataImporter()

    def test_english_import_and_detection(self):
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Student ID", "First Name", "Last Name", "Grade", "Email Address"])
            writer.writerow(["100000000001", "John", "Doe", "A", "john.doe@example.edu"])
            writer.writerow(["100000000002", "Alice", "Smith", "B", "alice.smith@example.edu"])
            filepath = f.name

        try:
            rows = self.importer.load_rows(filepath)
            self.assertEqual(len(rows), 3)

            email_idx, id_idx, name_idx, surname_idx = self.importer.detect_columns()
            self.assertEqual(email_idx, 4)
            self.assertEqual(id_idx, 0)
            self.assertEqual(name_idx, 1)
            self.assertEqual(surname_idx, 2)

            members = self.importer.parse_members(email_idx, id_idx, name_idx, surname_idx)
            self.assertEqual(len(members), 2)
            self.assertEqual(members[0]["id"], "100000000001")
            self.assertEqual(members[0]["name"], "John Doe")
            self.assertEqual(members[0]["email"], "john.doe@example.edu")
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

    def test_obs_turkish_format(self):
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["renci No_Code", "Ad_Code", "Soyad_Code", "Snf_Code", "A.Tipi_Code", "Not_Code", "Faklte_Code", "Program_Code", "e-posta_Code"])
            writer.writerow(["100000000003", "Ahmet", "Yılmaz", "4", "Zorunlu", "", "Mühendislik", "Bilgisayar Müh", "ahmet.yilmaz@example.edu.tr"])
            filepath = f.name

        try:
            self.importer.load_rows(filepath)
            email_idx, id_idx, name_idx, surname_idx = self.importer.detect_columns()
            self.assertEqual(email_idx, 8)
            # Crucial: ID column must be 0, NOT 5 (Not)
            self.assertEqual(id_idx, 0)
            self.assertEqual(name_idx, 1)
            self.assertEqual(surname_idx, 2)
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

    def test_spanish_format(self):
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Matrícula", "Nombre", "Apellido", "Nota", "Correo Electrónico"])
            writer.writerow(["ESP123456", "Carlos", "Garcia", "9.5", "carlos.garcia@example.es"])
            filepath = f.name

        try:
            self.importer.load_rows(filepath)
            email_idx, id_idx, name_idx, surname_idx = self.importer.detect_columns()
            self.assertEqual(email_idx, 4)
            self.assertEqual(id_idx, 0)
            self.assertEqual(name_idx, 1)
            self.assertEqual(surname_idx, 2)
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

    def test_german_format(self):
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Matrikelnummer", "Vorname", "Nachname", "Note", "E-Mail-Adresse"])
            writer.writerow(["DE123456", "Max", "Mustermann", "1.3", "max.mustermann@example.de"])
            filepath = f.name

        try:
            self.importer.load_rows(filepath)
            email_idx, id_idx, name_idx, surname_idx = self.importer.detect_columns()
            self.assertEqual(email_idx, 4)
            self.assertEqual(id_idx, 0)
            self.assertEqual(name_idx, 1)
            self.assertEqual(surname_idx, 2)
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

if __name__ == "__main__":
    unittest.main()
