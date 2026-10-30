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
'anchor':'<circle cx="12" cy="5" r="2"/><path d="M12 7v14M8 11h8M5 14c0 4 3 7 7 7s7-3 7-7"/>',
}
def ic(n): return f'<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{ICON[n]}</svg>'
def h2(n,pt,en): return f'<div class="sh">{ic(n)}{t("h2",pt,en)}</div>'
def fig(src,w,h,pt,en,altpt,alten):
    return f'<figure><img src="photos/{src}" width="{w}" height="{h}" loading="lazy" decoding="async" data-alt-pt="{html.escape(altpt)}" data-alt-en="{html.escape(alten)}" alt="{html.escape(altpt)}">{t("figcaption",pt,en)}</figure>'
DIV='<svg class="div" viewBox="0 0 200 20" aria-hidden="true"><path d="M0 10h80M120 10h80"/><path d="M100 3l2 5h5l-4 3 2 5-5-3-5 3 2-5-4-3h5z"/></svg>'
OBJ_PT='Liberdade imediata para Bolsonaro e os militares presos, e aplicação já da dosimetria aprovada para os demais.'
OBJ_EN='Immediate freedom for Bolsonaro and the imprisoned servicemembers, and immediate application of the already-approved sentencing reduction (dosimetria) for the others.'
slog=[('Logs não mentem.',"Logs don't lie."),('Rollback da consciência não existe.','There is no rollback for a conscience.'),('Sem ordem por escrito, sem deploy.','No written order, no deploy.'),('Não repúdio.','Non-repudiation.'),('Integridade é o melhor firewall.','Integrity is the best firewall.'),('Problema de usuário ou de sistema?','User problem or system problem?'),('Daqui a 4 anos, onde estará sua consciência?','Four years from now, where will your conscience be?'),('O silêncio também é uma escolha.','Silence is also a choice.'),('Meu juramento foi à Constituição. O seu também.','My oath was to the Constitution. So was yours.'),('Justiça sem devido processo não é justiça.','Justice without due process is not justice.')]
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
{t("p","Status da sua consciência?","Your conscience's status?","status")}
{DIV}
{t("h1","Liberdade","Freedom")}
{t("p",OBJ_PT,OBJ_EN,"obj")}
{t("p","Pela lei, sem violência. Com respeito a quem serve e protege.","Through the law, without violence. With respect for those who serve and protect.","sub")}
</section>

<section>
{h2("heart","Respeito a quem serve","Respect for those who serve")}
{LAUREL}
{t("p","Nos Estados Unidos, fui — e ainda sou — agradecido pelo meu serviço. Por estranhos, na rua, quase todos os dias.","In the United States I was, and still am, thanked for my service. By strangers, on the street, almost every day.")}
{t("p","Aqui, vejo quem protege o país — militares, policiais, bombeiros — sem esse reconhecimento. E alguns deles, presos. Isso é terrível.","Here, I see those who protect the country — servicemembers, police officers, firefighters — without that recognition. And some of them in prison. That is terrible.")}
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
{t("p","Servi sob 4 presidentes, de dois partidos. Jurei lealdade à Constituição, não a um governante.","I served under 4 presidents, from two parties. I swore loyalty to the Constitution, not to a ruler.","quote")}
<div class="pair">
{fig("headset-2008.webp",900,674,"2008, comunicações","2008, communications","No rádio, de capacete e headset, 2008","On the radio in helmet and headset, 2008")}
{fig("cpo-2019.webp",900,601,"2019, cerimônia de Chief","2019, Chief ceremony","De uniforme de gala diante das bandeiras, cerimônia de Chief, 2019","In dress uniform before the flags at a Chief ceremony, 2019")}
</div>
{t("p",'Histórico verificável, com o DD-214: <a href="https://shadowbox.shklr.org">shadowbox.shklr.org</a>','Verifiable record, including the DD-214: <a href="https://shadowbox.shklr.org">shadowbox.shklr.org</a>',"note",True)}
</section>

<section>
{h2("scale","O que peço","What I ask")}
{t("p",OBJ_PT,OBJ_EN,"lead")}
<ul class="list">
{t("li","Devido processo legal, com amplo direito de defesa e juízes imparciais.","Due process, with full right of defense and impartial judges.")}
{t("li","Proporcionalidade: prisão domiciliar para maiores de 70 anos com problemas de saúde, como a lei já prevê.","Proportionality: house arrest for people over 70 with health problems, as the law already provides.")}
{t("li","Fiscalização institucional: freios e contrapesos que valham para todos os Poderes.","Institutional oversight: checks and balances that apply to every branch.")}
</ul>
{t("p","Tudo isso pelos meios legais e sem violência. Não apoio nenhum ato ilegal, nem agressão a ninguém.","All of this through legal means and without violence. I support no illegal act and no aggression against anyone.")}
{t("p","Quem fiscaliza quem julga?","Who oversees those who judge?","ask")}
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
<footer>{t("p","Campanha independente e virtual. Sem partido, sem financiamento.","Independent, virtual campaign. No party, no funding.")}</footer>
'''
tpl=open('template.html').read()
open('index.html','w').write(tpl.replace('<!--BODY-->',body))
