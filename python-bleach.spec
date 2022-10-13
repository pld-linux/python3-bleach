# TODO: use system html5lib
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	An easy safelist-based HTML-sanitizing tool
Summary(pl.UTF-8):	Proste, oparte na liście elementów bezpiecznych, narzędzie do porządkowania HTML-a
Name:		python-bleach
# keep 3.x here for python2 support
Version:	3.3.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/bleach/
Source0:	https://files.pythonhosted.org/packages/source/b/bleach/bleach-%{version}.tar.gz
# Source0-md5:	b4c1b8f27289f9e5d73792daed4c0879
URL:		https://pypi.org/project/bleach/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 3.0.0
BuildRequires:	python-six >= 1.9.0
BuildRequires:	python-webencodings
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.0.0
BuildRequires:	python3-six >= 1.9.0
BuildRequires:	python3-webencodings
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bleach is an allowed-list-based HTML sanitizing library that escapes
or strips markup and attributes.

%description -l pl.UTF-8
Bleach to oparta na liście elementów dozwolonych biblioteka
zabezpieczająca lub usuwająca znaczniki i atrybuty.

%package -n python3-bleach
Summary:	An easy safelist-based HTML-sanitizing tool
Summary(pl.UTF-8):	Proste, oparte na liście elementów bezpiecznych, narzędzie do porządkowania HTML-a
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-bleach
Bleach is an allowed-list-based HTML sanitizing library that escapes
or strips markup and attributes.

%description -n python3-bleach -l pl.UTF-8
Bleach to oparta na liście elementów dozwolonych biblioteka
zabezpieczająca lub usuwająca znaczniki i atrybuty.

%package apidocs
Summary:	API documentation for Python bleach module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona bleach
Group:		Documentation

%description apidocs
API documentation for Python bleach module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona bleach.

%prep
%setup -q -n bleach-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS LICENSE README.rst
%{py_sitescriptdir}/bleach
%{py_sitescriptdir}/bleach-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-bleach
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS LICENSE README.rst
%{py3_sitescriptdir}/bleach
%{py3_sitescriptdir}/bleach-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
