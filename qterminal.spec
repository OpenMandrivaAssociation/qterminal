%define	_subversion 1309992712

Name:		qterminal
Version: 	0.4.0
Release: 	3
License:	GPLv2
Source0:	%{name}-%{name}-master.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}_it.ts
Group:		Terminals
Summary:	QT-based multitab terminal emulator
URL:		https://gitorious.org/qtermwidget
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	qtermwidget-devel >= 0.4.0-1

Patch0:		%{name}-0.4.0-italian-translations.patch

%description
QT-based multitab terminal emulator. 
Based on QTermWidget by e_k@users.sourceforge.net 

%prep
%setup -q -n %{name}-%{name}
%patch0 -p1 -b .itts
cp %{S:3} src/translations/

%build
%cmake

%install
rm -rf %{buildroot}
%makeinstall_std -C build
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}_drop.desktop

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_drop.desktop
%{_datadir}/pixmaps/%{name}.png
%lang(cs) %{_datadir}/%{name}/translations/%{name}_cs.qm
%lang(it) %{_datadir}/%{name}/translations/%{name}_it.qm
