Summary:	Python 2D chemical structure drawing tool
Summary(pl):	Narzędzie do rysowania 2D struktur chemicznych
Name:		bkchem
Version:	0.9.0
Release:	2
License:	GPL
Group:		X11/Applications/Science
Source0:	http://zirael.org/bkchem/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
# Source0-md5:	85b89c905af843cb191cc6ab30fe3a4c
Patch0:		%{name}-reaction_mode.patch 
URL:		http://zirael.org/bkchem/index.html
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	python
Requires:	python-devel-tools
Requires:	Pmw
Requires:	python-PyXML
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BKchem is a free (as in free software :o) chemical drawing program. It
was conceived and written by Beda Kosata. Supported file formats are
SVG and CML. The output looks best with the Adobe SVG viewer, but
sodipodi and batik do a reasonable job as well.

%description -l pl
BKchem to wolnodostępny program do rysunków chemicznych. Jego
pomysłodawcą i autorem jest Beda Kosata. Obsługiwane formaty plików to
SVG i CML. Wyjście wygląda najlepiej pod przeglądarką SVG firmy Adobe,
ale sodipodi i batik także wyświetlają je sensownie.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install images/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/bkchem.png
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

#fix executable
sed -e "s@$RPM_BUILD_ROOT@@g" -i $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -e "s@%{name}.py@%{name}.pyo@g" -i $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -e "s@$RPM_BUILD_ROOT@@g" -i $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/site_config.py

%find_lang BKchem

%clean
rm -rf $RPM_BUILD_ROOT

%files -f BKchem.lang
%defattr(644,root,root,755)
%doc README RELEASE doc/html
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/site_config.py
%{py_sitescriptdir}/%{name}/%{name}.py
%dir %{py_sitescriptdir}/%{name}/plugins
%{py_sitescriptdir}/%{name}/plugins/*.py[co]
%dir %{py_sitescriptdir}/%{name}/oasa
%{py_sitescriptdir}/%{name}/oasa/*.py[co]
%dir %{py_sitescriptdir}/%{name}/oasa/oasa/graph
%{py_sitescriptdir}/%{name}/oasa/oasa/graph/*.py[co]
%dir %{py_sitescriptdir}/%{name}/oasa/oasa
%{py_sitescriptdir}/%{name}/oasa/oasa/*.py[co]
%dir %{py_sitescriptdir}/%{name}/piddle
%dir %{py_sitescriptdir}/%{name}/piddle/*.py[co]
