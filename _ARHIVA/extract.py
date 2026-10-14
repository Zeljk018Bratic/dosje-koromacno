import os, sys
from pypdf import PdfReader

here = os.path.dirname(os.path.abspath(__file__))
d = os.path.join(here, 'uploads')
target = [n for n in os.listdir(d) if n.lower().endswith('.pdf')][0]
r = PdfReader(os.path.join(d, target))
texts = []
for i, p in enumerate(r.pages):
    try:
        t = p.extract_text() or ""
    except Exception as e:
        t = "[err %s]" % e
    texts.append("===== PAGE %d =====\n%s" % (i + 1, t))
full = "\n".join(texts)
out = os.path.join(here, 'doc_full.txt')
with open(out, 'w') as f:
    f.write(full)
print("pages:", len(r.pages), "chars:", len(full))
