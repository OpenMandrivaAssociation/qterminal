#define gitdate 20240501

Summary:	QT-based multitab terminal emulator
Name:		qterminal
Version:	2.2.0
Release:	%{?gitdate:0.%{gitdate}.}1
Source0:	https://github.com/lxqt/qterminal/%{!?gitdate:releases/download/%{version}/qterminal-%{version}.tar.xz}%{?gitdate:archive/refs/heads/master.tar.gz#/%{name}-%{gitdate}.tar.gz}
Patch0:		qterminal-master-defaultfont.patch
License:	GPLv2
Group:		Terminals
Url:		https://github.com/lxqt/qterminal
BuildSystem:	cmake
BuildOption:	-DPULL_TRANSLATIONS:BOOL=OFF
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(qtermwidget6)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(LayerShellQt)

%description
Qt based multitab terminal emulator.

%install -a
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
cat >%{buildroot}%{_datadir}/polkit-1/actions/com.github.lxqt.qterminal.policy <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-FileCopyrightText: no
     SPDX-License-Identifier: CC0-1.0
-->
<!DOCTYPE policyconfig PUBLIC
"-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
"http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">
<policyconfig>

 <vendor>Konsole</vendor>
 <vendor_url>https://apps.kde.org/konsole</vendor_url>

 <action id="com.github.lxqt.qterminal.pkexec.run">
    <description>QTerminal</description>
    <message>Authentication is required to run QTerminal in admin mode</message>
    <icon_name>qterminal</icon_name>
    <defaults>
     <allow_any>no</allow_any>
     <allow_inactive>no</allow_inactive>
     <allow_active>auth_admin</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">%{_bindir}/qterminal</annotate>
    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
 </action>
</policyconfig>
EOF


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-drop.desktop
%{_datadir}/icons/*/*/*/qterminal.*
%{_datadir}/metainfo/qterminal.metainfo.xml
%{_datadir}/qterminal/qterminal_bookmarks_example.xml
%dir %{_datadir}/qterminal
%dir %{_datadir}/qterminal/translations
%{_datadir}/polkit-1/actions/com.github.lxqt.qterminal.policy
