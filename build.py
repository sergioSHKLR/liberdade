import html
def t(tag,pt,en,cls='',raw=False):
    a=f' class="{cls}"' if cls else ''
    h=' data-html' if raw else ''
    return f'<{tag}{a}{h} data-pt="{html.escape(pt)}" data-en="{html.escape(en)}">{pt}</{tag}>'
ICON={
'person':'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
'heart':'<path d="M12 21s-8-5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 6-8 11-8 11z"/>',
'scale':'<path d="M12 3v18M5 21h14M6 7h12M6 7l-3 7h6zM18 7l-3 7h6z"/>',
'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
'terminal':'<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M12 15h5"/>',
'quote':'<path d="M7 7h4v4c0 3-2 5-4 6M14 7h4v4c0 3-2 5-4 6"/>',
'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
'play':'<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9l5 3-5 3z"/>',
'anchor':'<circle cx="12" cy="5" r="2"/><path d="M12 7v14M8 11h8M5 14c0 4 3 7 7 7s7-3 7-7"/>',
}
def ic(n): return f'<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{ICON[n]}</svg>'
def h2(n,pt,en): return f'<div class="sh">{ic(n)}{t("h2",pt,en)}</div>'
def fig(src,w,h,pt,en,altpt,alten):
    return f'<figure><img src="photos/{src}" width="{w}" height="{h}" loading="lazy" decoding="async" data-alt-pt="{html.escape(altpt)}" data-alt-en="{html.escape(alten)}" alt="{html.escape(altpt)}">{t("figcaption",pt,en)}</figure>'
DIV='<svg class="div" viewBox="0 0 200 20" aria-hidden="true"><path d="M0 10h80M120 10h80"/><path d="M100 3l2 5h5l-4 3 2 5-5-3-5 3 2-5-4-3h5z"/></svg>'
OBJ_PT='Liberdade imediata para Bolsonaro e os militares presos.'
OBJ_EN='Immediate freedom for Bolsonaro and the imprisoned service members.'
slog=[('Logs não mentem.',"Logs don't lie."),('Rollback da consciência não existe.','There is no rollback for a conscience.'),('Sem ordem por escrito, sem deploy.','No written order, no deploy.'),('Não repúdio.','Non-repudiation.'),('Integridade é o melhor firewall.','Integrity is the best firewall.'),('Problema de usuário ou de sistema?','User problem or system problem?'),('Daqui a quatro anos, onde estará sua consciência?','Four years from now, where will your conscience be?'),('O silêncio também é uma escolha.','Silence is also a choice.'),('Meu juramento foi à Constituição. O seu também.','My oath was to the Constitution. So was yours.'),('Justiça sem devido processo não é justiça.','Justice without due process is not justice.')]
grid=''.join(f'<li>{t("span",p,e)}</li>' for p,e in slog)
grid+='<li>'+t('span','Justiça que tarda é ilegal.','Justice delayed is unlawful.')+t('small','CF, art. 5º, LXXVIII — razoável duração do processo','Brazilian Constitution, art. 5, LXXVIII — right to a reasonable duration of proceedings')+'</li>'
TL='''<svg class="tl" viewBox="0 0 340 110" role="img" aria-label="1997–2018"><path class="ln" d="M45 55H295"/><g class="pt"><circle cx="45" cy="55" r="7"/><circle cx="170" cy="55" r="7"/><circle cx="295" cy="55" r="7"/></g><g class="yr"><text x="45" y="33">1997</text><text x="170" y="33">2008–12</text><text x="295" y="33">2018</text></g><g class="lb"><text x="45" y="85" data-pt="Recruta" data-en="Recruit">Recruta</text><text x="170" y="85" data-pt="Missões" data-en="Deployments">Missões</text><text x="295" y="85" data-pt="Reserva" data-en="Retired">Reserva</text></g></svg>'''
LAUREL='''<svg class="laurel" viewBox="0 0 120 60" aria-hidden="true"><path d="M60 55C35 50 20 35 18 10M60 55C85 50 100 35 102 10"/><g class="lf"><ellipse cx="24" cy="18" rx="3" ry="7" transform="rotate(-30 24 18)"/><ellipse cx="30" cy="31" rx="3" ry="7" transform="rotate(-50 30 31)"/><ellipse cx="42" cy="43" rx="3" ry="7" transform="rotate(-70 42 43)"/><ellipse cx="96" cy="18" rx="3" ry="7" transform="rotate(30 96 18)"/><ellipse cx="90" cy="31" rx="3" ry="7" transform="rotate(50 90 31)"/><ellipse cx="78" cy="43" rx="3" ry="7" transform="rotate(70 78 43)"/></g><path d="M60 14l3 7h7l-6 4 2 7-6-4-6 4 2-7-6-4h7z" class="st"/></svg>'''
body=f'''
<header class="top"><span class="brand">{ic("anchor")}Liberdade</span>
<div class="lang" role="group" aria-label="Idioma / Language"><button type="button" data-set="pt" aria-pressed="true">PT</button><button type="button" data-set="en" aria-pressed="false">EN</button></div></header>
<main class="wrap">
<section class="hero">
<div class="badge" aria-hidden="true"><span class="ok">200</span><span class="or" data-pt="OU" data-en="OR">OU</span><span class="no">403?</span></div>
<p class="sr" data-pt="200 OU 403?" data-en="200 OR 403?">200 OU 403?</p>
{t("p","Status da sua consciência?","Status of your conscience?","status")}
{DIV}
{t("h1","Liberdade","Freedom")}
{t("p",OBJ_PT,OBJ_EN,"obj")}
{t("p","Pela lei, sem violência. Com respeito a quem serve e protege.","Through the law, without violence. With respect for those who serve and protect.","sub")}
</section>

<section id="respeito">
{h2("heart","Respeito a quem serve","Respect for those who serve")}
{LAUREL}
{t("p","Nos Estados Unidos, fui — e ainda sou — agradecido pelo meu serviço. Por estranhos, na rua, quase todos os dias.","In the United States, I was, and still am, thanked for my service. By strangers, on the street, almost every day.")}
{t("p","Aqui, vejo quem protege o país — militares, policiais, bombeiros — sem esse reconhecimento. E alguns deles, presos. Isso é terrível.","Here, I see those who protect the country — service members, police officers, firefighters — without that recognition. And some of them in prison. That is terrible.")}
{t("p","Não sou paraquedista, mas servi ao lado deles. Sei que ninguém salta de um avião, arriscando a própria vida, pelo adicional de periculosidade. Salta pelo país.","I'm not a paratrooper, but I served alongside them. I know no one jumps out of an aircraft, risking their life, for hazard pay. They jump for their country.")}
<svg class="chute" viewBox="0 0 60 60" aria-hidden="true"><path d="M6 26C6 12 18 4 30 4s24 8 24 22M6 26c4-3 8-3 12 0 4-3 8-3 12 0 4-3 8-3 12 0 4-3 8-3 12 0M6 26l22 22M18 26l10 22M42 26l-10 22M54 26L32 48"/><circle cx="30" cy="52" r="4"/></svg>
<blockquote class="verse">{t("p","Depois disto, ouvi a voz do Senhor, que dizia: A quem enviarei, e quem há de ir por nós? Então, disse eu: eis-me aqui, envia-me a mim.","Also I heard the voice of the Lord, saying, Whom shall I send, and who will go for us? Then said I, Here am I; send me.")}{t("cite","Isaías 6:8","Isaiah 6:8")}</blockquote>
<blockquote class="verse">{t("p","Ninguém tem maior amor do que este: de dar alguém a sua vida pelos seus amigos.","Greater love hath no man than this, that a man lay down his life for his friends.")}{t("cite","João 15:13","John 15:13")}</blockquote>
{t("p","Esta página não é sobre mim. É sobre liberdade, respeito e apreço por eles.","This page is not about me. It is about freedom, respect and appreciation for them.","lead")}
<div class="pair">
{fig("recruit-1997.webp",640,625,"1997, recruta","1997, recruit","Retrato de recruta da Marinha dos EUA, 1997","U.S. Navy recruit portrait, 1997")}
{fig("memorial-2025.webp",300,560,"2025, Memorial Day","2025, Memorial Day","De uniforme de gala azul no Memorial Day de 2025","In dress blues on Memorial Day 2025")}
</div>
<p class="arrow" aria-hidden="true">1997 → 2025</p>
</section>

<section>
{h2("person","Quem sou","Who I am")}
{t("p","Sergio Schickler, Chief Petty Officer (ETC) da Marinha dos EUA, na reserva. Fui técnico de comunicações em apoio à guerra especial naval, no Iraque e no Afeganistão. Brasileiro e americano.","Sergio Schickler, retired U.S. Navy Chief Petty Officer (ETC). I was a communications technician supporting naval special warfare, in Iraq and Afghanistan. Brazilian and American.")}
{TL}
{t("p","Servi sob quatro presidentes, de dois partidos. Jurei lealdade à Constituição, não a um governante.","I served under four presidents, from two parties. I swore loyalty to the Constitution, not to a ruler.","quote")}
<div class="pair">
{fig("headset-2008.webp",900,674,"2008, comunicações","2008, communications","No rádio, de capacete e headset, 2008","On the radio in helmet and headset, 2008")}
{fig("cpo-2019.webp",900,601,"2019, cerimônia de aposentadoria de um amigo","2019, a friend's retirement ceremony","De uniforme de gala diante das bandeiras, na cerimônia de aposentadoria de um amigo, 2019","In dress uniform before the flags at a friend's retirement ceremony, 2019")}
</div>
{t("p",'Histórico verificável, com o DD-214: <a href="https://shadowbox.shklr.org">shadowbox.shklr.org</a>','Verifiable record, including the DD-214: <a href="https://shadowbox.shklr.org">shadowbox.shklr.org</a>',"note",True)}
</section>

<section id="peco">
{h2("scale","O que peço","What I ask")}
{t("p",OBJ_PT,OBJ_EN,"lead")}
{t("p",'Não reconheço como imparcial nem legítimo o julgamento conduzido por quem tem interesse no resultado. Peço a anulação, pelo mesmo critério que anulou as condenações do atual presidente: juiz parcial não julga.',"I do not recognize as impartial or legitimate a trial conducted by those with a stake in its outcome. I ask for annulment, by the same standard that annulled the current president's convictions: a biased judge cannot judge.","lead")}
<ul class="list">
{t("li","Devido processo legal, com amplo direito de defesa e juízes imparciais.","Due process, with the full right to a defense and impartial judges.")}
{t("li","Proporcionalidade: prisão domiciliar para maiores de 70 anos com problemas de saúde, como a lei já prevê.","Proportionality: house arrest for people over 70 with health problems, as the law already provides.")}
{t("li","Fiscalização institucional: freios e contrapesos que valham para todos os Poderes.","Institutional oversight: checks and balances that apply to every branch.")}
</ul>
{t("p","Tudo isso pelos meios legais e sem violência. Não apoio nenhum ato ilegal nem agressão a quem quer que seja.","All of this through legal means and without violence. I support no illegal act and no aggression against anyone.")}
{t("p","Quem fiscaliza quem julga?","Who oversees those who judge?","ask")}
</section>

<section id="palavras">
{h2("play","Nas palavras dele","In his own words")}
<div class="yt" data-id="AkvPuvjwfdA" data-start="0"><button type="button" class="ytb" data-label-pt="Reproduzir vídeo: Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso (carrega o YouTube)" data-label-en="Play video: Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso (loads YouTube)" aria-label="Reproduzir vídeo: Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso (carrega o YouTube)"><img src="photos/video-AkvPuvjwfdA.webp" width="480" height="270" alt="" loading="lazy" decoding="async"><svg viewBox="0 0 68 48" aria-hidden="true"><path d="M66.5 7.7A8.6 8.6 0 0 0 60.5 1.6C55.2.2 34 .2 34 .2S12.8.2 7.5 1.6a8.6 8.6 0 0 0-6 6.1C.1 13 .1 24 .1 24s0 11 1.4 16.3a8.6 8.6 0 0 0 6 6.1C12.8 47.8 34 47.8 34 47.8s21.2 0 26.5-1.4a8.6 8.6 0 0 0 6-6.1C67.9 35 67.9 24 67.9 24s0-11-1.4-16.3z" fill="#c4302b"/><path d="M45 24 27 14v20z" fill="#fff"/></svg></button></div>
<blockquote class="verse">{t("p","“[...] A ideia do outro: ‘eu quero ganhar a eleição para tirar meu pai da cadeia’. E eu quero ganhar para manter ele na cadeia.”","“[...] The other guy's idea is: ‘I want to win the election to get my father out of jail.’ And I want to win to keep him in jail.”")}</blockquote>
{t("p","Fonte: Correio Braziliense, YouTube. “Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso”","Source: Correio Braziliense, YouTube. “Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso” (“In Santa Catarina, Lula says he wants to win the elections to keep Jair Bolsonaro in prison”)","note")}
{t("p","Prisão é decisão da Justiça. Por que depende da eleição?","Imprisonment is a decision for the courts. Why does it depend on an election?","ask")}
<div class="yt" data-id="79V-n4Q5gbQ" data-start="34"><button type="button" class="ytb" data-label-pt="Reproduzir vídeo: Lula diz na TV Globo que ministros do STF não estão acima da lei e defende reforma do Judiciário (carrega o YouTube)" data-label-en="Play video: Lula diz na TV Globo que ministros do STF não estão acima da lei e defende reforma do Judiciário (loads YouTube)" aria-label="Reproduzir vídeo: Lula diz na TV Globo que ministros do STF não estão acima da lei e defende reforma do Judiciário (carrega o YouTube)"><img src="photos/video-79V-n4Q5gbQ.webp" width="480" height="270" alt="" loading="lazy" decoding="async"><svg viewBox="0 0 68 48" aria-hidden="true"><path d="M66.5 7.7A8.6 8.6 0 0 0 60.5 1.6C55.2.2 34 .2 34 .2S12.8.2 7.5 1.6a8.6 8.6 0 0 0-6 6.1C.1 13 .1 24 .1 24s0 11 1.4 16.3a8.6 8.6 0 0 0 6 6.1C12.8 47.8 34 47.8 34 47.8s21.2 0 26.5-1.4a8.6 8.6 0 0 0 6-6.1C67.9 35 67.9 24 67.9 24s0-11-1.4-16.3z" fill="#c4302b"/><path d="M45 24 27 14v20z" fill="#fff"/></svg></button></div>
<blockquote class="verse">{t("p","“Era o mais implicado. O Toffoli também está implicado, o André Mendonça também está implicado e o Kassio está implicado. Agora está todo mundo implicado.”","“He was the most implicated. Toffoli is implicated too, André Mendonça is implicated too, and Kassio is implicated. Now everyone is implicated.”")}</blockquote>
{t("p","Na entrevista ao Jornal Nacional (15/10/2026), o presidente afirmou que vários ministros do STF estão implicados no caso Master. Implicados têm imparcialidade?","In his Jornal Nacional interview (Oct 15, 2026), the president said several Supreme Court justices are implicated in the Banco Master case. Can those implicated be impartial?","ask")}
<p class="note">{t("span","Fonte: Estadão (recorte) · ","Source: Estadão (clip) · ")}<a href="https://g1.globo.com/jornal-nacional/noticia/2026/10/15/lula-pt-e-entrevistado-na-globo-veja-integra.ghtml" rel="noopener">{t("span","íntegra no g1","full interview on g1")}</a></p>
</section>

<section>
{h2("shield","Declaração","Statement")}
{t("p","Sem partido. Sem cargo. Sem dinheiro. Sem interesse pessoal.","No party. No office. No money. No personal interest.","lead")}
</section>

<section>
{h2("terminal","Carta aos profissionais de TI do serviço público","Letter to public-sector IT professionals")}
{t("p","Vocês conhecem os sistemas que fazem o Estado funcionar melhor do que ninguém. Sabem que cada log, cada acesso e cada ordem deixa um rastro. Por isso, sabem também a diferença entre um procedimento legítimo e um abuso.","You know the systems that keep the State running better than anyone. You know that every log, every access and every order leaves a trail. So you also know the difference between a legitimate procedure and an abuse.")}
{t("p","Não peço que desliguem nada, nem que tomem nenhum dado. Peço o que a ética da profissão já exige. Recusem ordens manifestamente ilegais. Exijam que tudo seja documentado e formalizado por escrito. Quando virem uma irregularidade, levem-na pelos canais legais: ouvidorias, Ministério Público, Tribunal de Contas da União, a sua entidade de classe.","I am not asking you to shut anything down, or to take any data. I ask for what the ethics of the profession already require. Refuse manifestly illegal orders. Insist that everything be documented and formalized in writing. When you see an irregularity, take it through legal channels: ombudsman offices, the Public Prosecutor's Office, the Federal Court of Accounts (TCU), your professional association.")}
{t("p","A integridade de um sistema depende da integridade de quem o opera. Contamos com a sua consciência, não com o seu teclado.","A system's integrity depends on the integrity of those who operate it. We count on your conscience, not your keyboard.","lead")}
{t("p","Lei 8.112/90, art. 116, IV: é dever do servidor cumprir as ordens superiores, exceto quando manifestamente ilegais.","Law 8.112/90, art. 116, IV: a federal civil servant must follow superior orders, except when manifestly illegal.","note")}
</section>

<section>
{h2("quote","Slogans","Slogans")}
<ul class="grid">{grid}</ul>
</section>

<section>
{h2("mail","Imprensa","Press")}
{t("p",'Contato: <a href="mailto:sergio@shklr.org">sergio@shklr.org</a>','Contact: <a href="mailto:sergio@shklr.org">sergio@shklr.org</a>',"",True)}
<!-- TODO: press kit (high-res photos) pending Sergio's approval. -->
{t("p","Kit de imprensa: em breve.","Press kit: coming soon.","note")}
</section>
</main>
<footer>{t("p","Campanha independente e virtual. Sem partido, sem financiamento.","Independent, virtual campaign. No party, no funding.")}{t("p","As fotos de uniforme são do período de serviço ativo (1997–2018), exceto a de 2025, tirada já na reserva, no Memorial Day, ocasião em que o uso é permitido a aposentados. Esta página expressa apenas opiniões pessoais e não representa nem tem endosso da Marinha dos EUA, do Departamento de Defesa ou do governo dos EUA.","Photos in uniform are from my active service (1997–2018), except the 2025 photo, taken as a retiree on Memorial Day, when retirees are permitted to wear it. This page reflects personal views only and is not endorsed by the U.S. Navy, the Department of Defense, or the U.S. Government.","lic")}<p class="lic"><a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license noopener">{t("span","© 2026 Sergio Schickler · Textos e fotos (exceto onde indicado): CC BY-NC-ND 4.0","© 2026 Sergio Schickler · Text and photos (unless otherwise noted): CC BY-NC-ND 4.0")}</a></p>{t("p","Uso indevido de imagem ou texto, incluindo montagens e alterações, está sujeito às medidas previstas na Lei 9.610/98 (direitos autorais) e no art. 20 do Código Civil (direito de imagem).","Misuse of images or text, including edits or alterations, may be subject to legal action under copyright and image-rights law.","lic")}</footer>
'''
tpl=open('template.html').read()
open('index.html','w').write(tpl.replace('<!--BODY-->',body))
