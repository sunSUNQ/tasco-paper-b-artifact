# PROVENANCE: exported from the internal TASCO research repository. This script references internal absolute paths and is a provenance record; the runnable reproduction interface is reproduction/verify.py. Source file: colorize_tables.py
"""Apply color semantic markup to benefit values in paper-emse.tex (tables 2 & 3)."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RED = "\\textcolor[rgb]{0.55,0.09,0.18}{"
GRN = "\\textcolor[rgb]{0.10,0.42,0.22}{"
END = "}"

tex = Path(r"D:\tasco-temp\research-semantic-compression\r5\paper-b\emse-submission-pack-r1\paper-emse.tex")
c = tex.read_text(encoding="utf-8")

# Table 2 benefit means
c = c.replace("$-41.8\\%$ [$", RED + "$-41.8\\%$" + END + " [$")
c = c.replace("$-21.3\\%$ [$", RED + "$-21.3\\%$" + END + " [$")
c = c.replace("$-23.0\\%$ [$", RED + "$-23.0\\%$" + END + " [$")
# Table 3 per-family means (M1)
for v in ("-59.9", "-6.9", "-11.1", "-346.7"):
    c = c.replace("& $" + v + "$ [", "& " + RED + "$" + v + "$" + END + " [")
# M2 family means
for v in ("-7.7", "-28.5", "-3.6", "-87.3"):
    c = c.replace("& $" + v + "$ [", "& " + RED + "$" + v + "$" + END + " [")
# M3 family means (no CI)
for v in ("-32.9", "-9.9", "-39.3"):
    c = c.replace("& $" + v + "$ &", "& " + RED + "$" + v + "$" + END + " &")
# positives
for v in ("+7.1", "+30.3"):
    c = c.replace("& $" + v + "$ [", "& " + GRN + "$" + v + "$" + END + " [")
    c = c.replace("& $" + v + "$ &", "& " + GRN + "$" + v + "$" + END + " &")

tex.write_text(c, encoding="utf-8")
n = c.count("textcolor[rgb]")
print("colorized fragments:", n)
