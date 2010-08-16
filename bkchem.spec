#
# TODO: python unpackaged files: some of them are needed by program. It's impossible to postclean them
#
%define		_pre	pre2
Summary:	Python 2D chemical structure drawing tool
Summary(pl.UTF-8):	Narzędzie do rysowania dwuwymiarowych struktur chemicznych
Name:		bkchem
Version:	0.14.0
Release:	0.%{_pre}.1
License:	GPL v2+
Group:		X11/Applications/Science
Source0:	http://bkchem.zirael.org/download/%{name}-%{version}-%{_pre}.tar.gz
# Source0-md5:	e2a2ec2e4625acdefce1ad6eb2433291
Source1:	%{name}.desktop
URL:		http://bkchem.zirael.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
#BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	Pmw
Requires:	python
Requires:	python-PyXML
Requires:	python-devel-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BKchem is a free (as in free software :o) chemical drawing program. It
was conceived and written by Beda Kosata. Supported file formats are
SVG and CML. The output looks best with the Adobe SVG viewer, but
sodipodi and batik do a reasonable job as well.

%description -l pl.UTF-8
BKchem to wolnodostępny program do rysunków chemicznych. Jego
pomysłodawcą i autorem jest Beda Kosata. Obsługiwane formaty plików to
SVG i CML. Wyjście wygląda najlepiej pod przeglądarką SVG firmy Adobe,
ale sodipodi i batik także wyświetlają je sensownie.

%package plugin-cairo
Summary:	High quality PDF and PNG export plugin
Summary(pl.UTF-8):	Wtyczka do tworzenia wysokiej jakości plików PDF i PNG
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}
Requires:	python-pycairo >= 0.5.1

%description plugin-cairo
The plugin, that allowes exporting the picture to the high quality PDF
and PNG files. It uses Cairo and pycario libraries.

%description plugin-cairo -l pl.UTF-8
Wtyczka umożliwiająca eksportowanie do plików PDF i PNG, o wysokiej
jakości. Używane są biblioteki Cairo oraz pycairo.

%prep
%setup -q -n %{name}-%{version}-%{_pre}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install images/bkchem.png $RPM_BUILD_ROOT%{_pixmapsdir}/bkchem.png
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

#fix executable
%{__sed} -e "s@$RPM_BUILD_ROOT@@g" -i $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__sed} -e "s@%{name}.py@%{name}.pyo@g" -i $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__sed} -e "s@$RPM_BUILD_ROOT@@g" -i $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/site_config.py

%find_lang BKChem

rm -rf $RPM_BUILD_ROOT%{_docdir}/bkchem

#%%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f BKChem.lang
%defattr(644,root,root,755)
%doc PKG-INFO README doc/*
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
%dir %{py_sitescriptdir}/%{name}/plugins/piddle
%{py_sitescriptdir}/%{name}/plugins/piddle/*.py[co]
%{py_sitescriptdir}/*.egg-info
%exclude %{py_sitescriptdir}/%{name}/plugins/*cairo*

%files plugin-cairo
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{name}/plugins/*cairo*
