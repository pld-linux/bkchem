# TODO:
# - desktop file
%define		pre	pre2
Summary:	Python 2D chemical structure drawing tool
Summary(pl):	Narzêdzie do rysowania 2D struktur chemicznych
Name:		bkchem
Version:	0.8.0
Release:	0.%{pre}.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://zirael.org/bkchem/download/%{name}-%{version}-pre2.tar.gz
# Source0-md5:	8280cc1a8b675252b90d565cbf73cc0f
URL:		http://zirael.org/bkchem/index.html
BuildRequires:	python-devel
Requires:	python
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

%prep
%setup -q -n %{name}-%{version}-%{pre}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

#fix executable
sed -e "s@$RPM_BUILD_ROOT@@g" $RPM_BUILD_ROOT%{_bindir}/%{name} |\
	sed -e "s@%{name}.py@%{name}.pyo@g" >$RPM_BUILD_ROOT%{_bindir}/%{name}.new
mv $RPM_BUILD_ROOT%{_bindir}/%{name}.new $RPM_BUILD_ROOT%{_bindir}/%{name}

%find_lang BKchem

%clean
rm -rf $RPM_BUILD_ROOT

%files -f BKchem.lang
%defattr(644,root,root,755)
%doc README RELEASE doc/html
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/%{name}.py
%dir %{py_sitescriptdir}/%{name}/plugins
%{py_sitescriptdir}/%{name}/plugins/*.py[co]
%dir %{py_sitescriptdir}/%{name}/oasa
%{py_sitescriptdir}/%{name}/oasa/*.py[co]
%dir %{py_sitescriptdir}/%{name}/oasa/oasa/graph
%{py_sitescriptdir}/%{name}/oasa/oasa/graph/*.py[co]
%dir %{py_sitescriptdir}/%{name}/oasa/oasa
%{py_sitescriptdir}/%{name}/oasa/oasa/*.py[co]
