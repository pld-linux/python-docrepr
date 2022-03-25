#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Rendering Python docstrings in HTML
Summary(pl.UTF-8):	Obrazowanie pythonowych docstringów w HTML-u
Name:		python-docrepr
Version:	0.1.1
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/docrepr/
Source0:	https://files.pythonhosted.org/packages/source/d/docrepr/docrepr-%{version}.tar.gz
# Source0-md5:	e2d1b964a9f63518dcbd1d31b7273104
URL:		https://pypi.org/project/docrepr/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
docrepr renders Python docstrings in HTML. It is based on the
sphinxify module developed by Tim Dumol for the Sage Notebook and the
utils.inspector developed for their Spyder IDE.

%description -l pl.UTF-8
docrepr obrazuje pythonowe docstringi w HTML-u. Jest oparty na module
sphinxify, stworzonym przez Tima Dumola dla Sage Nootebooka oraz
utils.inspector, powstałego dla ich Spyder IDE.

%package -n python3-docrepr
Summary:	Rendering Python docstrings in HTML
Summary(pl.UTF-8):	Obrazowanie pythonowych docstringów w HTML-u
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-docrepr
docrepr renders Python docstrings in HTML. It is based on the
sphinxify module developed by Tim Dumol for the Sage Notebook and the
utils.inspector developed for their Spyder IDE.

%description -n python3-docrepr -l pl.UTF-8
docrepr obrazuje pythonowe docstringi w HTML-u. Jest oparty na module
sphinxify, stworzonym przez Tima Dumola dla Sage Nootebooka oraz
utils.inspector, powstałego dla ich Spyder IDE.

%prep
%setup -q -n docrepr-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc README.md
%{py_sitescriptdir}/docrepr
%{py_sitescriptdir}/docrepr-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-docrepr
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/docrepr
%{py3_sitescriptdir}/docrepr-%{version}-py*.egg-info
%endif
