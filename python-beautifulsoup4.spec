%define module	beautifulsoup4
  
Summary:	The Screen-Scraper's Friend 
Name:		python-beautifulsoup4
Version:	4.5.0
Release:	1
Group:		Development/Python
License:	Python
Url:		http://www.crummy.com/software/BeautifulSoup 
Source0:	http://www.crummy.com/software/BeautifulSoup/bs4/download/4.5/%{module}-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
  
%description 
The BeautifulSoup class turns arbitrarily bad HTML into a tree-like 
nested tag-soup list of Tag objects and text snippets. A Tag object 
corresponds to an HTML tag.  It knows about the HTML tag's attributes, 
and contains a representation of everything contained between the 
original tag and its closing tag (if any). It's easy to extract Tags 
that meet certain criteria. 
  
%prep
%setup -qn %{module}-%{version}
  
%install 
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST

