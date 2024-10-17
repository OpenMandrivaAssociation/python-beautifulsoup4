%define module	beautifulsoup4

Summary:	The Screen-Scraper's Friend
Name:		python-beautifulsoup4
Version:	4.11.1
Release:	2
Group:		Development/Python
License:	Python
Url:		https://www.crummy.com/software/BeautifulSoup
Source0:	https://files.pythonhosted.org/packages/c6/62/8a2bef01214eeaa5a4489eca7104e152968729512ee33cb5fbbc37a896b7/beautifulsoup4-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildRequires:	pkgconfig(python)


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

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%{python_sitelib}/beautifulsoup4-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/bs4
