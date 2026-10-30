# Desktop (wide) intro background: statue on the right, navy fade on the left for text.
import os
from PIL import Image, ImageOps, ImageFilter
src=Image.open('/workspace/social/src.jpg').convert('RGB')
NAVY=(11,31,58)
def tone(im):
    im=ImageOps.autocontrast(ImageOps.grayscale(im),cutoff=1)
    return ImageOps.colorize(im,black=(4,12,26),white=(150,170,200),mid=NAVY)
for W in (1600,2400):
    H=W*9//16
    c=src.crop((0,0,src.width,int(src.height*0.80)))   # head..pedestal
    s=H/c.height; ph=tone(c.resize((int(c.width*s),H),Image.LANCZOS))
    canvas=Image.new('RGB',(W,H),(5,14,30))
    # blurred stretched backdrop
    back=tone(src.resize((W,int(src.height*W/src.width)))).crop((0,0,W,H)).filter(ImageFilter.GaussianBlur(W//60))
    canvas=Image.blend(canvas,back,0.55)
    x0=int(W*0.70-ph.width*0.55)
    m=Image.new('L',ph.size,255)
    fw=int(ph.width*0.28)
    for i in range(fw):
        v=int(255*i/fw)
        for edge in (i,ph.width-1-i): m.paste(v,(edge,0,edge+1,ph.height))
    canvas.paste(ph,(x0,0),m)
    canvas.save(f'photos/justica-wide-{W}.webp','WEBP',quality=68,method=6)
    print(W,os.path.getsize(f'photos/justica-wide-{W}.webp'))
