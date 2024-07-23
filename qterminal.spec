#define gitdate 20240501

Summary:	QT-based multitab terminal emulator
Name:		qterminal
Version:	2.0.1
Release:	%{?gitdate:0.%{gitdate}.}1
Source0:	https://github.com/lxqt/qterminal/%{!?gitdate:releases/download/%{version}/qterminal-%{version}.tar.xz}%{?gitdate:archive/refs/heads/master.tar.gz#/%{name}-%{gitdate}.tar.gz}
Patch0:		qterminal-master-defaultfont.patch
License:	GPLv2
Group:		Terminals
Url:		https://github.com/lxqt/qterminal
BuildRequires:	cmake
BuildRequires:	ninja
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

%prep
%autosetup -p1 -n %{name}-%{?gitdate:master}%{!?gitdate:%{version}}

%conf
%cmake -DPULL_TRANSLATIONS:BOOL=OFF -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-drop.desktop
%{_datadir}/icons/*/*/*/qterminal.*
%{_datadir}/metainfo/qterminal.metainfo.xml
%{_datadir}/qterminal/qterminal_bookmarks_example.xml
%dir %{_datadir}/qterminal
%dir %{_datadir}/qterminal/translations
