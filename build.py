import html
def t(tag,pt,en,cls='',raw=False):
    a=f' class="{cls}"' if cls else ''
    h=' data-html' if raw else ''
    return f'<{tag}{a}{h} data-pt="{html.escape(pt)}" data-en="{html.escape(en)}">{pt}</{tag}>'
# Icons: Lucide v1.65.0 (lucide-static), ISC license, https://lucide.dev
ICON={
'chevron-down':'<path d="m6 9 6 6 6-6"/>',
'person':'<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
'heart':'<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/>',
'scale':'<path d="M12 3v18"/><path d="m19 8 3 8a5 5 0 0 1-6 0zV7"/><path d="M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1"/><path d="m5 8 3 8a5 5 0 0 1-6 0zV7"/><path d="M7 21h10"/>',
'shield':'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
'terminal':'<path d="m7 11 2-2-2-2"/><path d="M11 13h4"/><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/>',
'quote':'<path d="M16 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z"/><path d="M5 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z"/>',
'mail':'<path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/><rect x="2" y="4" width="20" height="16" rx="2"/>',
'play':'<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9.003a1 1 0 0 1 1.517-.859l4.997 2.997a1 1 0 0 1 0 1.718l-4.997 2.997A1 1 0 0 1 9 14.996z"/>',
'scale':'<path d="M12 3v18"/><path d="m19 8 3 8a5 5 0 0 1-6 0zV7"/><path d="M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1"/><path d="m5 8 3 8a5 5 0 0 1-6 0zV7"/><path d="M7 21h10"/>',
'anchor':'<path d="M12 6v16"/><path d="m19 13 2-1a9 9 0 0 1-18 0l2 1"/><path d="M9 11h6"/><circle cx="12" cy="4" r="2"/>',
'handshake':'<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.88-3.88a3 3 0 0 0-4.24 0l-.88.88a1 1 0 1 1-3-3l2.81-2.81a5.79 5.79 0 0 1 7.06-.87l.47.28a2 2 0 0 0 1.42.25L21 4"/><path d="m21 3 1 11h-2"/><path d="M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3"/><path d="M3 4h8"/>',
}
def ic(n,cls="ic",extra=' aria-hidden="true"'): return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"{extra}>{ICON[n]}</svg>'
def h2(n,pt,en): return f'<div class="sh">{ic(n)}{t("h2",pt,en)}</div>'
def fig(src,w,h,pt,en,altpt,alten):
    return f'<figure><img src="photos/{src}" width="{w}" height="{h}" loading="lazy" decoding="async" data-alt-pt="{html.escape(altpt)}" data-alt-en="{html.escape(alten)}" alt="{html.escape(altpt)}">{t("figcaption",pt,en)}</figure>'
DIV='<svg class="div" viewBox="0 0 200 20" aria-hidden="true"><path d="M0 10h80M120 10h80"/><path d="M100 3l2 5h5l-4 3 2 5-5-3-5 3 2-5-4-3h5z"/></svg>'
OBJ_PT='Liberdade para Bolsonaro e para os militares e civis presos injustamente, por motivação política.'
OBJ_EN='Freedom for Bolsonaro and for the service members and civilians unjustly imprisoned for political reasons.'
slog=[('Logs não mentem.',"Logs don't lie."),('Rollback da consciência não existe.','There is no rollback for a conscience.'),('Sem ordem por escrito, sem deploy.','No written order, no deploy.'),('Não repúdio.','Non-repudiation.'),('Integridade é o melhor firewall.','Integrity is the best firewall.'),('O silêncio também é uma escolha.','Silence is also a choice.'),('Meu juramento foi à Constituição. O seu também.','My oath was to the Constitution. So was yours.'),('Justiça sem devido processo não é justiça.','Justice without due process is not justice.')]
grid=''.join(f'<li>{t("span",p,e)}</li>' for p,e in slog)
grid+=f'<li>{t("span","Quem fiscaliza quem julga?","Who oversees those who judge?")}</li>'
TL='''<svg class="tl" viewBox="-20 0 380 110" role="img" aria-label="1997–2018"><path class="ln" d="M45 55H295"/><g class="pt"><circle cx="45" cy="55" r="7"/><circle cx="170" cy="55" r="7"/><circle cx="295" cy="55" r="7"/></g><g class="yr"><text x="45" y="33">1997</text><text x="170" y="33">2006–13</text><text x="295" y="33">2018</text></g><g class="lb"><text x="45" y="85" data-pt="Recruta" data-en="Recruit">Recruta</text><text x="170" y="85" data-pt="Iraque e Afeganistão" data-en="Iraq &amp; Afghanistan">Iraque e Afeganistão</text><text x="295" y="85" data-pt="Aposentadoria" data-en="Retirement">Aposentadoria</text></g></svg>'''
LAUREL='''<svg class="laurel" viewBox="0 0 120 60" aria-hidden="true"><path d="M60 55C35 50 20 35 18 10M60 55C85 50 100 35 102 10"/><g class="lf"><ellipse cx="24" cy="18" rx="3" ry="7" transform="rotate(-30 24 18)"/><ellipse cx="30" cy="31" rx="3" ry="7" transform="rotate(-50 30 31)"/><ellipse cx="42" cy="43" rx="3" ry="7" transform="rotate(-70 42 43)"/><ellipse cx="96" cy="18" rx="3" ry="7" transform="rotate(30 96 18)"/><ellipse cx="90" cy="31" rx="3" ry="7" transform="rotate(50 90 31)"/><ellipse cx="78" cy="43" rx="3" ry="7" transform="rotate(70 78 43)"/></g><path d="M60 14l3 7h7l-6 4 2 7-6-4-6 4 2-7-6-4h7z" class="st"/></svg>'''
body=f'''
<header class="top"><span class="brand"><span class="badge-ic" aria-hidden="true">{ic("scale")}</span>Liberdade</span>
<div class="lang" role="group" aria-label="Idioma / Language"><button type="button" data-set="pt" aria-pressed="true">PT</button><button type="button" data-set="en" aria-pressed="false">EN</button></div></header>
<section class="intro" aria-labelledby="intro-q">
<div class="pin">
<div class="ibg" aria-hidden="true"><img src="photos/justica-1080.webp" srcset="photos/justica-640.webp 640w, photos/justica-1080.webp 1080w, photos/justica-1600.webp 1600w" sizes="100vw" width="1080" height="1440" alt="" decoding="async" fetchpriority="high"></div>
<div class="stage">
<p class="q3" id="intro-q"><span class="s s1 ok">200</span><span class="s s2 or" data-pt="OU" data-en="OR">OU</span><span class="s s3 no">403<span class="q">?</span></span></p>
<div class="s s4 legend">{t("p","200 OK: acesso permitido.","200 OK: access granted.","lg1")}{t("p","403 Forbidden: acesso negado.","403 Forbidden: access denied.","lg1")}{t("p","Na internet, respostas de um servidor. Aqui, uma pergunta:","Online, a server’s replies. Here, a question:","lg2")}</div>
<p class="s s5 rule" data-pt="A regra tem de valer para todos." data-en="The rule must apply to everyone.">A regra tem de valer para todos.</p>
</div>
<p class="cue" aria-hidden="true"><span data-pt="Role para baixo" data-en="Scroll">Role para baixo</span>{ic("chevron-down")}</p>
<p class="icredit">{t("span","Escultura “A Justiça”, de Alfredo Ceschiatti. Foto: Morio, CC BY-SA 3.0 (tonalizada)","Sculpture “A Justiça” by Alfredo Ceschiatti. Photo: Morio, CC BY-SA 3.0 (toned)")} · <a href="https://commons.wikimedia.org/wiki/File:A_Justica_Alfredo_Ceschiatti_Brasilia_Brasil.jpg" target="_blank" rel="noopener">Wikimedia Commons</a></p>
</div>
</section>
<main class="wrap">
<section class="hero">
{DIV}
{t("h1","Liberdade","Freedom")}
{t("p",OBJ_PT,OBJ_EN,"obj")}
{t("p","Pela lei, sem violência. Com respeito a quem serve e protege.","Through the law, without violence. With respect for those who serve and protect.","sub")}
</section>

<section id="quem">
{h2("person","Quem sou","Who I am")}
{t("p","Sergio Schickler, Chief Petty Officer (ETC) aposentado da Marinha dos EUA. Técnico de comunicações, com mais de 7 anos em apoio à Guerra Especial Naval, incluindo missões no Iraque e no Afeganistão. Não fui operador; fui quem mantinha a comunicação funcionando. Cidadão brasileiro e americano.","Sergio Schickler, retired U.S. Navy Chief Petty Officer (ETC). Communications technician, with 7+ years supporting Naval Special Warfare, including deployments to Iraq and Afghanistan. I was not an operator; I kept the communications running. Brazilian and U.S. citizen.")}
{TL}
{t("p","Servi sob quatro presidentes, de dois partidos. Jurei lealdade à Constituição, não a um governante.","I served under four presidents, from two parties. I swore loyalty to the Constitution, not to a ruler.","quote")}
<div class="pair">
{fig("headset-2008.webp",900,674,"2009, treinamento de comboio (simulação), Fort Bliss","2009, convoy training (simulation), Fort Bliss","No rádio, de capacete e headset, em simulação de treinamento de comboio em Fort Bliss, 2009","On the radio in helmet and headset during a convoy training simulation at Fort Bliss, 2009")}
{fig("cpo-2019.webp",900,601,"2019, cerimônia de aposentadoria de um amigo","2019, a friend's retirement ceremony","De uniforme de gala diante das bandeiras, na cerimônia de aposentadoria de um amigo, 2019","In dress uniform before the flags at a friend's retirement ceremony, 2019")}
</div>
{t("p",'Histórico verificável, com o DD-214: <a href="https://shadowbox.shklr.org">shadowbox.shklr.org</a>','Verifiable record, including the DD-214: <a href="https://shadowbox.shklr.org">shadowbox.shklr.org</a>',"note",True)}
</section>

<section id="respeito">
{h2("heart","Respeito a quem serve","Respect for those who serve")}
{ic("handshake","hand",' role="img" aria-label="Aperto de mãos" data-label-pt="Aperto de mãos" data-label-en="Handshake"')}
{t("p","Nos Estados Unidos, fui — e ainda sou — agradecido pelo meu serviço. Por estranhos, na rua, quase todos os dias.","In the United States, I was, and still am, thanked for my service. By strangers, on the street, almost every day.")}
{t("p","Aqui, vejo quem protege o país — militares, policiais, bombeiros — sem esse reconhecimento. E alguns deles, presos.","Here, I see those who protect the country — service members, police officers, firefighters — without that recognition. And some of them in prison.")}
{t("p","Não sou paraquedista, mas servi ao lado deles. Ninguém salta de um avião pelo adicional de periculosidade. Salta pelo país.","I'm not a paratrooper, but I served alongside them. No one jumps out of an aircraft for hazard pay. They jump for their country.")}
<svg class="chute" viewBox="0 0 60 60" aria-hidden="true"><path d="M6 26C6 12 18 4 30 4s24 8 24 22M6 26c4-3 8-3 12 0 4-3 8-3 12 0 4-3 8-3 12 0 4-3 8-3 12 0M6 26l22 22M18 26l10 22M42 26l-10 22M54 26L32 48"/><circle cx="30" cy="52" r="4"/></svg>
<blockquote class="verse">{t("p","Depois disto, ouvi a voz do Senhor, que dizia: A quem enviarei, e quem há de ir por nós? Então, disse eu: eis-me aqui, envia-me a mim.","Also I heard the voice of the Lord, saying, Whom shall I send, and who will go for us? Then said I, Here am I; send me.")}{t("cite","Isaías 6:8","Isaiah 6:8")}</blockquote>
<blockquote class="verse">{t("p","Ninguém tem maior amor do que este: de dar alguém a sua vida pelos seus amigos.","Greater love hath no man than this, that a man lay down his life for his friends.")}{t("cite","João 15:13","John 15:13")}</blockquote>
<div class="pair">
{fig("recruit-1997.webp",640,625,"1997, recruta","1997, recruit","Retrato de recruta da Marinha dos EUA, 1997","U.S. Navy recruit portrait, 1997")}
{fig("memorial-2025.webp",300,560,"2025, Memorial Day","2025, Memorial Day","De uniforme de gala azul no Memorial Day de 2025","In dress blues on Memorial Day 2025")}
</div>
<p class="arrow" aria-hidden="true">1997 → 2025</p>
</section>

<section id="peco">
{h2("scale","O que peço","What I ask")}
{t("p","Peço a anulação dos julgamentos conduzidos por quem tem interesse no resultado, pelo mesmo critério que anulou as condenações do atual presidente: juiz parcial não julga.","I ask for the annulment of trials conducted by those with a stake in the outcome, by the same standard that annulled the current president's convictions: a biased judge cannot judge.","lead")}
<ul class="list">
{t("li","Devido processo legal, com amplo direito de defesa e juízes imparciais.","Due process, with the full right to a defense and impartial judges.")}
{t("li","Fiscalização institucional: freios e contrapesos que valham para todos os Poderes.","Institutional oversight: checks and balances that apply to every branch.")}
</ul>
{t("p","Não defendo pessoas. Defendo o serviço e a honestidade jurídica. Não vou entrar em questões sobre minha vida pessoal: minha reivindicação é jurídica.","I am not defending individuals. I am defending service and legal integrity. I will not engage with questions about my personal life: my claim is a legal one.")}
{t("p","Se a suspeição do juiz anulou uma condenação, por que não anularia outra? A regra tem de valer para todos.","If a judge's bias voided one conviction, why wouldn't it void another? The rule must apply to everyone.")}
{t("p",'Fonte: <a href="https://noticias.stf.jus.br/postsnoticias/2a-turma-reconhece-parcialidade-de-ex-juiz-sergio-moro-na-condenacao-de-lula-no-caso-triplex/" target="_blank" rel="noopener">STF, HC 164.493</a>','Source: <a href="https://noticias.stf.jus.br/postsnoticias/2a-turma-reconhece-parcialidade-de-ex-juiz-sergio-moro-na-condenacao-de-lula-no-caso-triplex/" target="_blank" rel="noopener">STF, HC 164.493</a>',"note",True)}
{t("p","Pelos meios legais e sem violência. Não apoio nenhum ato ilegal nem agressão a ninguém. Não temo represálias; sigo pela via legal e pacífica.","Through legal means, without violence. I support no illegal act and no aggression against anyone. I do not fear reprisals; I stay on the lawful, peaceful path.")}
{t("p","Uma presença pacífica em Brasília continua sendo uma opção.","A peaceful presence in Brasília remains an option.")}
</section>

<section id="palavras">
{h2("play","Nas palavras dele","In his own words")}
<div class="yt" data-id="AkvPuvjwfdA" data-start="0"><button type="button" class="ytb" data-label-pt="Reproduzir vídeo: Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso (carrega o YouTube)" data-label-en="Play video: Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso (loads YouTube)" aria-label="Reproduzir vídeo: Em SC, Lula diz que quer ganhar as eleições para manter Jair Bolsonaro preso (carrega o YouTube)"><img src="photos/video-AkvPuvjwfdA.webp" width="480" height="270" alt="" loading="lazy" decoding="async"><svg viewBox="0 0 68 48" aria-hidden="true"><path d="M66.5 7.7A8.6 8.6 0 0 0 60.5 1.6C55.2.2 34 .2 34 .2S12.8.2 7.5 1.6a8.6 8.6 0 0 0-6 6.1C.1 13 .1 24 .1 24s0 11 1.4 16.3a8.6 8.6 0 0 0 6 6.1C12.8 47.8 34 47.8 34 47.8s21.2 0 26.5-1.4a8.6 8.6 0 0 0 6-6.1C67.9 35 67.9 24 67.9 24s0-11-1.4-16.3z" fill="#c4302b"/><path d="M45 24 27 14v20z" fill="#fff"/></svg></button></div>
<blockquote class="verse">{t("p","“[...] A ideia do outro: ‘eu quero ganhar a eleição para tirar meu pai da cadeia’. E eu quero ganhar para manter ele na cadeia.”","“[...] The other guy's idea is: ‘I want to win the election to get my father out of jail.’ And I want to win to keep him in jail.”")}</blockquote>
{t("p","Fonte: Correio Braziliense, YouTube (discurso em Santa Catarina)","Source: Correio Braziliense, YouTube (speech in Santa Catarina)","note")}
{t("p","Prisão é decisão da Justiça. Por que depende da eleição?","Imprisonment is a decision for the courts. Why does it depend on an election?","ask")}
<div class="yt" data-id="79V-n4Q5gbQ" data-start="34"><button type="button" class="ytb" data-label-pt="Reproduzir vídeo: Lula diz na TV Globo que ministros do STF não estão acima da lei e defende reforma do Judiciário (carrega o YouTube)" data-label-en="Play video: Lula diz na TV Globo que ministros do STF não estão acima da lei e defende reforma do Judiciário (loads YouTube)" aria-label="Reproduzir vídeo: Lula diz na TV Globo que ministros do STF não estão acima da lei e defende reforma do Judiciário (carrega o YouTube)"><img src="photos/video-79V-n4Q5gbQ.webp" width="480" height="270" alt="" loading="lazy" decoding="async"><svg viewBox="0 0 68 48" aria-hidden="true"><path d="M66.5 7.7A8.6 8.6 0 0 0 60.5 1.6C55.2.2 34 .2 34 .2S12.8.2 7.5 1.6a8.6 8.6 0 0 0-6 6.1C.1 13 .1 24 .1 24s0 11 1.4 16.3a8.6 8.6 0 0 0 6 6.1C12.8 47.8 34 47.8 34 47.8s21.2 0 26.5-1.4a8.6 8.6 0 0 0 6-6.1C67.9 35 67.9 24 67.9 24s0-11-1.4-16.3z" fill="#c4302b"/><path d="M45 24 27 14v20z" fill="#fff"/></svg></button></div>
<blockquote class="verse">{t("p","“Era o mais implicado. O Toffoli também está implicado, o André Mendonça também está implicado e o Kassio está implicado. Agora está todo mundo implicado.”","“He was the most implicated. Toffoli is implicated too, André Mendonça is implicated too, and Kassio is implicated. Now everyone is implicated.”")}</blockquote>
{t("p","Na entrevista ao Jornal Nacional (15/10/2026), o presidente afirmou que vários ministros do STF estão implicados no caso Master. Implicados têm imparcialidade?","In his Jornal Nacional interview (Oct 15, 2026), the president said several Supreme Court justices are implicated in the Banco Master case. Can those implicated be impartial?","ask")}
<p class="note">{t("span","Fonte: Estadão (recorte) · ","Source: Estadão (clip) · ")}<a href="https://g1.globo.com/jornal-nacional/noticia/2026/10/15/lula-pt-e-entrevistado-na-globo-veja-integra.ghtml" rel="noopener">{t("span","íntegra no g1","full interview on g1")}</a></p>
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
</section>
</main>
<footer>{t("p","Campanha independente e virtual. Sem partido, sem cargo, sem financiamento.","Independent, virtual campaign. No party, no office, no funding.")}{t("p","Fotos de uniforme: serviço ativo (1997–2018), exceto a de 2025 (Memorial Day, uso permitido a aposentados). Esta página expressa apenas opiniões pessoais e não representa nem tem endosso da Marinha dos EUA, do Departamento de Guerra ou do governo dos EUA.","Uniform photos: active service (1997–2018), except 2025 (Memorial Day, when retirees may wear it). This page reflects personal views only and is not endorsed by the U.S. Navy, the Department of War, or the U.S. Government.","lic")}<div class="social">{t("p","Perfis oficiais","Official profiles","social-h")}<div class="social-row"><a href="https://x.com/sergioshklr" rel="me noopener" target="_blank" aria-label="X (@sergioshklr)" title="X"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z"/></svg></a><a href="https://www.instagram.com/sergio.shklr" rel="me noopener" target="_blank" aria-label="Instagram (@sergio.shklr)" title="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077"/></svg></a><a href="https://www.youtube.com/@sergioshklr" rel="me noopener" target="_blank" aria-label="YouTube (@sergioshklr)" title="YouTube"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a><a href="https://www.tiktok.com/@sergioshklr" rel="me noopener" target="_blank" aria-label="TikTok (@sergioshklr)" title="TikTok"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg></a><a href="https://t.me/sergioshklr" rel="me noopener" target="_blank" aria-label="Telegram (@sergioshklr)" title="Telegram"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg></a></div></div><p class="lic"><a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license noopener">{t("span","© 2026 Sergio Schickler · Textos e fotos (exceto onde indicado): CC BY-NC-ND 4.0","© 2026 Sergio Schickler · Text and photos (unless otherwise noted): CC BY-NC-ND 4.0")}</a></p>{t("p","Uso indevido de imagem ou texto, incluindo montagens e alterações, está sujeito às medidas previstas na Lei 9.610/98 (direitos autorais) e no art. 20 do Código Civil (direito de imagem).","Misuse of images or text, including edits or alterations, may be subject to legal action under Brazilian copyright law (Law 9.610/98) and image rights (Civil Code, art. 20).","lic")}</footer>
'''
tpl=open('template.html').read()
open('index.html','w').write(tpl.replace('<!--BODY-->',body))
