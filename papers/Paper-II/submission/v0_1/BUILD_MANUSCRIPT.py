"""Build presentation derivatives from the hash-locked manuscript; no analysis runs.

Requires pandoc and xelatex on PATH. Run with Python 3 from any directory.
"""
from pathlib import Path
import hashlib
import re
import subprocess

DEST = Path(__file__).resolve().parent
PAPER = DEST.parent.parent
SOURCE = PAPER / 'P2_FINAL_MANUSCRIPT_ASSEMBLY_v0_7_FINAL_AUDITED.md'
EXPECTED_SHA256 = '3af5ca3baa9331f2227d2c121f13efb7f60046d3769c899383b1e7a4133ee870'

def formatting_copy():
    data = SOURCE.read_bytes()
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise RuntimeError('Frozen source hash changed; stop before generating.')
    text = data.decode('utf-8')
    old = '## 3.3 Angular Fourier morphology\n\n## 3.3 Angular Fourier morphology'
    assert text.count(old) == 1
    text = text.replace(old, '## 3.3 Angular Fourier morphology', 1)
    old = '### 3.4.7 Primary the controlled same-pixel support intervention inference'
    assert text.count(old) == 1
    text = text.replace(old, '### 3.4.7 Primary controlled same-pixel support intervention inference', 1)
    text = re.sub(r'(!\[[^\]]*\]\()([^)]*\.png)(\))', r'\1../../\2\3', text)
    old = r'''\boxed{
\text{validate the measurement frame;}
\newline
\text{allocate representation complexity only where evidence supports it;}
\newline
\text{preserve unsupported structure;}
\newline
\text{and keep retained latent variation traceable to explicit morphology coordinates.}
}'''
    new = r'''\boxed{\begin{gathered}
\text{validate the measurement frame;}\\
\text{allocate representation complexity only where evidence supports it;}\\
\text{preserve unsupported structure;}\\
\text{and keep retained latent variation traceable to explicit morphology coordinates.}
\end{gathered}}'''
    assert text.count(old) == 1
    return text.replace(old, new, 1)

if __name__ == '__main__':
    formatted = DEST / 'MANUSCRIPT_FORMATTED.md'
    formatted.write_text(formatting_copy(), encoding='utf-8')
    common = ['pandoc', str(formatted), '--from=markdown+tex_math_single_backslash',
              '--standalone', '--resource-path=' + str(DEST)]
    subprocess.run(common + ['--to=docx', '--output=' + str(DEST / 'MANUSCRIPT.docx')], check=True)
    subprocess.run(common + ['--pdf-engine=xelatex', '-V', 'geometry:margin=1in',
                            '-V', 'fontsize=10pt', '--output=' + str(DEST / 'MANUSCRIPT_REVIEW.pdf')], check=True)
