# TODO: use system html5lib
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	An easy safelist-based HTML-sanitizing tool
Summary(pl.UTF-8):	Proste, oparte na liście elementów bezpiecznych, narzędzie do porządkowania HTML-a
Name:		python3-bleach
Version:	5.0.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/bleach/
Source0:	https://files.pythonhosted.org/packages/source/b/bleach/bleach-%{version}.tar.gz
# Source0-md5:	97322e672e4b285e6354c40d07166fc4
URL:		https://pypi.org/project/bleach/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.0.0
BuildRequires:	python3-six >= 1.9
BuildRequires:	python3-webencodings
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bleach is an allowed-list-based HTML sanitizing library that escapes
or strips markup and attributes.

%description -l pl.UTF-8
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
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS LICENSE README.rst SECURITY.md
%{py3_sitescriptdir}/bleach
%{py3_sitescriptdir}/bleach-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
