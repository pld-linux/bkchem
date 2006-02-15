Summary:	Python 2D chemical structure drawing tool
Summary(pl):	Narzêdzie do rysowania dwuwymiarowych struktur chemicznych
Name:		bkchem
Version:	0.11.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://bkchem.zirael.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	d40298db9d36c86c99f04f6d94ff9f7c
Source1:	%{name}.desktop
URL:		http://bkchem.zirael.org/
BuildRequires:	python
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
BKchem to wolnodostêpny program do rysunków chemicznych. Jego
pomys³odawc± i autorem jest Beda Kosata. Obs³ugiwane formaty plików to
SVG i CML. Wyj¶cie wygl±da najlepiej pod przegl±dark± SVG firmy Adobe,
ale sodipodi i batik tak¿e wy¶wietlaj± je sensownie.

%package plugin-cairo
Summary:	High quality PDF and PNG export plugin
Summary(pl):	Wtyczka do tworzenia wysokiej jako¶ci plików PDF i PNG
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}
Requires:	python-pycairo >= 0.5.1

%description plugin-cairo
The plugin, that allowes exporting the picture to the high quality PDF
and PNG files. It uses Cairo and pycario libraries.

%description plugin-cairo -l pl
Wtyczka umo¿liwiaj±ca exportowanie do plików PDF i PNG, o wysokiej 
jako¶ci. U¿ywane s± biblioteki Cairo oraz pycairo.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install images/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/bkchem.png
%{__python} setup.py install \
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
%dir %{py_sitescriptdir}/%{name}/plugins/piddle
%{py_sitescriptdir}/%{name}/plugins/piddle/*.py[co]
%exclude %{py_sitescriptdir}/%{name}/plugins/*cairo* 

%files plugin-cairo
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{name}/plugins/*cairo*
