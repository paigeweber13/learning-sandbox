import lxml
import lxml.html
import urllib.request

wikipedia_base_url = "https://en.wikipedia.org"
common_lisp_implementations_wikipedia = """<tr><td colspan="2" style="text-align:center"><a href="/wiki/Allegro_Common_Lisp" title="Allegro Common Lisp">Allegro CL</a>, <a href="/wiki/Armed_Bear_Common_Lisp" class="mw-redirect" title="Armed Bear Common Lisp">ABCL</a>, <a href="/wiki/CLISP" title="CLISP">CLISP</a>, <a href="/wiki/Clozure_CL" title="Clozure CL">Clozure CL</a>, <a href="/wiki/CMUCL" class="mw-redirect" title="CMUCL">CMUCL</a>, <a href="/wiki/Embeddable_Common_Lisp" title="Embeddable Common Lisp">ECL</a>, <a href="/wiki/GNU_Common_Lisp" title="GNU Common Lisp">GCL</a>, <a href="/wiki/LispWorks" title="LispWorks">LispWorks</a>, <a href="/w/index.php?title=Scieneer_Common_Lisp&amp;action=edit&amp;redlink=1" class="new" title="Scieneer Common Lisp (page does not exist)">Scieneer CL</a>, <a href="/wiki/SBCL" class="mw-redirect" title="SBCL">SBCL</a>, <a href="/wiki/Genera_(operating_system)" title="Genera (operating system)">Symbolics Common Lisp</a></td></tr>"""
scheme_implementations_wikipedia_url = "https://en.wikipedia.org/wiki/Category:Scheme_(programming_language)_implementations"

clisp = lxml.html.fragment_fromstring(common_lisp_implementations_wikipedia)
scheme = lxml.html.parse(
        urllib.request.urlopen(scheme_implementations_wikipedia_url))

print('implementation,initial release,stable release,repository')
for link in clisp.cssselect('a'):
    next_url = wikipedia_base_url + link.attrib['href']
    print(next_url)
    try:
        a = lxml.html.parse(urllib.request.urlopen(next_url)).getroot()
        table = a.cssselect('table.infobox')
        table = table[0]
        for row in table.cssselect('tr'):
            header = row.cssselect('th')
            value = row.cssselect('td')
            if len(header) > 0:
                print(lxml.etree.tostring(header[0]))
            if len(value) > 0:
                print(lxml.etree.tostring(value[0]))
    except urllib.error.HTTPError as e:
        print('error retrieving url', next_url)
        print('error:', e)
