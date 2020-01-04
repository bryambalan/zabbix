# Monitoramento sites DownDetector.
Script para monitoramento de sites cadastrados no downdetector, e integração com o grafana.

O "How to" foi testado no ZABBIX 4.0.3 no Debian 9.

# Instalação:

<b>0 – </b> Instalar o script no diretório padrão aonde fica os external scripts do seu zabbix, existem  2 locais possiveis dependendo da forma de instalação do ZABBIX, compilando (<code>/usr/local/share/zabbix/alertscripts/</code>) ou por pacote (<code>/usr/lib/zabbix/alertscripts/</code>). <br>

<blockquote> <p>Acesse o seu diretório padrão e faça o download do script</p> </blockquote>
<pre>cd /usr/lib/zabbix/alertscripts/ ; wget https://raw.githubusercontent.com/made4-it/zabbix/master/Scripts/down.py -O down.py</pre>

<blockquote> <p>De permissão de execução para o script</p> </blockquote>
<pre>chmod a+x /usr/lib/zabbix/alertscripts/down.py</pre>


<i>PS: O script funciona da seguinte forma:</i><br>
<b>-</b> Acessa o site: https://downdetector.com.br/fora-do-ar/' + site + '/'<br>
<b>-</b> Extrai o status_code do site<br>
<b>-</b> Printa o Status code (Para ficar mais facil gerenciar no zabbix/grafana, foi feito alguns if's no final do código para transformar a string em numero)<br>

Status Code's Possíveis:<br>
<b>10 = success</b><br>
<b>20 = warning</b><br>
<b>30 = danger</b><br>

<blockquote> <p>Reinicie o serviço do zabbix para que ele reconheça o novo script</p> </blockquote>
<pre>systemctl restart zabbix-server</pre>

<b>1 – </b>  Adicionar o host no zabbix.<br>

Pensei em criar um template, mas para ficar mais simples criei logo um host com 3 itens de exemplo.
<blockquote> <p>Faça download do XML do HOST e adicione em seu Zabbix</p> </blockquote>
<pre>https://github.com/made4-it/zabbix/blob/master/Hosts/zbx_export_hosts.xml</pre>
<i>PS: Lembrando que o host foi criado na versão 4.0.3 do zabbix</i><br>

O host irá criar o grupo Sites e irá adicionar um Value MAP para a tradução dos Status Codes.

Para monitorar algum outro site do DownDetector, basta criar um novo item e na <b>chave</b> adicionar o seguinte valor:
<pre>down.py[MEUSITE]</pre>

<center><img src="https://github.com/made4-it/zabbix/blob/master/IMAGENS/Captura%20de%20Tela%202020-01-03%20a%CC%80s%2022.07.18.png"></center>

Exemplo para monitoramento do Apple Store:
<pre>down.py[apple-store]</pre>



Lista de todos os sites disponiveis para monitoramento:
<pre>albion-online
alelo
algar
alog
amazon
amazon-prime-video
amazon-web-services
america-net
anthem
anydesk
apex-legends
app-store
apple-store
avianca
azul
banco-central-do-brasil
banco-do-brasil
banco-inter
banco-itaú
banco-safra
banco-santander
banestes
banrisul
battlefield
betfair
binance
bing
blizzard-battle.net
bradesco
brisanet
buscapé
c6-bank
cabo-telecom
cabonnet
caixa-econômica-federal
call-of-duty
claro
clash-of-clans
clash-royale
clear
cloudflare
clusterweb
copel-telecom
correios
counter-strike
credit-suisse
crunchyroll
dataprev
dead-by-daylight
deezer
destiny
discord
dota-2
dropbox
ea
ebay
ecac
embratel
enem
epic-games-store
escape-from-tarkov
esocial
faceapp
facebook
facebook-messenger
facetime
feedly
fifa
for-honor
fortnite
free-fire
garena
getnet
github
globo
gmail
go-daddy
gol
google
google-cloud
google-play
gta-5
gvt
hbo
hostgator
hostnet
hsbc
icloud
icq
ifood
imessage
instagram
iti
itmnetworks
itunes
jurassic-world-alive
kik
kinghost
kraken
league-of-legends
ligue-telecom
line
linkedin
locaweb
mandic
mercado-bitcoin
mercado-livre
microsoft-azure
multiplay
net
netflix
neverwinter
nextel
nota-fiscal-eletrônica
nubank
office-365
oi
olx
onedrive
origin
outlook
overwatch
pagseguro
path-of-exile
paypal
pinterest
player-unknown's-battlegrounds
playstation-network
pokémon-go
polícia-federal
porto-seguro-conecta
qconcursos
rainbow-six
receita-federal
red-dead-redemption
reddit
roblox
rocket-league
salesforce
sefaz
sercomtel
sicoob
sicredi
sisu
sky
skype
slack
snapchat
spotify
steam
submarino
superdigital
teamviewer
telegram
terra
tim
tinder
tribunal-superior-eleitoral
twitch
twitter
uber
uber-eats
udemy
umbler
uol
uolhost
uplay-pc
viber
vimeo
vivo
vono
warframe
waze
wechat
whatsapp
wikipedia
world-of-warcraft
xbox-live
yahoo
yahoo-mail
youtube
zello
site-principal</pre>

Você pode verificar os sites disponiveis em:
https://downdetector.com.br/fora-do-ar

Lembrando que todo o espaço tem que ser convertido para <b>-</b> na hora da criação da chave.


Como os possiveis valores são: 

<b>10= success</b><br>
<b>20 = warning</b><br>
<b>30 = danger</b><br>

Então foi criado uma simples trigger para monitorar o last value dos items:
<pre>	{DownDetector:down.py[caixa].last()}>10</pre>

<b>2 – </b> Criar Dashboard no Grafana <br>
<center><img src="https://github.com/made4-it/zabbix/blob/master/IMAGENS/Captura%20de%20Tela%202020-01-03%20a%CC%80s%2022.05.08.png"></center>

Para adicionar a tela do grafana, basta importar o seguinte JSON para o seu grafana:
<pre>https://raw.githubusercontent.com/made4-it/zabbix/master/Grafana/downdetector.json</pre>

No grafana foi utilizado 2 plugins padrões, <b>Text</b> e <b>Singlestat</b>, aonde o Text é para gerar a imagem do site:
<center><img src="https://github.com/made4-it/zabbix/blob/master/IMAGENS/Captura%20de%20Tela%202020-01-03%20a%CC%80s%2022.05.30.png"></center>


E o SingleStat é para monitorar o valor dos itens do zabbix, aonde está configurado uma Thresholds para quando mudar para os Status codes especificos irá mudar a cor do texto apresentado, e como o zabbix está enviando numero para a gente, foi utilizado o <b>Value Mapping</b> para a tradução dos numeros para textos.
<center><img src="https://github.com/made4-it/zabbix/blob/master/IMAGENS/Captura%20de%20Tela%202020-01-03%20a%CC%80s%2022.05.59.png"></center>
<center><img src="https://github.com/made4-it/zabbix/blob/master/IMAGENS/Captura%20de%20Tela%202020-01-03%20a%CC%80s%2022.06.05.png"></center>


Para ir adicionando novos itens no grafana, basta copiar os plugings Text e SingleStat e vincular os novos sites que você adicionou no zabbix.

