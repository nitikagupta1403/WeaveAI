"""Render an illustrative trail from frozen pixels and a frozen conditional field."""
from pathlib import Path
import hashlib
import json
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

OUT = Path(__file__).resolve().parent
PAPER = OUT.parents[1]
PIXELS = PAPER / 'reproducibility/frozen/05K1_Sentinel_Materialization_v1_0/canvases/S01/S01__row0781__s1p00.png'
ARCHIVE = PAPER / 'reproducibility/frozen/05K2_B1_Sentinel_Descriptor_Sweep_v1_0/P2_R0_05K2_B1_raster_fields_70.npz'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PIXELS) == '88313423804e74e186411df91dc3c655b54d5206ce54523d75b7474c0c7195a7'
with np.load(ARCHIVE, allow_pickle=False) as z:
    matches = np.flatnonzero((z['condition_index'] == 0) & (z['row_indices'] == 781) & (z['support_factors'] == 1.0))
    assert len(matches) == 1
    P = z['fields'][matches[0]].copy()
assert P.shape == (72, 72)
I = np.asarray(Image.open(PIXELS).convert('L'), dtype=float)
h, w = I.shape
yy, xx = np.indices(I.shape, dtype=float)
ink = np.maximum(255-I, 0)
cx, cy = (xx*ink).sum()/ink.sum(), (yy*ink).sum()/ink.sum()
radius = np.hypot(xx-cx, yy-cy)
rmax = radius.max()
theta = np.arctan2(yy-cy, xx-cx)
joint = np.histogram2d((radius/rmax).ravel(), theta.ravel(), bins=[np.linspace(0,1,73),np.linspace(-np.pi,np.pi,73)], weights=ink.ravel())[0]
tot = joint.sum(axis=1, keepdims=True)
replay = np.divide(joint, tot, out=np.zeros_like(joint), where=tot>0)
error = float(np.max(np.abs(replay-P)))
assert error < 1e-12, error
occupied = np.flatnonzero(P.sum(axis=1)>0)
shell = int(occupied[np.argmin(np.abs(occupied-35))])
F = np.fft.rfft(P, axis=1)
degrees = np.linspace(-180,180,72,endpoint=False)+2.5
blue, orange = '#176b9b', '#c96d20'
plt.rcParams.update({'font.size':10,'axes.titlesize':13,'axes.labelsize':10,'font.family':'DejaVu Sans'})
fig, axs = plt.subplots(2,3,figsize=(14,9),layout='constrained')
fig.suptitle('One sketch → distance and angle → angular harmonics',fontsize=20,weight='bold')
a=axs[0,0]; a.imshow(I,cmap='gray',vmin=0,vmax=255); a.set_title('A  Start with the sketch',loc='left'); a.axis('off')
a=axs[0,1]; a.imshow(I,cmap='gray',vmin=0,vmax=255)
for frac in [.25,.5,.75]: a.add_patch(Circle((cx,cy),rmax*frac,fill=False,color=blue,alpha=.35,lw=1))
rr=rmax*(shell+.5)/72
a.add_patch(Circle((cx,cy),rr,fill=False,color=orange,lw=2))
a.scatter([cx],[cy],s=25,color=blue)
a.annotate('',xy=(min(w-1,cx+140),cy),xytext=(cx,cy),arrowprops={'arrowstyle':'->','color':blue})
a.text(cx+55,cy-12,'angle = 0°',color=blue,fontsize=9)
a.annotate('distance',xy=(cx,cy-rr),xytext=(cx+25,cy-rr*.6),color=orange,arrowprops={'arrowstyle':'->','color':orange})
a.set_xlim(0,w-1);a.set_ylim(h-1,0);a.set_title('B  Measure around the ink centre',loc='left');a.axis('off')
a=axs[0,2]; im=a.imshow(P,origin='lower',aspect='auto',extent=[-180,180,0,1],cmap='Blues',vmin=0)
a.axhline((shell+.5)/72,color=orange,lw=2);a.set(xlabel='Angle (degrees)',ylabel='Normalized distance',title='C  Unroll the angular distributions')
fig.colorbar(im,ax=a,shrink=.7,label='Within-shell proportion of ink')
a=axs[1,0];a.plot(degrees,P[shell],color=orange,lw=2);a.set(xlabel='Angle (degrees)',ylabel='Within-shell proportion of ink',title=f'D  Read one shell (bin {shell+1} of 72)');a.set_xlim(-180,180)
a=axs[1,1];a.bar(np.arange(1,37),np.abs(F[shell,1:]),color=orange,width=.8);a.set(xlabel='Harmonic order: oscillations per turn',ylabel='Fourier amplitude',title='E  Separate angular scales');a.set_xlim(.3,36.7)
a=axs[1,2];im=a.imshow(np.abs(F[:,1:]),origin='lower',aspect='auto',extent=[.5,36.5,0,1],cmap='Blues',vmin=0);a.axhline((shell+.5)/72,color=orange,lw=2);a.set(xlabel='Harmonic order',ylabel='Normalized distance',title='F  Keep each scale across distance');fig.colorbar(im,ax=a,shrink=.7,label='Fourier amplitude')
fig.savefig(OUT/'FIGURE_1_TEACHING_TRAIL.png',dpi=180)
fig.savefig(OUT/'FIGURE_1_TEACHING_TRAIL.svg')
plt.close(fig)
provenance={'purpose':'Illustrative teaching example, not population evidence','selection':'First archived sentinel S01; no effect-based selection','original_relative_path':'Harem/8-10.tif','row_index':781,'condition_index':0,'support_factor':1.0,'pixel_source':str(PIXELS.relative_to(PAPER)),'pixel_sha256':sha(PIXELS),'field_source':str(ARCHIVE.relative_to(PAPER)),'field_sha256':sha(ARCHIVE),'pixel_field_replay_max_abs_error':error,'selected_shell_1_based':shell+1,'shell_selection':'Occupied shell nearest zero-based index 35','transform':'numpy.fft.rfft along angular dimension; no rescaling','display':'Positive harmonics 1–36; amplitude only, phase not displayed','coordinate_convention':'Image y increases downward; angle in [-pi,pi]; radial extent from complete raster grid','outputs':{p.name:sha(p) for p in [OUT/'FIGURE_1_TEACHING_TRAIL.png',OUT/'FIGURE_1_TEACHING_TRAIL.svg']}}
(OUT/'FIGURE_1_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps({'pixel_field_replay_max_abs_error':error,'selected_shell':shell+1,'outputs':list(provenance['outputs'])}))
