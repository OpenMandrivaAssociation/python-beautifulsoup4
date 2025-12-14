%define module	beautifulsoup4

Summary:	The Screen-Scraper's Friend
Name:		python-beautifulsoup4
Version:	4.14.3
Release:	1
Group:		Development/Python
License:	Python
Url:		https://www.crummy.com/software/BeautifulSoup
Source0:	https://files.pythonhosted.org/packages/source/b/beautifulsoup4/beautifulsoup4-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
BuildRequires:  python-hatchling
BuildRequires:  python-soupsieve
BuildRequires:	pkgconfig(python)
BuildSystem:    python


%description
The BeautifulSoup class turns arbitrarily bad HTML into a tree-like
nested tag-soup list of Tag objects and text snippets. A Tag object
corresponds to an HTML tag.  It knows about the HTML tag's attributes,
and contains a representation of everything contained between the
original tag and its closing tag (if any). It's easy to extract Tags
that meet certain criteria.

%files
%{python_sitelib}/bs4
%{python_sitelib}/beautifulsoup4-%{version}.dist-info
