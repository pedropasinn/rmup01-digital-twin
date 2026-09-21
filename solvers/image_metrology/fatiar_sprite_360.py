#!/usr/bin/env python3
"""Fatia o sprite 360 oficial do RM UP-01 em quadros individuais.

O visualizador da pagina oficial serve uma tira horizontal unica. O numero de
quadros nao esta declarado no HTML; foi determinado por periodicidade:
o desvio-padrao por coluna da tira e um sinal periodico, e a FFT desse sinal
tem pico limpo em 81 ciclos -> 81 quadros de 800x800 px (64800 = 81 x 800).

Uso:  python fatiar_sprite_360.py research/images/rm-oficial/360_rmup-01_d01.jpg saida/
"""
import sys, os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def detectar_quadros(caminho, minimo=8, maximo=200):
    """Devolve (n_quadros, largura) pelo pico da FFT do perfil de colunas."""
    a = np.asarray(Image.open(caminho).convert("L"), dtype=np.float32)
    sinal = a.std(axis=0)
    espectro = np.abs(np.fft.rfft(sinal - sinal.mean()))
    largura_total = a.shape[1]
    candidatos = [(k, espectro[k]) for k in range(minimo, maximo + 1)
                  if largura_total % k == 0]
    if not candidatos:
        raise SystemExit("nenhum numero de quadros divide a largura da tira")
    k = max(candidatos, key=lambda t: t[1])[0]
    return k, largura_total // k


def fatiar(caminho, destino):
    n, w = detectar_quadros(caminho)
    im = Image.open(caminho)
    h = im.size[1]
    os.makedirs(destino, exist_ok=True)
    base = os.path.splitext(os.path.basename(caminho))[0].replace("360_rmup-01_", "360-")
    for i in range(n):
        im.crop((i * w, 0, (i + 1) * w, h)).save(f"{destino}/{base}-{i:02d}.jpg", quality=92)
    passo = 360.0 / n
    print(f"{n} quadros de {w}x{h} px, passo {passo:.2f} graus -> {destino}")
    print("marcadores do visualizador: Top view=00, Right view~%d, Back view=%d, Left view~%d"
          % (round(n / 4), round(n / 2), round(3 * n / 4)))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    fatiar(sys.argv[1], sys.argv[2])
