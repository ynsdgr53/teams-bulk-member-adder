"""
Internationalization (i18n) Module
Supports English (en), Turkish (tr), Spanish (es), French (fr), and German (de).
"""

LANGUAGES = {
    "en": "English",
    "tr": "Türkçe",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch"
}

TRANSLATIONS = {
    "en": {
        "app_title": "Teams Bulk Member Adder",
        "app_subtitle": "Automate adding members to Microsoft Teams from Excel & CSV files",
        "dark_mode": "Dark Mode",
        "how_to_use_btn": "How to Use",
        "about_btn": "About",
        
        # Section 1: File Selection
        "sec_file": "1. Source File (Excel / CSV)",
        "file_placeholder": "Select an Excel (.xlsx, .xls) or CSV file...",
        "btn_browse": "Browse...",
        "lbl_sheet": "Sheet:",
        "file_not_selected": "No file selected yet.",
        "file_loaded": "File loaded successfully: {filename}",
        "file_empty_sheet": "No valid data found in selected sheet!",
        "file_error": "Could not read file: {error}",
        
        # Section 2: Column Mapping
        "sec_columns": "2. Column Mapping (Auto-detected & Customizable)",
        "lbl_email": "Email Column:*",
        "lbl_id": "Member/Student ID:",
        "lbl_name": "Full Name:",
        "lbl_delay": "Search Delay:",
        "lbl_delay_unit": "sec (for directory search)",
        "col_empty": "(None)",
        
        # Section 3: Preview Table
        "sec_preview": "3. Member List ({count} Found)",
        "col_header_id": "Member ID",
        "col_header_name": "Full Name",
        "col_header_email": "Email Address",
        "btn_export_txt": "Export TXT",
        "btn_export_csv": "Export CSV",
        "txt_exported": "{count} email addresses exported successfully:\n{path}",
        "csv_exported": "Member list exported successfully as CSV:\n{path}",
        "export_empty": "The list is currently empty.",
        
        # Section 4: Execution & Control
        "step_hint": "QUICK STEPS: 1. Open 'Add member' in Teams  ->  2. Click 'Add All' and focus search box (5s delay)  ->  3. Click 'Add' in Teams when done",
        "status_ready": "Ready. Select a mode to begin.",
        "status_reading": "Reading file data...",
        "btn_test": "Test (First 2)",
        "btn_add_all": "Add All to Teams",
        "btn_stop": "Stop",
        "footer_text": "Open Source Microsoft Teams Automation Tool • MIT License",
        
        # Automation Dialogs & Prompts
        "confirm_title": "Start Automation",
        "confirm_body": (
            "A total of {count} members will be added to Microsoft Teams.\n\n"
            "PREPARATION:\n"
            "1. When you click 'OK', a 5-SECOND AUDIBLE COUNTDOWN will begin.\n"
            "2. Switch to your Microsoft Teams window immediately.\n"
            "3. Click inside the 'Add member' search box so the cursor is blinking.\n"
            "4. Do not move your mouse or press keys while members are being typed.\n\n"
            "Do you want to proceed?"
        ),
        "status_countdown": "Click inside Teams search box! Starting in {seconds} seconds...",
        "status_running": "Adding member [{current}/{total}]: {email}",
        "status_done": "Completed! {count} members have been entered into the search field.",
        "status_stopped": "Process cancelled by user ({current}/{total} entered).",
        "status_failsafe": "Emergency stop triggered (mouse moved to corner of the screen).",
        "dialog_done_title": "Process Completed!",
        "dialog_done_body": (
            "{count} members have been successfully entered into Microsoft Teams!\n\n"
            "Please switch to your Teams window and click the 'Add' button to finalize."
        ),
        "dialog_failsafe_title": "Emergency Stop",
        "dialog_failsafe_body": "Automation was stopped because the mouse cursor was moved to the corner of the screen.",
        
        # Guide Modal
        "guide_title": "How to Use - Step-by-Step Guide",
        "guide_heading": "Microsoft Teams Automated Member Addition Guide",
        "guide_btn_close": "Understood, Close",
        "step_1_title": "Select Your File",
        "step_1_desc": "- Click 'Browse...' and choose your Excel (.xlsx, .xls) or CSV file.\n- The application will automatically detect Email, ID, and Name columns.\n- Verify that members appear correctly in the preview table.",
        "step_2_title": "Prepare Microsoft Teams",
        "step_2_desc": "- Open the Microsoft Teams desktop or web application and go to your Team/Class.\n- Click the '...' (More options) menu next to the team name and select 'Add member'.\n- Ensure the member search input box is visible on your screen.",
        "step_3_title": "Start the Automation",
        "step_3_desc": "- Click 'Add All to Teams' (or 'Test (First 2)' to verify first).\n- An audible 5-second countdown will start.\n- During these 5 seconds, switch to Teams and click inside the member search field.",
        "step_4_title": "Watch and Finalize",
        "step_4_desc": "- The tool will paste each email (Ctrl+V), wait for Teams directory resolution, and press Enter to select each person.\n- Once all members are added as tags/chips in the box, a completion prompt will appear.\n- Click the blue 'Add' button in Teams to save the members to your team.",
        "step_safety_title": "Safety & Emergency Stop",
        "step_safety_desc": "- If you need to stop the automation at any moment, simply move your mouse cursor to ANY CORNER of your screen (FailSafe).\n- You can also click the red 'Stop' button in the application.",
        
        # About Modal
        "about_title": "About Teams Bulk Member Adder",
        "about_heading": "Teams Bulk Member Adder v1.0.0",
        "about_body": (
            "An open-source desktop tool to automate bulk member enrollment into Microsoft Teams.\n\n"
            "Created for educators, system administrators, and team owners worldwide.\n\n"
            "• License: MIT License (Free & Open Source)\n"
            "• Technology: Python 3, CustomTkinter, PyAutoGUI\n"
            "• Multi-language: English, Turkish, Spanish, French, German"
        ),
        "about_btn_close": "Close"
    },
    
    "tr": {
        "app_title": "Teams Toplu Üye Ekleme Aracı",
        "app_subtitle": "Excel ve CSV dosyalarından Microsoft Teams'e otomatik üye ekleme",
        "dark_mode": "Karanlık Mod",
        "how_to_use_btn": "Nasıl Kullanılır?",
        "about_btn": "Hakkında",
        
        "sec_file": "1. Kaynak Dosya (Excel / CSV)",
        "file_placeholder": "Excel (.xlsx, .xls) veya CSV dosyası seçin...",
        "btn_browse": "Dosya Seç...",
        "lbl_sheet": "Sayfa (Sheet):",
        "file_not_selected": "Henüz dosya seçilmedi.",
        "file_loaded": "Dosya başarıyla yüklendi: {filename}",
        "file_empty_sheet": "Seçilen sayfada geçerli veri bulunamadı!",
        "file_error": "Dosya okunamadı: {error}",
        
        "sec_columns": "2. Sütun Eşleştirme (Otomatik Algılanır / Değiştirilebilir)",
        "lbl_email": "E-Posta Sütunu:*",
        "lbl_id": "Öğrenci/Üye No:",
        "lbl_name": "Ad Soyad:",
        "lbl_delay": "Arama Bekleme:",
        "lbl_delay_unit": "sn (dizin araması için)",
        "col_empty": "(Yok)",
        
        "sec_preview": "3. Üye Listesi ({count} Kişi)",
        "col_header_id": "Numara / ID",
        "col_header_name": "Ad Soyad",
        "col_header_email": "E-Posta Adresi",
        "btn_export_txt": "Mailleri TXT",
        "btn_export_csv": "CSV Kaydet",
        "txt_exported": "{count} e-posta adresi kaydedildi:\n{path}",
        "csv_exported": "Liste başarıyla CSV olarak kaydedildi:\n{path}",
        "export_empty": "Liste şu anda boş.",
        
        "step_hint": "HIZLI ADIMLAR: 1. Teams'te 'Üye ekle'yi açın  ->  2. 'Hepsini Ekle'ye basıp kutuya tıklayın (5 sn süre)  ->  3. Bitince Teams'ten 'Ekle'ye basın",
        "status_ready": "Hazır. Başlamak için bir mod seçin.",
        "status_reading": "Dosya okunuyor...",
        "btn_test": "Test Et (İlk 2)",
        "btn_add_all": "Hepsini Teams'e Ekle",
        "btn_stop": "Durdur",
        "footer_text": "Açık Kaynak Microsoft Teams Otomasyon Aracı • MIT Lisansı",
        
        "confirm_title": "Otomasyon Başlatılıyor",
        "confirm_body": (
            "Toplam {count} üye Microsoft Teams sınıfına/ekibine eklenecektir.\n\n"
            "HAZIRLIK:\n"
            "1. 'Tamam' butonuna bastığınızda 5 SANİYELİK SESLİ GERİ SAYIM başlayacaktır.\n"
            "2. Hemen Microsoft Teams pencerenize geçin.\n"
            "3. 'Üye ekle' arama kutusuna tıklayın (imlecin yanıp söndüğünden emin olun).\n"
            "4. Üyeler yazılırken farenizi oynatmayın.\n\n"
            "Başlatmak istiyor musunuz?"
        ),
        "status_countdown": "Teams arama kutusuna tıklayın! Başlıyor: {seconds} saniye...",
        "status_running": "Üye ekleniyor [{current}/{total}]: {email}",
        "status_done": "Tamamlandı! {count} üye arama kutusuna girildi.",
        "status_stopped": "İşlem kullanıcı tarafından durduruldu ({current}/{total} girildi).",
        "status_failsafe": "Acil durdurma tetiklendi (Fare ekranın köşesine çekildi).",
        "dialog_done_title": "İşlem Tamamlandı!",
        "dialog_done_body": (
            "{count} üye Teams arama kutusuna başarıyla girildi!\n\n"
            "Lütfen Teams penceresine dönüp 'Ekle' butonuna tıklayarak işlemi tamamlayın."
        ),
        "dialog_failsafe_title": "Acil Durdurma",
        "dialog_failsafe_body": "Fare imleci ekranın köşesine götürüldüğü için işlem güvenlik amacıyla durduruldu.",
        
        "guide_title": "Nasıl Kullanılır? - Kullanım Kılavuzu",
        "guide_heading": "Microsoft Teams Otomatik Üye Ekleme Kılavuzu",
        "guide_btn_close": "Anladım, Kapat",
        "step_1_title": "Dosyanızı Seçin",
        "step_1_desc": "- 'Dosya Seç...' butonuna basarak Excel (.xlsx, .xls) veya CSV dosyanızı yükleyin.\n- Program E-Posta, Numara ve İsim sütunlarını otomatik olarak tanır.\n- Önizleme tablosunda bilgilerin doğruluğunu kontrol edin.",
        "step_2_title": "Teams Penceresini Hazırlayın",
        "step_2_desc": "- Microsoft Teams'i açın ve ilgili ekibe/sınıfa gidin.\n- Ekip adının yanındaki '...' simgesine tıklayıp 'Üye ekle' seçeneğini açın.\n- Arama kutusunun ekranda göründüğünden emin olun.",
        "step_3_title": "Otomasyonu Başlatın",
        "step_3_desc": "- 'Hepsini Teams'e Ekle' (veya denemek için 'Test Et') butonuna tıklayın.\n- 5 saniyelik sesli geri sayım başlar.\n- Bu sürede Teams'teki arama kutucuğuna tıklayıp imleci yerleştirin.",
        "step_4_title": "İzleyin ve Tamamlayın",
        "step_4_desc": "- Program mailleri panodan yapıştırır (Ctrl+V), Teams dizininde aratıp Enter ile seçer.\n- Tüm üyeler kutuda belirdiğinde işlem tamamlanır.\n- Teams'teki mavi 'Ekle' butonuna basarak kaydedin.",
        "step_safety_title": "Güvenlik ve Acil Durdurma",
        "step_safety_desc": "- İşlemi anında durdurmak için farenizi ekranın herhangi bir DIŞ KÖŞESİNE çekmeniz yeterlidir (FailSafe).\n- Ayrıca 'Durdur' butonunu kullanabilirsiniz.",
        
        "about_title": "Hakkında",
        "about_heading": "Teams Bulk Member Adder v1.0.0",
        "about_body": (
            "Microsoft Teams'e toplu üye eklemeyi otomatikleştiren açık kaynaklı masaüstü aracı.\n\n"
            "Eğitmenler, akademisyenler ve ekip yöneticileri için geliştirilmiştir.\n\n"
            "• Lisans: MIT Lisansı (Ücretsiz & Açık Kaynak)\n"
            "• Teknoloji: Python 3, CustomTkinter, PyAutoGUI\n"
            "• Çoklu Dil: İngilizce, Türkçe, İspanyolca, Fransızca, Almanca"
        ),
        "about_btn_close": "Kapat"
    },

    "es": {
        "app_title": "Añadidor Masivo de Miembros para Teams",
        "app_subtitle": "Automatice la adición de miembros a Microsoft Teams desde archivos Excel y CSV",
        "dark_mode": "Modo Oscuro",
        "how_to_use_btn": "Cómo Usar",
        "about_btn": "Acerca de",
        
        "sec_file": "1. Archivo Fuente (Excel / CSV)",
        "file_placeholder": "Seleccione un archivo Excel (.xlsx, .xls) o CSV...",
        "btn_browse": "Examinar...",
        "lbl_sheet": "Hoja:",
        "file_not_selected": "Aún no se ha seleccionado ningún archivo.",
        "file_loaded": "Archivo cargado con éxito: {filename}",
        "file_empty_sheet": "¡No se encontraron datos válidos en la hoja seleccionada!",
        "file_error": "No se pudo leer el archivo: {error}",
        
        "sec_columns": "2. Asignación de Columnas (Automática y Personalizable)",
        "lbl_email": "Columna de Correo:*",
        "lbl_id": "ID / Matrícula:",
        "lbl_name": "Nombre Completo:",
        "lbl_delay": "Pausa de Búsqueda:",
        "lbl_delay_unit": "seg (para búsqueda en directorio)",
        "col_empty": "(Ninguno)",
        
        "sec_preview": "3. Lista de Miembros ({count} Encontrados)",
        "col_header_id": "ID de Miembro",
        "col_header_name": "Nombre Completo",
        "col_header_email": "Correo Electrónico",
        "btn_export_txt": "Exportar TXT",
        "btn_export_csv": "Exportar CSV",
        "txt_exported": "{count} correos exportados con éxito:\n{path}",
        "csv_exported": "Lista exportada con éxito como CSV:\n{path}",
        "export_empty": "La lista está actualmente vacía.",
        
        "step_hint": "PASOS RÁPIDOS: 1. Abra 'Agregar miembro' en Teams  ->  2. Haga clic en 'Agregar todo' y seleccione el cuadro (espera de 5s)  ->  3. Haga clic en 'Agregar' en Teams",
        "status_ready": "Listo. Seleccione un modo para comenzar.",
        "status_reading": "Leyendo archivo...",
        "btn_test": "Probar (Primeros 2)",
        "btn_add_all": "Agregar Todo a Teams",
        "btn_stop": "Detener",
        "footer_text": "Herramienta de Automatización de Microsoft Teams de Código Abierto • Licencia MIT",
        
        "confirm_title": "Iniciar Automatización",
        "confirm_body": (
            "Se agregarán {count} miembros a Microsoft Teams.\n\n"
            "PREPARACIÓN:\n"
            "1. Al hacer clic en 'Aceptar', comenzará una CUENTA REGRESIVA AUDIBLE DE 5 SEGUNDOS.\n"
            "2. Cambie a su ventana de Microsoft Teams de inmediato.\n"
            "3. Haga clic dentro del campo de búsqueda 'Agregar miembro' para que el cursor parpadee.\n"
            "4. No mueva el ratón mientras se escriben los miembros.\n\n"
            "¿Desea continuar?"
        ),
        "status_countdown": "¡Haga clic dentro del buscador de Teams! Comenzando en {seconds} segundos...",
        "status_running": "Agregando miembro [{current}/{total}]: {email}",
        "status_done": "¡Completado! {count} miembros ingresados en el campo de búsqueda.",
        "status_stopped": "Proceso cancelado por el usuario ({current}/{total} ingresados).",
        "status_failsafe": "Parada de emergencia activada (el ratón se movió a la esquina de la pantalla).",
        "dialog_done_title": "¡Proceso Completado!",
        "dialog_done_body": (
            "¡Se han ingresado {count} miembros con éxito en Microsoft Teams!\n\n"
            "Por favor, cambie a su ventana de Teams y haga clic en 'Agregar' para finalizar."
        ),
        "dialog_failsafe_title": "Parada de Emergencia",
        "dialog_failsafe_body": "La automatización se detuvo porque el cursor del ratón se movió a la esquina de la pantalla.",
        
        "guide_title": "Cómo Usar - Guía Paso a Paso",
        "guide_heading": "Guía de Adición Automatizada de Miembros en Microsoft Teams",
        "guide_btn_close": "Entendido, Cerrar",
        "step_1_title": "Seleccione su Archivo",
        "step_1_desc": "- Haga clic en 'Examinar...' y elija su archivo Excel (.xlsx, .xls) o CSV.\n- La aplicación detectará automáticamente las columnas de Correo, ID y Nombre.\n- Compruebe que los miembros aparezcan correctamente en la tabla de vista previa.",
        "step_2_title": "Prepare Microsoft Teams",
        "step_2_desc": "- Abra Microsoft Teams y vaya a su Equipo/Clase.\n- Haga clic en '...' junto al nombre del equipo y elija 'Agregar miembro'.\n- Asegúrese de que el cuadro de búsqueda esté visible en la pantalla.",
        "step_3_title": "Inicie la Automatización",
        "step_3_desc": "- Haga clic en 'Agregar Todo a Teams' (o 'Probar (Primeros 2)' para verificar).\n- Comenzará una cuenta regresiva sonora de 5 segundos.\n- Durante este tiempo, cambie a Teams y haga clic dentro del cuadro de búsqueda.",
        "step_4_title": "Supervise y Finalice",
        "step_4_desc": "- La herramienta pegará cada correo (Ctrl+V), esperará la búsqueda en el directorio y presionará Enter.\n- Cuando todos los miembros aparezcan como etiquetas, la tarea estará lista.\n- Haga clic en el botón azul 'Agregar' en Teams para guardar.",
        "step_safety_title": "Seguridad y Parada de Emergencia",
        "step_safety_desc": "- Si necesita detener la automatización en cualquier momento, simplemente mueva el ratón a CUALQUIER ESQUINA de su pantalla (FailSafe).\n- También puede usar el botón 'Detener'.",
        
        "about_title": "Acerca de",
        "about_heading": "Teams Bulk Member Adder v1.0.0",
        "about_body": (
            "Herramienta de escritorio de código abierto para automatizar la inscripción masiva de miembros en Microsoft Teams.\n\n"
            "Desarrollada para educadores, administradores y coordinadores de todo el mundo.\n\n"
            "• Licencia: Licencia MIT (Gratuita y de Código Abierto)\n"
            "• Tecnología: Python 3, CustomTkinter, PyAutoGUI\n"
            "• Multilingüe: Inglés, Turco, Español, Francés, Alemán"
        ),
        "about_btn_close": "Cerrar"
    },

    "fr": {
        "app_title": "Ajout Groupé de Membres pour Teams",
        "app_subtitle": "Automatisez l'ajout de membres dans Microsoft Teams à partir de fichiers Excel et CSV",
        "dark_mode": "Mode Sombre",
        "how_to_use_btn": "Mode d'emploi",
        "about_btn": "À propos",
        
        "sec_file": "1. Fichier Source (Excel / CSV)",
        "file_placeholder": "Sélectionnez un fichier Excel (.xlsx, .xls) ou CSV...",
        "btn_browse": "Parcourir...",
        "lbl_sheet": "Feuille :",
        "file_not_selected": "Aucun fichier sélectionné.",
        "file_loaded": "Fichier chargé avec succès : {filename}",
        "file_empty_sheet": "Aucune donnée valide trouvée dans la feuille sélectionnée !",
        "file_error": "Impossible de lire le fichier : {error}",
        
        "sec_columns": "2. Mappage des Colonnes (Automatique et Personnalisable)",
        "lbl_email": "Colonne E-mail :*",
        "lbl_id": "ID / Numéro :",
        "lbl_name": "Nom Complet :",
        "lbl_delay": "Délai de Recherche :",
        "lbl_delay_unit": "sec (pour la recherche d'annuaire)",
        "col_empty": "(Aucun)",
        
        "sec_preview": "3. Liste des Membres ({count} Trouvés)",
        "col_header_id": "ID Membre",
        "col_header_name": "Nom Complet",
        "col_header_email": "Adresse E-mail",
        "btn_export_txt": "Exporter TXT",
        "btn_export_csv": "Exporter CSV",
        "txt_exported": "{count} adresses e-mail exportées avec succès :\n{path}",
        "csv_exported": "Liste exportée avec succès au format CSV :\n{path}",
        "export_empty": "La liste est actuellement vide.",
        
        "step_hint": "ÉTAPES RAPIDES : 1. Ouvrez 'Ajouter un membre' dans Teams  ->  2. Cliquez sur 'Ajouter tout' et ciblez le champ (délai 5s)  ->  3. Cliquez sur 'Ajouter' dans Teams",
        "status_ready": "Prêt. Sélectionnez un mode pour commencer.",
        "status_reading": "Lecture du fichier...",
        "btn_test": "Tester (2 premiers)",
        "btn_add_all": "Tout Ajouter à Teams",
        "btn_stop": "Arrêter",
        "footer_text": "Outil d'automatisation Microsoft Teams Open Source • Licence MIT",
        
        "confirm_title": "Démarrer l'Automatisation",
        "confirm_body": (
            "Un total de {count} membres seront ajoutés à Microsoft Teams.\n\n"
            "PRÉPARATION :\n"
            "1. Lorsque vous cliquez sur 'OK', un COMPTE À REBOURS SONORE DE 5 SECONDES commence.\n"
            "2. Basculez immédiatement vers la fenêtre Microsoft Teams.\n"
            "3. Cliquez dans le champ de recherche 'Ajouter un membre' afin que le curseur clignote.\n"
            "4. Ne touchez pas à la souris pendant la saisie automatique.\n\n"
            "Souhaitez-vous continuer ?"
        ),
        "status_countdown": "Cliquez dans le champ Teams ! Début dans {seconds} secondes...",
        "status_running": "Ajout du membre [{current}/{total}] : {email}",
        "status_done": "Terminé ! {count} membres ont été saisis dans le champ de recherche.",
        "status_stopped": "Processus annulé par l'utilisateur ({current}/{total} saisis).",
        "status_failsafe": "Arrêt d'urgence déclenché (souris déplacée dans le coin de l'écran).",
        "dialog_done_title": "Processus Terminé !",
        "dialog_done_body": (
            "{count} membres ont été saisis avec succès dans Microsoft Teams !\n\n"
            "Veuillez basculer vers votre fenêtre Teams et cliquer sur le bouton 'Ajouter' pour valider."
        ),
        "dialog_failsafe_title": "Arrêt d'Urgence",
        "dialog_failsafe_body": "L'automatisation a été arrêtée car le curseur de la souris a été déplacé dans un coin de l'écran.",
        
        "guide_title": "Mode d'emploi - Guide Étape par Étape",
        "guide_heading": "Guide d'Ajout Automatisé de Membres dans Microsoft Teams",
        "guide_btn_close": "Compris, Fermer",
        "step_1_title": "Sélectionnez votre Fichier",
        "step_1_desc": "- Cliquez sur 'Parcourir...' et choisissez votre fichier Excel (.xlsx, .xls) ou CSV.\n- L'application détecte automatiquement les colonnes E-mail, ID et Nom.\n- Vérifiez que les membres apparaissent correctement dans le tableau d'aperçu.",
        "step_2_title": "Préparez Microsoft Teams",
        "step_2_desc": "- Ouvrez Microsoft Teams et accédez à votre Équipe/Classe.\n- Cliquez sur '...' à côté du nom de l'équipe et choisissez 'Ajouter un membre'.\n- Assurez-vous que le champ de recherche est bien visible à l'écran.",
        "step_3_title": "Lancez l'Automatisation",
        "step_3_desc": "- Cliquez sur 'Tout Ajouter à Teams' (ou 'Tester (2 premiers)').\n- Un compte à rebours sonore de 5 secondes démarre.\n- Pendant ce délai, basculez vers Teams et cliquez dans le champ de recherche.",
        "step_4_title": "Surveillez et Validez",
        "step_4_desc": "- L'outil colle chaque e-mail (Ctrl+V), attend la recherche d'annuaire et valide avec Entrée.\n- Une fois tous les membres ajoutés sous forme de pastilles, la saisie est finie.\n- Cliquez sur le bouton bleu 'Ajouter' dans Teams pour valider.",
        "step_safety_title": "Sécurité et Arrêt d'Urgence",
        "step_safety_desc": "- Pour arrêter l'opération à tout moment, déplacez simplement votre curseur vers N'IMPORTE QUEL COIN de l'écran (FailSafe).\n- Vous pouvez aussi utiliser le bouton 'Arrêter'.",
        
        "about_title": "À propos",
        "about_heading": "Teams Bulk Member Adder v1.0.0",
        "about_body": (
            "Outil bureautique open-source pour automatiser l'inscription groupée de membres dans Microsoft Teams.\n\n"
            "Conçu pour les enseignants, universitaires et administrateurs du monde entier.\n\n"
            "• Licence : Licence MIT (Gratuit et Open Source)\n"
            "• Technologie : Python 3, CustomTkinter, PyAutoGUI\n"
            "• Multilingue : Anglais, Turc, Espagnol, Français, Allemand"
        ),
        "about_btn_close": "Fermer"
    },

    "de": {
        "app_title": "Teams Massen-Mitglieder-Hinzufüger",
        "app_subtitle": "Automatisieren Sie das Hinzufügen von Mitgliedern zu Microsoft Teams aus Excel- und CSV-Dateien",
        "dark_mode": "Dunkelmodus",
        "how_to_use_btn": "Anleitung",
        "about_btn": "Über",
        
        "sec_file": "1. Quelldatei (Excel / CSV)",
        "file_placeholder": "Wählen Sie eine Excel- (.xlsx, .xls) oder CSV-Datei...",
        "btn_browse": "Durchsuchen...",
        "lbl_sheet": "Tabellenblatt:",
        "file_not_selected": "Noch keine Datei ausgewählt.",
        "file_loaded": "Datei erfolgreich geladen: {filename}",
        "file_empty_sheet": "Keine gültigen Daten im ausgewählten Blatt gefunden!",
        "file_error": "Datei konnte nicht gelesen werden: {error}",
        
        "sec_columns": "2. Spaltenzuordnung (Automatisch erkannt & Anpassbar)",
        "lbl_email": "E-Mail-Spalte:*",
        "lbl_id": "Mitglieds-/Matrikel-Nr.:",
        "lbl_name": "Vollständiger Name:",
        "lbl_delay": "Suchverzögerung:",
        "lbl_delay_unit": "Sek. (für Verzeichnissuche)",
        "col_empty": "(Keine)",
        
        "sec_preview": "3. Mitgliederliste ({count} Gefunden)",
        "col_header_id": "Mitglieds-ID",
        "col_header_name": "Vollständiger Name",
        "col_header_email": "E-Mail-Adresse",
        "btn_export_txt": "TXT Exportieren",
        "btn_export_csv": "CSV Exportieren",
        "txt_exported": "{count} E-Mail-Adressen erfolgreich exportiert:\n{path}",
        "csv_exported": "Mitgliederliste erfolgreich als CSV exportiert:\n{path}",
        "export_empty": "Die Liste ist derzeit leer.",
        
        "step_hint": "SCHNELLSTART: 1. 'Mitglied hinzufügen' in Teams öffnen  ->  2. 'Alle hinzufügen' klicken & Suchfeld fokussieren (5s Zeit)  ->  3. In Teams auf 'Hinzufügen' klicken",
        "status_ready": "Bereit. Wählen Sie einen Modus.",
        "status_reading": "Lese Datei...",
        "btn_test": "Test (Erste 2)",
        "btn_add_all": "Alle zu Teams hinzufügen",
        "btn_stop": "Stopp",
        "footer_text": "Open-Source Microsoft Teams Automatisierungstool • MIT-Lizenz",
        
        "confirm_title": "Automatisierung Starten",
        "confirm_body": (
            "Insgesamt werden {count} Mitglieder zu Microsoft Teams hinzugefügt.\n\n"
            "VORBEREITUNG:\n"
            "1. Wenn Sie auf 'OK' klicken, beginnt ein HÖRBARER 5-SEKUNDEN-COUNTDOWN.\n"
            "2. Wechseln Sie sofort zu Ihrem Microsoft Teams-Fenster.\n"
            "3. Klicken Sie in das Suchfeld 'Mitglied hinzufügen', sodass der Cursor blinkt.\n"
            "4. Bewegen Sie während der automatischen Eingabe weder Maus noch Tastatur.\n\n"
            "Möchten Sie fortfahren?"
        ),
        "status_countdown": "In Teams-Suchfeld klicken! Startet in {seconds} Sekunden...",
        "status_running": "Füge Mitglied hinzu [{current}/{total}]: {email}",
        "status_done": "Abgeschlossen! {count} Mitglieder wurden in das Suchfeld eingegeben.",
        "status_stopped": "Vorgang vom Benutzer abgebrochen ({current}/{total} eingegeben).",
        "status_failsafe": "Not-Aus ausgelöst (Maus wurde in Bildschirmecke bewegt).",
        "dialog_done_title": "Vorgang Abgeschlossen!",
        "dialog_done_body": (
            "{count} Mitglieder wurden erfolgreich in Microsoft Teams eingegeben!\n\n"
            "Bitte wechseln Sie zum Teams-Fenster und klicken Sie auf 'Hinzufügen', um abzuschließen."
        ),
        "dialog_failsafe_title": "Not-Aus",
        "dialog_failsafe_body": "Die Automatisierung wurde gestoppt, da der Mauszeiger in eine Bildschirmecke bewegt wurde.",
        
        "guide_title": "Anleitung - Schritt-für-Schritt",
        "guide_heading": "Anleitung zur automatisierten Mitgliederhinzufügung in Microsoft Teams",
        "guide_btn_close": "Verstanden, Schließen",
        "step_1_title": "Wählen Sie Ihre Datei",
        "step_1_desc": "- Klicken Sie auf 'Durchsuchen...' und wählen Sie Ihre Excel- (.xlsx, .xls) oder CSV-Datei.\n- Das Programm erkennt E-Mail-, ID- und Namensspalten automatisch.\n- Prüfen Sie die Vorschautabelle auf Richtigkeit.",
        "step_2_title": "Microsoft Teams Vorbereiten",
        "step_2_desc": "- Öffnen Sie Microsoft Teams und navigieren Sie zu Ihrem Team/Kurs.\n- Klicken Sie neben dem Teamnamen auf '...' und wählen Sie 'Mitglied hinzufügen'.\n- Stellen Sie sicher, dass das Suchfeld auf dem Bildschirm sichtbar ist.",
        "step_3_title": "Automatisierung Starten",
        "step_3_desc": "- Klicken Sie auf 'Alle zu Teams hinzufügen' (oder zuerst 'Test (Erste 2)').\n- Ein hörbarer 5-Sekunden-Countdown startet.\n- Klicken Sie währenddessen in Teams in das Mitgliedersuchfeld.",
        "step_4_title": "Zusehen und Bestätigen",
        "step_4_desc": "- Das Tool fügt jede E-Mail ein (Strg+V), wartet auf die Verzeichnissuche und bestätigt mit Enter.\n- Sobald alle Mitglieder als Tags erscheinen, ist die Eingabe fertig.\n- Klicken Sie in Teams auf die blaue Schaltfläche 'Hinzufügen', um zu speichern.",
        "step_safety_title": "Sicherheit & Not-Aus",
        "step_safety_desc": "- Wenn Sie den Vorgang abbrechen möchten, bewegen Sie die Maus in eine BELIEBIGE ECKE des Bildschirms (FailSafe).\n- Alternativ können Sie die rote 'Stopp'-Schaltfläche verwenden.",
        
        "about_title": "Über",
        "about_heading": "Teams Bulk Member Adder v1.0.0",
        "about_body": (
            "Open-Source Desktop-Tool zur Automatisierung der Masseneinschreibung von Mitgliedern in Microsoft Teams.\n\n"
            "Entwickelt für Lehrkräfte, Akademiker und Teamleiter weltweit.\n\n"
            "• Lizenz: MIT-Lizenz (Kostenlos & Open Source)\n"
            "• Technologie: Python 3, CustomTkinter, PyAutoGUI\n"
            "• Mehrsprachig: Englisch, Türkisch, Spanisch, Französisch, Deutsch"
        ),
        "about_btn_close": "Schließen"
    }
}

class I18nManager:
    def __init__(self, default_lang="en"):
        self.current_lang = default_lang if default_lang in TRANSLATIONS else "en"

    def set_language(self, lang_code):
        if lang_code in TRANSLATIONS:
            self.current_lang = lang_code

    def get(self, key, **kwargs):
        lang_dict = TRANSLATIONS.get(self.current_lang, TRANSLATIONS["en"])
        val = lang_dict.get(key, TRANSLATIONS["en"].get(key, key))
        if kwargs and isinstance(val, str):
            try:
                return val.format(**kwargs)
            except Exception:
                return val
        return val

# Global instance
i18n = I18nManager(default_lang="en")
