; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)

# define coq_version "0.9.3"
# define coq_path "C:\Users\Gero Kunter\coquery-0.9.3"
# define coq_icon "icons\artwork\logo.ico"

AppId={{42204621-F37F-40C3-96E2-886FFF94D497}
AppName=Coquery
AppCopyright=Copyright (C) 2016 Gero Kunter
AppVersion={#coq_version}
AppVerName=Coquery {#coq_version}
AppPublisher=Coquery maintainers
AppPublisherURL=http://www.coquery.org
AppSupportURL=http://www.coquery.org
AppUpdatesURL=http://www.coquery.org
DefaultDirName={pf}\Coquery
DisableProgramGroupPage=yes
LicenseFile={#coq_path}\make\gpl-3.0.txt
OutputBaseFilename=coquery-{#coq_version}-win32-setup
SetupIconFile={#coq_path}\coquery\icons\artwork\logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; \
  GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "{#coq_path}\make\dist\coquery\coquery.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#coq_path}\make\dist\coquery\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files
Source: "{#coq_path}\coquery\icons\artwork\logo.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\Coquery"; Filename: "{app}\coquery.exe"; WorkingDir: "{app}"; \
  IconFileName: "{app}\{#coq_icon}"; Tasks: desktopicon

[Run]
Filename: "{app}\coquery.exe"; Description: "{cm:LaunchProgram,Coquery}"; Flags: nowait postinstall skipifsilent

