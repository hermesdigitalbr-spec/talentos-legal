#!/usr/bin/env python3
"""Gera as páginas estáticas (CSS embutido, como nos demais repos -legal). Uso: python3 build.py"""
import pathlib
ROOT = pathlib.Path(__file__).parent
MAIL = '<a href="mailto:support@hermes.com.br">support@hermes.com.br</a>'
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
CSS = """
:root{
  --ground:#FBF6EC; --surface:#FFFFFF; --sunken:#F1E8D6;
  --ink:#2E2A24; --brand:#A94E2D; --accent:#A94E2D;
  --text2:#5E554A; --faint:#7A6F60; --hairline:rgba(46,42,36,.12);
  --serif:ui-serif,"New York","Iowan Old Style",Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);
  font-size:16.5px;line-height:1.62;padding:0 22px 90px;-webkit-font-smoothing:antialiased}
.wrap{max-width:40rem;margin:0 auto}
.lang{text-align:right;padding-top:18px;font-size:13px}
header{position:relative;padding:40px 0 26px;text-align:center}
header::before{content:"";position:absolute;left:50%;top:-10px;transform:translateX(-50%);
  width:190px;height:190px;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle at 40% 35%, rgba(217,164,65,.30), rgba(217,164,65,0) 62%),
    radial-gradient(circle at 62% 60%, rgba(199,96,58,.20), rgba(199,96,58,0) 62%);
  filter:blur(26px)}
.brand{position:relative;font-family:var(--serif);font-size:23px;letter-spacing:.01em;color:var(--brand)}
h1{position:relative;font-family:var(--serif);font-size:clamp(31px,8vw,40px);font-weight:500;
  line-height:1.12;letter-spacing:-.015em;margin:12px 0 8px;text-wrap:balance}
.updated{position:relative;font-size:13px;color:var(--faint);margin:0}
.rule{height:1px;background:var(--hairline);margin:6px 0 4px}
h2{font-family:var(--serif);font-size:20.5px;font-weight:500;letter-spacing:-.01em;margin:38px 0 8px;color:var(--ink)}
p,li{color:var(--text2);max-width:60ch;margin:0 0 .85rem}
ul{padding-left:1.15rem;margin:.2rem 0 1rem}
li{margin:.34rem 0}
li::marker{color:var(--accent)}
strong{color:var(--ink);font-weight:640}
a{color:var(--accent);text-underline-offset:2px;text-decoration-thickness:1px}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:3px}
.card{background:var(--surface);border:1px solid var(--hairline);border-radius:16px;padding:20px 22px;
  margin:26px 0 6px;box-shadow:0 1px 2px rgba(46,42,36,.03),0 10px 30px -18px rgba(46,42,36,.16)}
.card p{margin:0}
.card.quiet{background:var(--sunken);box-shadow:none}
.docs{list-style:none;padding:0;margin:8px 0 0}
.docs li{margin:0;border-top:1px solid var(--hairline);max-width:none}
.docs li:first-child{border-top:0}
.docs a{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:15px 2px;
  text-decoration:none;font-family:var(--serif);font-size:17.5px;color:var(--ink)}
.docs a span{font-family:var(--sans);font-size:13px;color:var(--faint)}
.docs a:hover{color:var(--accent)}
footer{margin-top:52px;padding-top:20px;border-top:1px solid var(--hairline);font-size:13px;color:var(--faint);text-align:center}
footer a{color:var(--faint)}
@media (prefers-color-scheme:dark){
 :root{--ground:#1A1713; --surface:#231F19; --sunken:#2A251E; --ink:#F1E8D6; --brand:#E9C46A;
   --accent:#F0A07E; --text2:#CFC4B2; --faint:#A89A85; --hairline:rgba(241,232,214,.14)}
 .card{box-shadow:none}
}
"""
L = {
 "pt": dict(html="pt-BR", brand="Talentos", other="en", other_label="English", legal="Documentos legais",
            upd="Última atualização: 7 de outubro de 2026"),
 "en": dict(html="en", brand="Talents", other="pt", other_label="Português", legal="Legal documents",
            upd="Last updated: October 7, 2026"),
}
def page(lang, slug, title, sub, body):
    t = L[lang]
    # caminhos relativos e sem extensão: /terms, /privacy, /support, /en/...
    here = "" if lang == "pt" else "en/"
    name = "" if slug == "index" else slug
    up = "" if lang == "pt" else "../"
    other = (up + ("en/" if lang == "pt" else "") + name) or "./"
    home = "./"
    foot = "" if slug == "index" else f' · <a href="{home}">{t["legal"]}</a>'
    html = f"""<!doctype html>
<html lang="{t['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<style>{CSS}</style>
<title>{t['brand']} — {title}</title>
</head>
<body>
<div class="wrap">
<div class="lang"><a href="{other}" hreflang="{L[t['other']]['html']}">{t['other_label']}</a></div>
<header>
<div class="brand">{t['brand']}</div>
<h1>{title}</h1>
<p class="updated">{sub or t['upd']}</p>
</header>
<div class="rule"></div>
{body.strip()}

<footer>Hermes Digital · {t['brand']}{foot}</footer>
</div>
</body>
</html>
"""
    out = ROOT / here / f"{slug}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")

# ---------------------------------------------------------------- pt-BR
page("pt", "index", "Documentos legais", "Quiz bíblico · Hermes Digital", f"""
<div class="card">
<ul class="docs">
<li><a href="terms">Termos de Uso<span>ler →</span></a></li>
<li><a href="privacy">Política de Privacidade<span>ler →</span></a></li>
<li><a href="support">Suporte<span>abrir →</span></a></li>
</ul>
</div>

<h2>Suporte</h2>
<p>Dúvidas sobre o app, sua assinatura ou seus dados, escreva para {MAIL}.</p>

<div class="card quiet">
<p>O Talentos funciona no seu iPhone: sem conta, sem anúncios, e o seu progresso fica no aparelho.</p>
</div>
""")

page("pt", "support", "Suporte", "Quiz bíblico · Hermes Digital", f"""
<div class="card">
<p><strong>Fale com a gente:</strong> {MAIL}</p>
</div>

<h2>Como podemos ajudar</h2>
<p>Escreva para o e-mail acima contando o que aconteceu. Se for um problema no app, ajuda muito informar o modelo do iPhone, a versão do iOS e o que você estava fazendo na hora.</p>

<h2>Encontrou um erro em uma pergunta?</h2>
<p>Toque em “Reportar” na pergunta, dentro do app, ou escreva para {MAIL} com o texto da pergunta e a referência bíblica. Revisamos cada relato.</p>

<h2>Assinatura</h2>
<ul>
<li><strong>Cancelar:</strong> Ajustes do iPhone → seu nome → Assinaturas → Talentos. Desinstalar o app não cancela a assinatura.</li>
<li><strong>Restaurar:</strong> na tela do Premium, toque em “Restaurar compra”, usando a mesma conta Apple da compra.</li>
<li><strong>Reembolso:</strong> é a Apple quem processa, em <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
</ul>

<h2>Seus dados</h2>
<p>O progresso fica só no aparelho. Para apagar tudo, use “Apagar todos os meus dados” nos Ajustes do app, ou desinstale o app. Detalhes na <a href="privacy">Política de Privacidade</a>.</p>

<h2>Esqueci o PIN do perfil infantil</h2>
<p>O PIN fica guardado apenas no seu aparelho e não temos como recuperá-lo. Escreva para {MAIL} e orientamos o que fazer.</p>

<h2>Documentos</h2>
<ul>
<li><a href="terms">Termos de Uso</a></li>
<li><a href="privacy">Política de Privacidade</a></li>
</ul>
""")

page("pt", "privacy", "Política de Privacidade", None, f"""
<div class="card">
<p><strong>Em uma frase:</strong> o Talentos funciona no seu iPhone. Seu progresso fica no aparelho — nada é enviado para nós, não existe conta de usuário, não há anúncios e não usamos ferramentas de análise de terceiros.</p>
</div>

<h2>Quem somos</h2>
<p>O Talentos é um quiz bíblico para iPhone desenvolvido pela Hermes Digital. Contato: {MAIL}</p>

<h2>Que dados o app trata e onde ficam</h2>
<p>Tudo o que o app guarda fica no armazenamento do seu próprio aparelho:</p>
<ul>
<li><strong>Apelido</strong> que você digita para cada perfil;</li>
<li><strong>progresso de jogo</strong> — partidas, acertos e erros, talentos, sequência de dias, conquistas e trilhas;</li>
<li><strong>preferências</strong> do app e os controles do perfil infantil (tempo por dia e outras opções);</li>
<li><strong>PIN do perfil infantil</strong>, guardado no Keychain do aparelho, a área protegida do iOS.</li>
</ul>
<p>Esses dados <strong>não são enviados para nossos servidores</strong> — o Talentos não tem servidor próprio nem cadastro. Não temos acesso a eles. Dependendo dos seus ajustes, eles podem fazer parte do backup do iPhone que a Apple faz para você; esse backup é controlado pela sua conta Apple, não por nós.</p>

<h2>Sugestões e relatos de pergunta</h2>
<p>Se você sugerir uma pergunta ou relatar um erro, o app abre o seu aplicativo de e-mail com a mensagem pronta e é <strong>você</strong> quem envia. Nesse caso recebemos o que qualquer e-mail traz: seu endereço de e-mail, o nome configurado na sua conta de e-mail e o texto que você escreveu. Usamos isso só para ler, responder e melhorar o conteúdo do app. O app não envia nada sozinho.</p>

<h2>O que não coletamos</h2>
<ul>
<li>Não pedimos nome, e-mail, telefone, data de nascimento nem criação de conta.</li>
<li>Não coletamos localização, contatos, fotos, microfone ou câmera.</li>
<li>Não usamos SDKs de análise ou de publicidade de terceiros e não rastreamos você entre apps ou sites.</li>
<li>Não exibimos anúncios.</li>
<li>Não vendemos, alugamos nem compartilhamos dados pessoais.</li>
</ul>

<h2>Compras</h2>
<p>As assinaturas são vendidas e cobradas pela Apple, pela App Store. O Talentos recebe da Apple apenas a informação de que a sua assinatura está ativa, para liberar o Premium. Não vemos, não recebemos e não guardamos dados do seu cartão. O tratamento que a Apple faz dos dados de compra segue a política de privacidade dela.</p>

<h2>Notificações</h2>
<p>As notificações são opcionais e só aparecem se você permitir. Elas são <strong>locais</strong>: agendadas pelo próprio aparelho (por exemplo, o lembrete diário e o aviso de fim do teste grátis), sem passar por um servidor nosso. Você pode desligá-las a qualquer momento nos Ajustes do app ou do iPhone.</p>

<h2>Crianças</h2>
<p>O Talentos tem um <strong>perfil infantil</strong>, criado e gerenciado por um adulto responsável. O app <strong>não coleta dados pessoais de crianças</strong>: o perfil infantil usa apenas um apelido e o progresso de jogo, e ambos ficam no aparelho. Não há anúncios, nem conta, nem contato com outras pessoas no perfil infantil.</p>
<p>O responsável conta com controles: limite de tempo por dia e um PIN que protege a saída do perfil infantil e as configurações da família. Recomendamos não usar o nome completo da criança como apelido. Pais e responsáveis podem apagar os dados a qualquer momento, como descrito abaixo, e tirar dúvidas em {MAIL}.</p>

<h2>Como apagar os seus dados</h2>
<ul>
<li>Nos Ajustes do app, toque em <strong>“Apagar todos os meus dados”</strong>; ou</li>
<li>desinstale o app — os dados guardados no aparelho são removidos junto.</li>
</ul>
<p>Apagar os dados não cancela a assinatura: ela é gerenciada na sua conta Apple. Se você nos enviou um e-mail e quer que ele seja apagado, basta pedir em {MAIL}.</p>

<h2>Seus direitos (LGPD)</h2>
<p>A Lei Geral de Proteção de Dados (Lei nº 13.709/2018) garante a você, entre outros, os direitos de confirmar a existência de tratamento, acessar, corrigir, eliminar e pedir a portabilidade dos seus dados, além de obter informações sobre compartilhamento e de revogar o consentimento.</p>
<p>Como não mantemos cadastro nem identificamos você, os dados do app simplesmente não estão em nossos sistemas — você os controla diretamente no aparelho. Os únicos dados pessoais que podemos ter são os de e-mails que você nos enviou. Para qualquer solicitação, escreva para {MAIL}. Você também pode recorrer à Autoridade Nacional de Proteção de Dados (ANPD).</p>

<h2>Mudanças nesta política</h2>
<p>Se esta política mudar, atualizamos a data no topo desta página. Mudanças relevantes — por exemplo, se o app passar a ter recursos online — serão descritas aqui antes de entrarem em vigor.</p>

<h2>Vigência</h2>
<p>Esta política vale a partir de 7 de outubro de 2026.</p>
""")

page("pt", "terms", "Termos de Uso", None, f"""
<div class="card">
<p><strong>O essencial:</strong> o Talentos é um jogo de perguntas sobre a Bíblia, de caráter educativo. Há uma parte gratuita e uma assinatura Premium, vendida e cobrada pela Apple, que você cancela quando quiser nos Ajustes do iPhone.</p>
</div>

<h2>1. Aceitação</h2>
<p>Ao usar o Talentos, você concorda com estes termos. Se não concordar, não use o app. Menores de idade devem usar o app com a autorização de um responsável, que aceita estes termos em nome deles.</p>

<h2>2. Licença de uso</h2>
<p>A Hermes Digital concede a você uma licença pessoal, limitada, não exclusiva, intransferível e revogável para usar o Talentos nos aparelhos Apple que você possui ou controla, conforme as regras da App Store. O app, as perguntas, os textos, o design e a marca pertencem à Hermes Digital ou aos seus licenciantes. Você concorda em não copiar, revender, extrair o banco de perguntas, fazer engenharia reversa nem tentar burlar o app.</p>

<h2>3. Conteúdo bíblico</h2>
<p>O conteúdo do Talentos tem <strong>caráter educativo e de entretenimento</strong>. O app <strong>não tem vínculo com nenhuma igreja, denominação ou instituição religiosa</strong> e não pretende oferecer orientação doutrinária, pastoral ou espiritual. Traduções da Bíblia e tradições diferem entre si; cuidamos da precisão das perguntas e explicações, mas erros podem acontecer — se encontrar um, avise em {MAIL}.</p>

<h2>4. Assinaturas</h2>
<p>O Talentos tem uma versão gratuita e o <strong>Premium</strong>, oferecido como assinatura auto-renovável: plano <strong>mensal</strong>, plano <strong>anual</strong> e plano <strong>Família anual</strong>. Os planos anuais podem incluir um período de teste grátis de 7 dias, quando disponível para você.</p>
<ul>
<li>O preço e a periodicidade de cada plano são exibidos na tela de compra, antes da confirmação.</li>
<li>A cobrança é feita na sua conta Apple na confirmação da compra e a cada renovação.</li>
<li>A assinatura <strong>renova automaticamente</strong> ao fim de cada período, pelo mesmo preço, salvo se for cancelada com pelo menos 24 horas de antecedência do fim do período em curso.</li>
<li><strong>Teste grátis:</strong> ao fim do período de teste, a assinatura passa a ser cobrada automaticamente pelo preço exibido, a menos que você cancele com pelo menos 24 horas de antecedência do fim do teste.</li>
<li>Ofertas com preço promocional valem pelo período indicado na tela de compra; depois, a renovação segue o preço normal ali exibido.</li>
<li>Você gerencia e cancela a assinatura nos Ajustes do iPhone, em seu nome → Assinaturas. Desinstalar o app não cancela a assinatura. Após o cancelamento, o Premium continua até o fim do período já pago.</li>
<li>O plano Família pode ser usado pelos membros do seu grupo de Compartilhamento Familiar da Apple, conforme as regras da Apple.</li>
</ul>

<h2>5. Reembolsos</h2>
<p>As compras são processadas pela Apple e seguem as políticas dela. Pedidos de reembolso devem ser feitos em <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. Não temos como processar reembolsos diretamente. Nada aqui limita os direitos que a legislação de defesa do consumidor garante a você.</p>

<h2>6. Perfil infantil</h2>
<p>O perfil infantil e seus controles (tempo por dia e PIN) são uma ajuda para a família, e não substituem a supervisão de um adulto. O responsável é quem cria o perfil, define os limites e guarda o PIN.</p>

<h2>7. Sugestões de perguntas</h2>
<p>Enviar sugestões é opcional. Ao nos enviar uma sugestão de pergunta, correção ou ideia, você declara que pode compartilhá-la e nos concede uma licença gratuita, não exclusiva, mundial e por prazo indeterminado para usar, adaptar, editar e publicar esse conteúdo no Talentos e em seus materiais, sem obrigação de pagamento ou de crédito. Não somos obrigados a usar as sugestões recebidas.</p>

<h2>8. Disponibilidade</h2>
<p>Fazemos o possível para manter o app funcionando bem, mas ele é fornecido “como está”. Não garantimos funcionamento ininterrupto nem ausência de erros, e podemos alterar, acrescentar ou retirar recursos e conteúdos.</p>

<h2>9. Limitação de responsabilidade</h2>
<p>Na máxima extensão permitida em lei, a Hermes Digital não se responsabiliza por danos indiretos decorrentes do uso do app, nem pela perda de progresso guardado no aparelho (por exemplo, em caso de troca, perda ou restauração do aparelho, ou de desinstalação do app). A responsabilidade total, em qualquer hipótese, fica limitada ao valor efetivamente pago por você nos últimos doze meses.</p>

<h2>10. Apple</h2>
<p>O Talentos é distribuído pela App Store. No que estes termos não tratarem, vale o <a href="{EULA}">Contrato de Licença de Usuário Final padrão da Apple (EULA)</a>. A Apple não é parte destes termos e não é responsável pelo app nem pelo suporte a ele.</p>

<h2>11. Privacidade</h2>
<p>O tratamento de dados está descrito na <a href="privacy">Política de Privacidade</a>.</p>

<h2>12. Alterações</h2>
<p>Podemos atualizar estes termos; a data no topo indica a última revisão. O uso continuado após a atualização representa concordância.</p>

<h2>13. Contato</h2>
<p>Contato: {MAIL}</p>
""")

# ---------------------------------------------------------------- en
page("en", "index", "Legal documents", "Bible quiz · Hermes Digital", f"""
<div class="card">
<ul class="docs">
<li><a href="terms">Terms of Use<span>read →</span></a></li>
<li><a href="privacy">Privacy Policy<span>read →</span></a></li>
<li><a href="support">Support<span>open →</span></a></li>
</ul>
</div>

<h2>Support</h2>
<p>Questions about the app, your subscription or your data? Write to {MAIL}.</p>

<div class="card quiet">
<p>Talents runs on your iPhone: no account, no ads, and your progress stays on the device.</p>
</div>
""")

page("en", "support", "Support", "Bible quiz · Hermes Digital", f"""
<div class="card">
<p><strong>Get in touch:</strong> {MAIL}</p>
</div>

<h2>How we can help</h2>
<p>Write to the address above and tell us what happened. For a problem in the app, it helps to include your iPhone model, iOS version and what you were doing at the time.</p>

<h2>Found a mistake in a question?</h2>
<p>Tap “Report” on the question in the app, or write to {MAIL} with the question text and the Bible reference. We review every report.</p>

<h2>Subscription</h2>
<ul>
<li><strong>Cancel:</strong> iPhone Settings → your name → Subscriptions → Talents. Deleting the app does not cancel the subscription.</li>
<li><strong>Restore:</strong> on the Premium screen, tap “Restore purchase”, using the same Apple Account you bought with.</li>
<li><strong>Refunds:</strong> handled by Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
</ul>

<h2>Your data</h2>
<p>Your progress stays on the device only. To erase everything, use “Erase all my data” in the app's Settings, or delete the app. See the <a href="privacy">Privacy Policy</a>.</p>

<h2>Forgot the kids profile PIN</h2>
<p>The PIN is stored only on your device and we cannot recover it. Write to {MAIL} and we will guide you.</p>

<h2>Documents</h2>
<ul>
<li><a href="terms">Terms of Use</a></li>
<li><a href="privacy">Privacy Policy</a></li>
</ul>
""")

page("en", "privacy", "Privacy Policy", None, f"""
<div class="card">
<p><strong>In one sentence:</strong> Talents runs on your iPhone. Your progress stays on the device — nothing is sent to us, there is no user account, there are no ads and we use no third-party analytics.</p>
</div>

<h2>Who we are</h2>
<p>Talents is a Bible quiz for iPhone developed by Hermes Digital. Contact: {MAIL}</p>

<h2>What data the app handles and where it lives</h2>
<p>Everything the app stores is kept in your own device's storage:</p>
<ul>
<li>the <strong>nickname</strong> you type for each profile;</li>
<li><strong>game progress</strong> — games played, right and wrong answers, talents, daily streak, achievements and trails;</li>
<li>app <strong>preferences</strong> and the kids profile controls (daily time and other options);</li>
<li>the <strong>kids profile PIN</strong>, stored in the device Keychain, the protected area of iOS.</li>
</ul>
<p>This data is <strong>not sent to our servers</strong> — Talents has no server of its own and no sign-up. We have no access to it. Depending on your settings, it may be included in the iPhone backup Apple makes for you; that backup is controlled by your Apple Account, not by us.</p>

<h2>Suggestions and question reports</h2>
<p>If you suggest a question or report a mistake, the app opens your email app with a prepared message and <strong>you</strong> send it. In that case we receive what any email carries: your email address, the name set in your email account and the text you wrote. We use it only to read, reply and improve the app's content. The app never sends anything on its own.</p>

<h2>What we do not collect</h2>
<ul>
<li>We do not ask for your name, email, phone number, date of birth or an account.</li>
<li>We do not collect location, contacts, photos, microphone or camera data.</li>
<li>We use no third-party analytics or advertising SDKs and do not track you across apps or websites.</li>
<li>We show no ads.</li>
<li>We do not sell, rent or share personal data.</li>
</ul>

<h2>Purchases</h2>
<p>Subscriptions are sold and billed by Apple through the App Store. Talents only receives from Apple the information that your subscription is active, in order to unlock Premium. We never see, receive or store your card details. Apple's handling of purchase data is governed by Apple's privacy policy.</p>

<h2>Notifications</h2>
<p>Notifications are optional and only appear if you allow them. They are <strong>local</strong>: scheduled by the device itself (for example, the daily reminder and the free-trial ending notice), without going through any server of ours. You can turn them off at any time in the app's or the iPhone's Settings.</p>

<h2>Children</h2>
<p>Talents has a <strong>kids profile</strong>, created and managed by a responsible adult. The app <strong>does not collect personal data from children</strong>: the kids profile uses only a nickname and game progress, both kept on the device. There are no ads, no account and no contact with other people in the kids profile.</p>
<p>The adult has controls: a daily time limit and a PIN that protects leaving the kids profile and the family settings. We recommend not using the child's full name as a nickname. Parents and guardians can erase the data at any time, as described below, and reach us at {MAIL}.</p>

<h2>How to erase your data</h2>
<ul>
<li>In the app's Settings, tap <strong>“Erase all my data”</strong>; or</li>
<li>delete the app — the data stored on the device is removed with it.</li>
</ul>
<p>Erasing data does not cancel your subscription: it is managed in your Apple Account. If you sent us an email and want it deleted, just ask at {MAIL}.</p>

<h2>Your rights</h2>
<p>Brazil's General Data Protection Law (LGPD, Law 13,709/2018) and, where applicable, laws such as the GDPR give you rights including confirming whether data is processed, access, correction, deletion and portability, information about sharing, and withdrawing consent.</p>
<p>Because we keep no sign-up and do not identify you, the app's data simply is not in our systems — you control it directly on the device. The only personal data we may hold is from emails you sent us. For any request, write to {MAIL}. You may also contact your data protection authority (in Brazil, the ANPD).</p>

<h2>Changes to this policy</h2>
<p>If this policy changes, we update the date at the top of this page. Material changes — for example, if the app gains online features — will be described here before they take effect.</p>

<h2>Effective date</h2>
<p>This policy is effective as of October 7, 2026.</p>
""")

page("en", "terms", "Terms of Use", None, f"""
<div class="card">
<p><strong>The essentials:</strong> Talents is an educational Bible quiz game. Part of it is free, and there is a Premium subscription sold and billed by Apple, which you can cancel any time in iPhone Settings.</p>
</div>

<h2>1. Acceptance</h2>
<p>By using Talents you agree to these terms. If you do not agree, do not use the app. Minors must use the app with the permission of a parent or guardian, who accepts these terms on their behalf.</p>

<h2>2. License</h2>
<p>Hermes Digital grants you a personal, limited, non-exclusive, non-transferable, revocable license to use Talents on Apple devices you own or control, as permitted by the App Store rules. The app, its questions, texts, design and brand belong to Hermes Digital or its licensors. You agree not to copy, resell, extract the question bank, reverse engineer or attempt to circumvent the app.</p>

<h2>3. Bible content</h2>
<p>The content of Talents is <strong>educational and for entertainment</strong>. The app is <strong>not affiliated with any church, denomination or religious institution</strong> and is not intended as doctrinal, pastoral or spiritual guidance. Bible translations and traditions differ; we take care over the accuracy of questions and explanations, but mistakes can happen — if you find one, tell us at {MAIL}.</p>

<h2>4. Subscriptions</h2>
<p>Talents has a free version and <strong>Premium</strong>, offered as an auto-renewable subscription: a <strong>monthly</strong> plan, a <strong>yearly</strong> plan and a <strong>yearly Family</strong> plan. Yearly plans may include a 7-day free trial, when available to you.</p>
<ul>
<li>The price and period of each plan are shown on the purchase screen before you confirm.</li>
<li>Payment is charged to your Apple Account at confirmation of purchase and at each renewal.</li>
<li>The subscription <strong>renews automatically</strong> at the end of each period, at the same price, unless it is cancelled at least 24 hours before the end of the current period.</li>
<li><strong>Free trial:</strong> when the trial ends, the subscription is charged automatically at the price shown, unless you cancel at least 24 hours before the end of the trial.</li>
<li>Promotional prices apply for the period stated on the purchase screen; after that, renewal is at the regular price shown there.</li>
<li>You manage and cancel the subscription in iPhone Settings, under your name → Subscriptions. Deleting the app does not cancel the subscription. After cancellation, Premium remains until the end of the period already paid.</li>
<li>The Family plan can be used by the members of your Apple Family Sharing group, under Apple's rules.</li>
</ul>

<h2>5. Refunds</h2>
<p>Purchases are processed by Apple and follow Apple's policies. Refund requests must be made at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. We cannot process refunds directly. Nothing here limits the rights that consumer protection law gives you.</p>

<h2>6. Kids profile</h2>
<p>The kids profile and its controls (daily time and PIN) are a help for families and do not replace adult supervision. The adult is the one who creates the profile, sets the limits and keeps the PIN.</p>

<h2>7. Question suggestions</h2>
<p>Sending suggestions is optional. By sending us a question suggestion, correction or idea, you confirm you are allowed to share it and grant us a free, non-exclusive, worldwide, perpetual license to use, adapt, edit and publish that content in Talents and its materials, with no obligation of payment or credit. We are not obliged to use suggestions we receive.</p>

<h2>8. Availability</h2>
<p>We do our best to keep the app working well, but it is provided “as is”. We do not guarantee uninterrupted or error-free operation, and we may change, add or remove features and content.</p>

<h2>9. Limitation of liability</h2>
<p>To the maximum extent permitted by law, Hermes Digital is not liable for indirect damages arising from the use of the app, nor for loss of progress stored on the device (for example, when a device is replaced, lost or restored, or the app is deleted). Total liability, in any case, is limited to the amount you actually paid in the last twelve months.</p>

<h2>10. Apple</h2>
<p>Talents is distributed through the App Store. Where these terms are silent, Apple's <a href="{EULA}">standard Licensed Application End User License Agreement (EULA)</a> applies. Apple is not a party to these terms and is not responsible for the app or its support.</p>

<h2>11. Privacy</h2>
<p>Data handling is described in the <a href="privacy">Privacy Policy</a>.</p>

<h2>12. Changes</h2>
<p>We may update these terms; the date at the top shows the latest revision. Continued use after an update means you agree.</p>

<h2>13. Contact</h2>
<p>Contact: {MAIL}</p>
""")
print("ok")
