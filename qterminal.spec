%define gitdate 20240419

Summary:	QT-based multitab terminal emulator
Name:		qterminal
Version:	2.0.0
Release:	%{?gitdate:0.%{gitdate}.}1
Source0:	https://github.com/lxqt/qterminal/%{!?gitdate:releases/download/%{version}/qterminal-%{version}.tar.xz}%{?gitdate:archive/refs/heads/master.tar.gz#/%{name}-%{gitdate}.tar.gz}
License:	GPLv2
Group:		Terminals
Url:		https://github.com/lxqt/qterminal
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(qtermwidget6)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	cmake(lxqt)

%description
Qt based multitab terminal emulator.

%prep
%autosetup -p1 -n %{name}-%{?gitdate:master}%{!?gitdate:%{version}}
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
