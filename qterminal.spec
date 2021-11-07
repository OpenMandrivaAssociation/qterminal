Summary:	QT-based multitab terminal emulator
Name:		qterminal
Version:	1.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Source0:	https://github.com/lxqt/qterminal/releases/download/%{version}/qterminal-%{version}.tar.xz
License:	GPLv2
Group:		Terminals
Url:		https://github.com/lxde/qterminal
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(qtermwidget5)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	cmake(lxqt)

%description
Qt based multitab terminal emulator.

%prep
%autosetup -p1
%cmake_qt5 -DPULL_TRANSLATIONS:BOOL=OFF -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-drop.desktop
%{_datadir}/appdata/qterminal.appdata.xml
%{_datadir}/icons/*/*/*/qterminal.*
%lang(arn) %{_datadir}/qterminal/translations/qterminal_arn.qm
%lang(ast) %{_datadir}/qterminal/translations/qterminal_ast.qm
