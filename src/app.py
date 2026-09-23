"""
Main User Interface Application
Built with CustomTkinter, supporting dynamic multi-language localization (EN, TR, ES, FR, DE).
"""

import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import customtkinter as ctk

from .i18n import i18n, LANGUAGES
from .importer import MemberDataImporter
from .automator import TeamsAutomator

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TeamsMemberAdderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.importer = MemberDataImporter()
        self.automator = TeamsAutomator()
        self.parsed_members = []
        self.surname_idx = None

        self.title(i18n.get("app_title"))
        self.geometry("900x720")
        self.minsize(740, 540)

        self.setup_ui()
        self.apply_table_theme("Dark")
        self.retranslate_ui()

    def setup_ui(self):
        # 1. FIXED BOTTOM PANEL (Sticky bottom: Buttons never vanish on resize)
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.pack(side="bottom", fill="x", padx=14, pady=(2, 6))

        self.lbl_footer = ctk.CTkLabel(
            self.footer_frame,
            text=i18n.get("footer_text"),
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=("gray50", "gray60")
        )
        self.lbl_footer.pack(side="left")

        self.ctrl_card = ctk.CTkFrame(self, corner_radius=10, fg_color=("gray85", "#1F202B"))
        self.ctrl_card.pack(side="bottom", fill="x", padx=14, pady=(4, 6))

        # Quick Step Guidance Banner
        self.step_banner = ctk.CTkFrame(self.ctrl_card, fg_color=("gray75", "#292A38"), corner_radius=6)
        self.step_banner.pack(fill="x", padx=12, pady=(8, 4))

        self.lbl_step_hint = ctk.CTkLabel(
            self.step_banner,
            text=i18n.get("step_hint"),
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color=("#1E40AF", "#93C5FD")
        )
        self.lbl_step_hint.pack(pady=4)

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self.ctrl_card, height=8, corner_radius=4)
        self.progress_bar.set(0)
        self.progress_bar.pack(fill="x", padx=12, pady=(4, 3))

        # Status text
        status_box = ctk.CTkFrame(self.ctrl_card, fg_color="transparent")
        status_box.pack(fill="x", padx=12, pady=(1, 4))

        self.lbl_status = ctk.CTkLabel(
            status_box,
            text=i18n.get("status_ready"),
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold")
        )
        self.lbl_status.pack(side="left")

        # Action Buttons
        btn_box = ctk.CTkFrame(self.ctrl_card, fg_color="transparent")
        btn_box.pack(fill="x", padx=12, pady=(2, 8))

        self.btn_test = ctk.CTkButton(
            btn_box,
            text=i18n.get("btn_test"),
            width=150,
            height=34,
            fg_color="#D97706",
            hover_color="#B45309",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            command=lambda: self.start_addition(limit=2)
        )
        self.btn_test.pack(side="left", padx=(0, 8))

        self.btn_all = ctk.CTkButton(
            btn_box,
            text=i18n.get("btn_add_all"),
            width=240,
            height=34,
            fg_color="#5B5FC7",
            hover_color="#4F52B2",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            command=lambda: self.start_addition(limit=None)
        )
        self.btn_all.pack(side="left", padx=(0, 8))

        self.btn_stop = ctk.CTkButton(
            btn_box,
            text=i18n.get("btn_stop"),
            width=90,
            height=34,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            state="disabled",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            command=self.stop_addition
        )
        self.btn_stop.pack(side="right")

        # 2. TOP HEADER
        self.header_card = ctk.CTkFrame(self, corner_radius=10, fg_color=("gray90", "#1E1F29"))
        self.header_card.pack(side="top", fill="x", padx=14, pady=(8, 4))

        title_box = ctk.CTkFrame(self.header_card, fg_color="transparent")
        title_box.pack(side="left", padx=14, pady=6)

        self.lbl_title = ctk.CTkLabel(
            title_box,
            text=i18n.get("app_title"),
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold")
        )
        self.lbl_title.pack(anchor="w")

        self.lbl_subtitle = ctk.CTkLabel(
            title_box,
            text=i18n.get("app_subtitle"),
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=("gray40", "gray70")
        )
        self.lbl_subtitle.pack(anchor="w")

        # Right Header: Language selector + Help/About + Theme
        top_right_box = ctk.CTkFrame(self.header_card, fg_color="transparent")
        top_right_box.pack(side="right", padx=14, pady=6)

        btn_row = ctk.CTkFrame(top_right_box, fg_color="transparent")
        btn_row.pack(side="top", pady=(0, 4))

        # Language dropdown
        self.combo_lang = ctk.CTkComboBox(
            btn_row,
            values=list(LANGUAGES.values()),
            width=110,
            height=28,
            font=ctk.CTkFont(size=11),
            command=self.on_language_change
        )
        self.combo_lang.set(LANGUAGES[i18n.current_lang])
        self.combo_lang.pack(side="left", padx=(0, 6))

        self.btn_how_to = ctk.CTkButton(
            btn_row,
            text=i18n.get("how_to_use_btn"),
            width=110,
            height=28,
            fg_color="#0284C7",
            hover_color="#0369A1",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            command=self.show_how_to_use
        )
        self.btn_how_to.pack(side="left", padx=(0, 6))

        self.btn_about = ctk.CTkButton(
            btn_row,
            text=i18n.get("about_btn"),
            width=80,
            height=28,
            fg_color="#8B5CF6",
            hover_color="#7C3AED",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            command=self.show_about
        )
        self.btn_about.pack(side="left")

        self.theme_switch = ctk.CTkSwitch(
            top_right_box,
            text=i18n.get("dark_mode"),
            command=self.toggle_theme,
            font=ctk.CTkFont(family="Segoe UI", size=11)
        )
        self.theme_switch.select()
        self.theme_switch.pack(side="top", anchor="e")

        # 3. SECTION 1: FILE SELECTION
        self.file_card = ctk.CTkFrame(self, corner_radius=10)
        self.file_card.pack(side="top", fill="x", padx=14, pady=3)

        f_row = ctk.CTkFrame(self.file_card, fg_color="transparent")
        f_row.pack(fill="x", padx=12, pady=(6, 2))

        self.lbl_sec_file = ctk.CTkLabel(f_row, text=i18n.get("sec_file"), font=ctk.CTkFont(size=12, weight="bold"))
        self.lbl_sec_file.pack(side="left", padx=(0, 6))

        self.entry_file = ctk.CTkEntry(
            f_row,
            placeholder_text=i18n.get("file_placeholder"),
            height=30,
            font=ctk.CTkFont(family="Segoe UI", size=11)
        )
        self.entry_file.pack(side="left", fill="x", expand=True, padx=(0, 6))

        self.btn_browse = ctk.CTkButton(
            f_row,
            text=i18n.get("btn_browse"),
            width=95,
            height=30,
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            command=self.browse_file
        )
        self.btn_browse.pack(side="right")

        f_sub_row = ctk.CTkFrame(self.file_card, fg_color="transparent")
        f_sub_row.pack(fill="x", padx=12, pady=(2, 6))

        self.lbl_sheet_title = ctk.CTkLabel(f_sub_row, text=i18n.get("lbl_sheet"), font=ctk.CTkFont(size=11))
        self.lbl_sheet_title.pack(side="left", padx=(0, 4))

        self.combo_sheet = ctk.CTkComboBox(
            f_sub_row,
            values=["(No file)"],
            width=160,
            height=26,
            command=self.on_sheet_change
        )
        self.combo_sheet.pack(side="left", padx=(0, 12))

        self.lbl_file_info = ctk.CTkLabel(
            f_sub_row,
            text=i18n.get("file_not_selected"),
            text_color=("gray40", "gray70"),
            font=ctk.CTkFont(size=11)
        )
        self.lbl_file_info.pack(side="left")

        # 4. SECTION 2: COLUMN MAPPING
        self.col_card = ctk.CTkFrame(self, corner_radius=10)
        self.col_card.pack(side="top", fill="x", padx=14, pady=3)

        c_grid = ctk.CTkFrame(self.col_card, fg_color="transparent")
        c_grid.pack(fill="x", padx=12, pady=6)

        # Email
        self.lbl_col_email = ctk.CTkLabel(c_grid, text=i18n.get("lbl_email"), font=ctk.CTkFont(size=11, weight="bold"))
        self.lbl_col_email.grid(row=0, column=0, sticky="w", padx=4, pady=2)
        self.combo_email = ctk.CTkComboBox(c_grid, values=["(Empty)"], width=210, height=26, command=self.on_column_change)
        self.combo_email.grid(row=0, column=1, sticky="w", padx=4, pady=2)

        # ID
        self.lbl_col_id = ctk.CTkLabel(c_grid, text=i18n.get("lbl_id"), font=ctk.CTkFont(size=11))
        self.lbl_col_id.grid(row=0, column=2, sticky="w", padx=(14, 4), pady=2)
        self.combo_no = ctk.CTkComboBox(c_grid, values=["(None)"], width=210, height=26, command=self.on_column_change)
        self.combo_no.grid(row=0, column=3, sticky="w", padx=4, pady=2)

        # Name
        self.lbl_col_name = ctk.CTkLabel(c_grid, text=i18n.get("lbl_name"), font=ctk.CTkFont(size=11))
        self.lbl_col_name.grid(row=1, column=0, sticky="w", padx=4, pady=2)
        self.combo_name = ctk.CTkComboBox(c_grid, values=["(None)"], width=210, height=26, command=self.on_column_change)
        self.combo_name.grid(row=1, column=1, sticky="w", padx=4, pady=2)

        # Delay
        self.lbl_col_delay = ctk.CTkLabel(c_grid, text=i18n.get("lbl_delay"), font=ctk.CTkFont(size=11))
        self.lbl_col_delay.grid(row=1, column=2, sticky="w", padx=(14, 4), pady=2)
        delay_box = ctk.CTkFrame(c_grid, fg_color="transparent")
        delay_box.grid(row=1, column=3, sticky="w", padx=4, pady=2)

        self.spin_delay = ctk.CTkComboBox(delay_box, values=["1.0", "1.2", "1.5", "1.8", "2.0", "2.5"], width=70, height=26)
        self.spin_delay.set("1.5")
        self.spin_delay.pack(side="left")
        self.lbl_delay_unit = ctk.CTkLabel(delay_box, text=f" {i18n.get('lbl_delay_unit')}", font=ctk.CTkFont(size=11), text_color="gray")
        self.lbl_delay_unit.pack(side="left", padx=4)

        # 5. SECTION 3: PREVIEW TABLE (Expandable center area)
        self.preview_card = ctk.CTkFrame(self, corner_radius=10)
        self.preview_card.pack(side="top", fill="both", expand=True, padx=14, pady=3)

        p_header = ctk.CTkFrame(self.preview_card, fg_color="transparent")
        p_header.pack(fill="x", padx=12, pady=(6, 2))

        self.lbl_table_count = ctk.CTkLabel(
            p_header,
            text=i18n.get("sec_preview", count=0),
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold")
        )
        self.lbl_table_count.pack(side="left")

        self.btn_exp_csv = ctk.CTkButton(
            p_header,
            text=i18n.get("btn_export_csv"),
            width=90,
            height=24,
            fg_color="gray40",
            hover_color="gray30",
            font=ctk.CTkFont(size=10),
            command=self.export_csv
        )
        self.btn_exp_csv.pack(side="right", padx=2)

        self.btn_exp_txt = ctk.CTkButton(
            p_header,
            text=i18n.get("btn_export_txt"),
            width=100,
            height=24,
            fg_color="gray40",
            hover_color="gray30",
            font=ctk.CTkFont(size=10),
            command=self.export_txt
        )
        self.btn_exp_txt.pack(side="right", padx=2)

        # Treeview
        table_container = ctk.CTkFrame(self.preview_card, fg_color="transparent")
        table_container.pack(fill="both", expand=True, padx=10, pady=(0, 6))

        self.table_style = ttk.Style()
        self.table_style.theme_use("clam")

        self.tree = ttk.Treeview(
            table_container,
            columns=("id", "name", "email"),
            show="headings",
            selectmode="browse"
        )
        self.tree.heading("id", text=i18n.get("col_header_id"))
        self.tree.heading("name", text=i18n.get("col_header_name"))
        self.tree.heading("email", text=i18n.get("col_header_email"))

        self.tree.column("id", width=140, anchor="center")
        self.tree.column("name", width=220, anchor="w")
        self.tree.column("email", width=340, anchor="w")

        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def on_language_change(self, choice):
        for code, name in LANGUAGES.items():
            if name == choice:
                i18n.set_language(code)
                break
        self.retranslate_ui()

    def retranslate_ui(self):
        """Updates text of all widgets to current language."""
        self.title(i18n.get("app_title"))
        self.lbl_title.configure(text=i18n.get("app_title"))
        self.lbl_subtitle.configure(text=i18n.get("app_subtitle"))
        self.theme_switch.configure(text=i18n.get("dark_mode"))
        self.btn_how_to.configure(text=i18n.get("how_to_use_btn"))
        self.btn_about.configure(text=i18n.get("about_btn"))

        self.lbl_sec_file.configure(text=i18n.get("sec_file"))
        self.entry_file.configure(placeholder_text=i18n.get("file_placeholder"))
        self.btn_browse.configure(text=i18n.get("btn_browse"))
        self.lbl_sheet_title.configure(text=i18n.get("lbl_sheet"))

        self.lbl_col_email.configure(text=i18n.get("lbl_email"))
        self.lbl_col_id.configure(text=i18n.get("lbl_id"))
        self.lbl_col_name.configure(text=i18n.get("lbl_name"))
        self.lbl_col_delay.configure(text=i18n.get("lbl_delay"))
        self.lbl_delay_unit.configure(text=f" {i18n.get('lbl_delay_unit')}")

        self.lbl_table_count.configure(text=i18n.get("sec_preview", count=len(self.parsed_members)))
        self.btn_exp_csv.configure(text=i18n.get("btn_export_csv"))
        self.btn_exp_txt.configure(text=i18n.get("btn_export_txt"))

        self.tree.heading("id", text=i18n.get("col_header_id"))
        self.tree.heading("name", text=i18n.get("col_header_name"))
        self.tree.heading("email", text=i18n.get("col_header_email"))

        self.lbl_step_hint.configure(text=i18n.get("step_hint"))
        self.btn_test.configure(text=i18n.get("btn_test"))
        self.btn_all.configure(text=i18n.get("btn_add_all"))
        self.btn_stop.configure(text=i18n.get("btn_stop"))
        self.lbl_footer.configure(text=i18n.get("footer_text"))

        if not self.automator.is_running:
            self.lbl_status.configure(text=i18n.get("status_ready"))

    def apply_table_theme(self, mode):
        """Theme ttk.Treeview cleanly for both Light and Dark mode."""
        if mode == "Dark":
            self.table_style.configure(
                "Treeview",
                background="#23242E",
                foreground="#E0E0E0",
                fieldbackground="#23242E",
                rowheight=25,
                font=("Segoe UI", 9)
            )
            self.table_style.configure(
                "Treeview.Heading",
                background="#323344",
                foreground="#FFFFFF",
                font=("Segoe UI", 9, "bold")
            )
            self.table_style.map("Treeview", background=[("selected", "#5B5FC7")], foreground=[("selected", "#FFFFFF")])
        else:
            self.table_style.configure(
                "Treeview",
                background="#FFFFFF",
                foreground="#1F2937",
                fieldbackground="#FFFFFF",
                rowheight=25,
                font=("Segoe UI", 9)
            )
            self.table_style.configure(
                "Treeview.Heading",
                background="#E5E7EB",
                foreground="#111827",
                font=("Segoe UI", 9, "bold")
            )
            self.table_style.map("Treeview", background=[("selected", "#5B5FC7")], foreground=[("selected", "#FFFFFF")])

    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("Dark")
            self.apply_table_theme("Dark")
        else:
            ctk.set_appearance_mode("Light")
            self.apply_table_theme("Light")

    def browse_file(self):
        filetypes = [
            ("Supported Files (*.xlsx, *.xls, *.csv)", "*.xlsx *.xls *.csv"),
            ("Excel Workbook (*.xlsx)", "*.xlsx"),
            ("Legacy Excel (*.xls)", "*.xls"),
            ("CSV Document (*.csv)", "*.csv"),
            ("All Files", "*.*")
        ]
        fp = filedialog.askopenfilename(title="Select Member List File", filetypes=filetypes)
        if fp:
            self.load_file(fp)

    def load_file(self, filepath):
        self.entry_file.delete(0, "end")
        self.entry_file.insert(0, filepath)

        try:
            sheets = self.importer.get_sheets(filepath)
            self.combo_sheet.configure(values=sheets)
            self.combo_sheet.set(sheets[0])
            self.load_sheet_data(sheets[0])
            self.lbl_file_info.configure(
                text=i18n.get("file_loaded", filename=os.path.basename(filepath)),
                text_color="#10B981"
            )
        except Exception as e:
            messagebox.showerror("Error", i18n.get("file_error", error=str(e)))

    def on_sheet_change(self, choice):
        self.load_sheet_data(choice)

    def load_sheet_data(self, sheet_name):
        try:
            rows = self.importer.load_rows(self.entry_file.get(), sheet_name)
            if not rows:
                messagebox.showwarning("Warning", i18n.get("file_empty_sheet"))
                return

            email_idx, id_idx, name_idx, surname_idx = self.importer.detect_columns()
            self.surname_idx = surname_idx

            first_row = rows[0]
            max_cols = max(len(r) for r in rows[:10])
            options = []
            for i in range(max_cols):
                val = first_row[i] if i < len(first_row) else ""
                options.append(f"{i+1}: {val}" if val else f"{i+1}: (Empty)")

            empty_opt = i18n.get("col_empty")
            self.combo_email.configure(values=options)
            self.combo_no.configure(values=[empty_opt] + options)
            self.combo_name.configure(values=[empty_opt] + options)

            # Assign detected defaults
            if email_idx is not None and email_idx < len(options):
                self.combo_email.set(options[email_idx])
            elif options:
                self.combo_email.set(options[0])

            if id_idx is not None and id_idx < len(options):
                self.combo_no.set(options[id_idx])
            else:
                self.combo_no.set(empty_opt)

            if name_idx is not None and name_idx < len(options):
                self.combo_name.set(options[name_idx])
            else:
                self.combo_name.set(empty_opt)

            self.refresh_table()

        except Exception as e:
            messagebox.showerror("Error", i18n.get("file_error", error=str(e)))

    def on_column_change(self, choice):
        self.refresh_table()

    def get_selected_col_index(self, combo):
        val = combo.get()
        if not val or ":" not in val:
            return None
        try:
            return int(val.split(":")[0]) - 1
        except Exception:
            return None

    def refresh_table(self):
        email_col = self.get_selected_col_index(self.combo_email)
        id_col = self.get_selected_col_index(self.combo_no)
        name_col = self.get_selected_col_index(self.combo_name)

        for item in self.tree.get_children():
            self.tree.delete(item)

        self.parsed_members = self.importer.parse_members(email_col, id_col, name_col, self.surname_idx)
        for m in self.parsed_members:
            self.tree.insert("", "end", values=(m["id"], m["name"], m["email"]))

        total = len(self.parsed_members)
        self.lbl_table_count.configure(text=i18n.get("sec_preview", count=total))
        self.lbl_status.configure(text=i18n.get("status_ready"))

    def export_txt(self):
        if not self.parsed_members:
            messagebox.showwarning("Warning", i18n.get("export_empty"))
            return
        fp = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File (*.txt)", "*.txt")])
        if fp:
            try:
                with open(fp, "w", encoding="utf-8") as f:
                    for m in self.parsed_members:
                        f.write(m["email"] + "\n")
                messagebox.showinfo("Success", i18n.get("txt_exported", count=len(self.parsed_members), path=fp))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def export_csv(self):
        if not self.parsed_members:
            messagebox.showwarning("Warning", i18n.get("export_empty"))
            return
        fp = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV File (*.csv)", "*.csv")])
        if fp:
            try:
                with open(fp, "w", newline="", encoding="utf-8-sig") as f:
                    writer = csv.writer(f)
                    writer.writerow(["ID", "Name", "Email"])
                    for m in self.parsed_members:
                        writer.writerow([m["id"], m["name"], m["email"]])
                messagebox.showinfo("Success", i18n.get("csv_exported", path=fp))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def start_addition(self, limit=None):
        if not self.parsed_members:
            messagebox.showwarning("Warning", i18n.get("export_empty"))
            return

        target_list = self.parsed_members[:limit] if limit else self.parsed_members
        count = len(target_list)

        msg = i18n.get("confirm_body", count=count)
        if not messagebox.askokcancel(i18n.get("confirm_title"), msg):
            return

        self.btn_test.configure(state="disabled")
        self.btn_all.configure(state="disabled")
        self.btn_stop.configure(state="normal")

        try:
            delay = float(self.spin_delay.get())
        except ValueError:
            delay = 1.5

        callbacks = {
            "on_countdown": lambda sec: self.lbl_status.configure(text=i18n.get("status_countdown", seconds=sec)),
            "on_progress": self._on_automator_progress,
            "on_complete": self._on_automator_complete,
            "on_stop": self._on_automator_stop,
            "on_failsafe": self._on_automator_failsafe,
            "on_error": lambda err: messagebox.showerror("Error", str(err))
        }

        self.automator.start(target_list, delay=delay, callbacks=callbacks)

    def stop_addition(self):
        self.automator.stop()

    def _on_automator_progress(self, current, total, email):
        self.lbl_status.configure(text=i18n.get("status_running", current=current, total=total, email=email))
        self.progress_bar.set(current / total)

    def _on_automator_complete(self, total):
        self.lbl_status.configure(text=i18n.get("status_done", count=total))
        self._reset_action_buttons()
        messagebox.showinfo(i18n.get("dialog_done_title"), i18n.get("dialog_done_body", count=total))

    def _on_automator_stop(self, current, total):
        self.lbl_status.configure(text=i18n.get("status_stopped", current=current, total=total))
        self._reset_action_buttons()

    def _on_automator_failsafe(self):
        self.lbl_status.configure(text=i18n.get("status_failsafe"))
        self._reset_action_buttons()
        messagebox.showwarning(i18n.get("dialog_failsafe_title"), i18n.get("dialog_failsafe_body"))

    def _reset_action_buttons(self):
        self.btn_test.configure(state="normal")
        self.btn_all.configure(state="normal")
        self.btn_stop.configure(state="disabled")

    def show_how_to_use(self):
        """Opens responsive how-to-use dialog with dynamic word wrapping and clean badges."""
        top = ctk.CTkToplevel(self)
        top.title(i18n.get("guide_title"))
        top.geometry("640x560")
        top.minsize(480, 420)
        top.transient(self)
        top.grab_set()

        guide_box = ctk.CTkScrollableFrame(top, corner_radius=12)
        guide_box.pack(fill="both", expand=True, padx=14, pady=(14, 8))

        ctk.CTkLabel(
            guide_box,
            text=i18n.get("guide_heading"),
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color=("#0284C7", "#38BDF8")
        ).pack(anchor="w", pady=(0, 10))

        steps = [
            ("1", "STEP 1", i18n.get("step_1_title"), i18n.get("step_1_desc")),
            ("2", "STEP 2", i18n.get("step_2_title"), i18n.get("step_2_desc")),
            ("3", "STEP 3", i18n.get("step_3_title"), i18n.get("step_3_desc")),
            ("4", "STEP 4", i18n.get("step_4_title"), i18n.get("step_4_desc")),
            ("!", "SAFETY", i18n.get("step_safety_title"), i18n.get("step_safety_desc"))
        ]

        desc_labels = []

        for code, badge_text, step_title, step_desc in steps:
            card = ctk.CTkFrame(guide_box, corner_radius=8, fg_color=("gray85", "#252634"))
            card.pack(fill="x", pady=6)

            header_line = ctk.CTkFrame(card, fg_color="transparent")
            header_line.pack(fill="x", padx=12, pady=(8, 2))

            badge_color = ("#DC2626", "#991B1B") if code == "!" else ("#0284C7", "#0369A1")
            ctk.CTkLabel(
                header_line,
                text=f" {badge_text} ",
                fg_color=badge_color,
                corner_radius=5,
                text_color="#FFFFFF",
                font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold")
            ).pack(side="left", padx=(0, 8))

            ctk.CTkLabel(
                header_line,
                text=step_title,
                font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
                text_color=("#1D4ED8", "#93C5FD")
            ).pack(side="left")

            lbl_desc = ctk.CTkLabel(
                card,
                text=step_desc,
                justify="left",
                wraplength=520,
                font=ctk.CTkFont(family="Segoe UI", size=11),
                text_color=("gray15", "gray85")
            )
            lbl_desc.pack(anchor="w", padx=12, pady=(2, 8))
            desc_labels.append(lbl_desc)

        def on_modal_resize(event):
            if event.widget == top:
                new_wrap = max(240, top.winfo_width() - 85)
                for lbl in desc_labels:
                    lbl.configure(wraplength=new_wrap)

        top.bind("<Configure>", on_modal_resize)

        ctk.CTkButton(
            top,
            text=i18n.get("guide_btn_close"),
            height=34,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            command=top.destroy
        ).pack(pady=(4, 12))

    def show_about(self):
        """Displays professional About modal."""
        top = ctk.CTkToplevel(self)
        top.title(i18n.get("about_title"))
        top.geometry("480x340")
        top.minsize(400, 280)
        top.transient(self)
        top.grab_set()

        card = ctk.CTkFrame(top, corner_radius=12)
        card.pack(fill="both", expand=True, padx=16, pady=16)

        ctk.CTkLabel(
            card,
            text=i18n.get("about_heading"),
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color=("#8B5CF6", "#A78BFA")
        ).pack(pady=(16, 8))

        ctk.CTkLabel(
            card,
            text=i18n.get("about_body"),
            justify="center",
            font=ctk.CTkFont(family="Segoe UI", size=11)
        ).pack(padx=16, pady=10)

        ctk.CTkButton(
            card,
            text=i18n.get("about_btn_close"),
            width=100,
            height=32,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            command=top.destroy
        ).pack(pady=(10, 16))
