# Generates the navy-toned intro background and the OG share image.
# Source photo: "A Justiça" (Alfredo Ceschiatti), by Morio, CC BY-SA 3.0, Wikimedia Commons.
import sys,os
os.chdir('/workspace/social')
src_code=open('make2.py').read().split('make(1080,1920')[0]
src_code=src_code.replace('def make(W','def _make(W')
exec(src_code)
OUT='/workspace/liberdade/photos/'
# intro bg: 3:4 portrait-ish, plain toned (no gradient overlay text) – use bg() then lighten bottom gradient handled by CSS
for w in (640,1080,1600):
    h=int(w*4/3)
    im=bg(w,h,0.55).convert('RGB')
    q=70 if w<1600 else 66
    im.save(OUT+f'justica-{w}.webp','WEBP',quality=q,method=6)
    print(w,os.path.getsize(OUT+f'justica-{w}.webp'))
# OG 1200x630
W,H=1200,630
img=bg(W,1700,0.62).crop((0,70,W,70+H))
d=ImageDraw.Draw(img)
L=Image.new("RGBA",img.size,(0,0,0,0)); dl=ImageDraw.Draw(L)
b=F(MONO,118,"Bold"); parts=[("200",GREEN,245),(" OU ",(205,215,232),230),("403",RED,245),("?",WHITE,245)]
x=70;y=215
for p,c,a in parts: dl.text((x,y),p,font=b,fill=c+(a,),anchor="lm"); x+=dl.textlength(p,font=b)
a=L.getchannel("A"); sh=Image.new("RGBA",img.size,(2,8,20,0)); sh.putalpha(a.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(20)))
img=Image.alpha_composite(Image.alpha_composite(img,sh),L)
d=ImageDraw.Draw(img)
hf=F(OSW,62,"Bold")
d.rectangle((70,330,70+130,336),fill=GOLD)
d.text((70,420),"A REGRA TEM DE VALER PARA TODOS.",font=hf,fill=WHITE,anchor="ls")
d.text((70,500),"liberdade.shklr.org",font=F(INTER,34,"SemiBold"),fill=GOLD,anchor="ls")
d.text((W-24,H-18),CREDIT,font=F(INTER,18,"Regular"),fill=MUTED,anchor="rs")
img.convert("RGB").save('/workspace/liberdade/og.jpg',quality=84,optimize=True,progressive=True)
print('og',os.path.getsize('/workspace/liberdade/og.jpg'))
