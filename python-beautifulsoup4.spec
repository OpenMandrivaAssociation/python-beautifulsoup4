%define module	beautifulsoup4

Summary:	The Screen-Scraper's Friend
Name:		python-beautifulsoup4
Version:	4.6.3
Release:	1
Group:		Development/Python
License:	Python
Url:		http://www.crummy.com/software/BeautifulSoup
Source0:	http://www.crummy.com/software/BeautifulSoup/bs4/download/%(echo %{version} |cut -d. -f1-2)/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)

%description
The BeautifulSoup class turns arbitrarily bad HTML into a tree-like
nested tag-soup list of Tag objects and text snippets. A Tag object
corresponds to an HTML tag.  It knows about the HTML tag's attributes,
and contains a representation of everything contained between the
original tag and its closing tag (if any). It's easy to extract Tags
that meet certain criteria.

%description
Beautiful Soup sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.

%package -n     python2-%{module}
Summary:        HTML/XML parser for quick-turnaround applications like screen-scraping
Group:          Development/Python

%description -n python2-%{module}
Beautiful Soup sits atop an HTML or XML parser, providing Pythonic
idioms for iterating, searching, and modifying the parse tree.
This is the Python 2 build of Beautiful Soup.

%prep
%setup -qn %{module}-%{version}

mkdir python3
mv `ls |grep -v python3` python3
cp -a python3 python2

%build
pushd python3
python setup.py build
popd

pushd python2
%{__python2} setup.py build
popd

%install
cd python3
%{__python} setup.py install --root=%{buildroot}

cd ../python2
%{__python2} setup.py install --root=%{buildroot}

%files
%{python_sitelib}/beautifulsoup4-%{version}-py%{py_ver}.egg-info/*
%{python_sitelib}/bs4

%files -n python2-beautifulsoup4
%{python2_sitelib}/beautifulsoup4-%{version}-py%{py2_ver}.egg-info/*
%{python2_sitelib}/bs4
