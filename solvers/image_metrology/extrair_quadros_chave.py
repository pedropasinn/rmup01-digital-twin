import subprocess, os, sys, glob
import numpy as np
from PIL import Image

VID="/home/pedro/repo/rmup01-digital-twin/research/videos/RMUP-01_SF_EN.mp4"
OUT="/home/pedro/repo/rmup01-digital-twin/research/images/frames/VID-0001-key"
TMP="/tmp/claude-1000/-home-pedro-repo/c643aa96-a46d-4331-9423-036303f11c55/scratchpad/kf"
os.makedirs(OUT, exist_ok=True)

# (label, t_start, t_end) janelas de interesse
WINDOWS = [
 ("mov-plan-cg",        12.0, 15.0),
 ("case-profile-175",   17.0, 20.5),
 ("baseplate-plan",     22.5, 25.5),
 ("baseplate-oblique",  29.5, 32.5),
 ("bridge-3arm",        36.5, 39.5),
 ("mov-plan-esc",       46.5, 48.5),
 ("balance-barrel-macro",51.5,53.5),
 ("barrel-balance-obl", 54.0, 57.5),
 ("hand-profile",       58.0, 60.5),
 ("mov-plan-assembled", 65.5, 68.5),
 ("indication-macro",   74.0, 80.5),
 ("watch-plan-cg",      89.0, 93.5),
 ("crown-selector",     94.0, 98.5),
 ("caseback-plan",     143.5,145.5),
 ("mov-plan-cg-2",     147.5,149.5),
 ("watch-plan-cg-2",   150.0,154.5),
 ("mov-on-strap",      127.0,130.5),
]

def sharp(p):
    im = np.asarray(Image.open(p).convert("L"), dtype=np.float32)
    # laplaciano 4-vizinhos
    lap = (-4*im[1:-1,1:-1] + im[:-2,1:-1] + im[2:,1:-1] + im[1:-1,:-2] + im[1:-1,2:])
    return float(lap.var())

rows=[]
for label, t0, t1 in WINDOWS:
    d=os.path.join(TMP,label); os.makedirs(d, exist_ok=True)
    for f in glob.glob(d+"/*.png"): os.remove(f)
    subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-ss",str(t0),"-to",str(t1),
                    "-i",VID,"-vsync","0",d+"/%04d.png"],check=True)
    files=sorted(glob.glob(d+"/*.png"))
    if not files: continue
    scored=[(sharp(f),f) for f in files]
    scored.sort(reverse=True)
    best_s,best_f=scored[0]
    idx=files.index(best_f)
    t = t0 + idx/25.0
    fn = "IMG-VID0001-K%s.png" % ("%06.2f"%t).replace(".","_")
    dst=os.path.join(OUT,fn)
    Image.open(best_f).save(dst)
    rows.append((fn,label,round(t,2),round(best_s,1),len(files)))
    print(f"{label:24s} t={t:7.2f}s  sharp={best_s:9.1f}  n={len(files)}  -> {fn}")

import csv
with open(os.path.join(OUT,"_selecao.csv"),"w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["arquivo","janela","timestamp_s","variancia_laplaciano","quadros_avaliados"])
    w.writerows(rows)
