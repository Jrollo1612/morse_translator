[Setup]
; --- Infos générales ---
AppName=Traducteur Morse
AppVersion=1.2
AppPublisher=Joseph
DefaultDirName={userappdata}\TraducteurMorse
DisableProgramGroupPage=yes
OutputBaseFilename=TraducteurMorse-1.2-Setup
Compression=lzma
SolidCompression=yes

; --- Pas d'admin requis ---
PrivilegesRequired=lowest

; --- Installation silencieuse ou personnalisée ---
Uninstallable=yes
AlwaysRestart=no

[Files]
; --- Ton EXE unique
Source: "traducteur_morse_2.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; --- Icône menu démarrer
Name: "{userprograms}\Traducteur Morse"; Filename: "{app}\traducteur_morse_2.exe"; IconFilename: "traduction.ico"
; --- Icône bureau
Name: "{userdesktop}\Traducteur Morse"; Filename: "{app}\traducteur_morse_2.exe"; IconFilename: "traduction.ico"; Tasks: desktopicon

[Tasks]
; --- Option création icône bureau
Name: "desktopicon"; Description: "Créer une icône sur le bureau"; Flags: unchecked

[Run]
; --- Lancer automatiquement après installation (optionnel)
Filename: "{app}\traducteur_morse_2.exe"; Description: "Lancer Traducteur Morse"; Flags: nowait postinstall skipifsilent
