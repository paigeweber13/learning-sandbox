from pyquery import PyQuery as pq
from lxml import etree
import urllib

common_lisp_implementations_wikipedia = """<tr><td colspan="2" style="text-align:center"><a href="/wiki/Allegro_Common_Lisp" title="Allegro Common Lisp">Allegro CL</a>, <a href="/wiki/Armed_Bear_Common_Lisp" class="mw-redirect" title="Armed Bear Common Lisp">ABCL</a>, <a href="/wiki/CLISP" title="CLISP">CLISP</a>, <a href="/wiki/Clozure_CL" title="Clozure CL">Clozure CL</a>, <a href="/wiki/CMUCL" class="mw-redirect" title="CMUCL">CMUCL</a>, <a href="/wiki/Embeddable_Common_Lisp" title="Embeddable Common Lisp">ECL</a>, <a href="/wiki/GNU_Common_Lisp" title="GNU Common Lisp">GCL</a>, <a href="/wiki/LispWorks" title="LispWorks">LispWorks</a>, <a href="/w/index.php?title=Scieneer_Common_Lisp&amp;action=edit&amp;redlink=1" class="new" title="Scieneer Common Lisp (page does not exist)">Scieneer CL</a>, <a href="/wiki/SBCL" class="mw-redirect" title="SBCL">SBCL</a>, <a href="/wiki/Genera_(operating_system)" title="Genera (operating system)">Symbolics Common Lisp</a></td></tr>"""
scheme_implementations_wikipedia_url = "https://en.wikipedia.org/wiki/Category:Scheme_(programming_language)_implementations"

clisp = pq(common_lisp_implementations_wikipedia)
scheme = pq(url=scheme_implementations_wikipedia_url)

print('implementation,initial release,stable release,repository')
