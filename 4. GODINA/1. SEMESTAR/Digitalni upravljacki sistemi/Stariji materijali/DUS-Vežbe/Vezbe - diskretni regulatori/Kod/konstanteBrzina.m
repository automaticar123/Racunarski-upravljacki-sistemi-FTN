%%
% Anja Buljevic
% April 2020
%% Zadatak
% Cilj ovih vezbi je da isprojektujemo diskretne regulatore za jednosmerni
% motor, cije smo modele izvodili na prethodnim vezbama. Bi?e razmatrana
% dva moguca upravljacka sistema jednosmernog motora za:
% upravljanje brzinom i upravljanje pozicijom.
% Simulacije su radjene u Simulink-u.


%% Inicijalizacija
% Priprema radnog prostora. Brisanje svih promenljivih. Brisanje radnog
% prostora. Napomena: Pri pokretanju MATLAB koda preporucujemo
% pokretanje sekcije po sekciju tako što se pozicionirate u sekciju i
% pritisnete komande Ctrl+Enter.

clc

close all
clear all
%% Konstante motora 
% Prvo cemo projektovati regulatore za upravljanje brzinom jednosmernog motora.
% Simulacije za upravljanje brzinom razlicitim regulatorima je data u fajlu
% upravljanjeBrzinom.slx, a konstante su date u fajlu konstanteBrzina.m. 
% Funkcija prenosa motora u tom slucaju je: G(s) = Km/(Tm*s + 1).

Km = 180;
Tm = 1.3;

T = 0.01; % perioda odabiranja

%% Osnovni oblik P regulatora
% Zeljeni ulaz r(t) cemo u svim primerima modelovati kao konstantan signal
% odredjeno amplitude.
K = 0.1; % proporcionalno pojacanje
b = 0.7;
%%
% Ocekivano, postoji greska u ustaljenom stanju. Da li ta greska ikada moze
% biti jednaka nuli?

%% Osnovni oblik PI regulator
% Radi eliminisanja greske u ustaljenom stanju, neophodno je da uvedemo
% integralno dejstvo u regulator.

K1 = 0.3; % proporcionalno pojacanje
Ti1 = 1.3; % vremenska konstanta integraljenja
%%
% Nakon simulacije vidimo da je greska u ustaljenom stanju jednaka nuli, odnosno izlaz
% je jednak zeljenoj vrednosti. 
%%
% *Domaci*: Podesiti parametre regulatora tako da preskok bude sto manji.

%% Osnovni oblik PI regulatora sa poremecajem i sumom
% U osnovno kolo automatskog upravljanja, ubacicemo poremecaj i sum.
% Za potrebe simulacije ovog primera, vrednost zeljenog ulaza r(t) cemo staviti da je
% 10. Poznato je da je referenca brzina, pa bi njena vrednost trebala da bude veca, 
% ali zelimo da pokazemo sve efekte koji bi se za vece vrednosti slabije videli.
% Poremecaj l(t) cemo modelovati kao konstantnu pobudu koja pocinje da deluje
% posle 5s (radi razdvajanja ulaza od poremecaja) sa amplitudom 1.
% Sum n(t) je sinusni signal ucestanosti 50000rad/s i amplitude 0.1. 

%%
% Kao sto je i receno na predavanjima, PI regulator dobro trpi sum
% merenja.

%% Osnovni oblik PID regulatora
% Sada cemo implementirati diskretni PID regulator. D dejstvo smo
% diskretizovali koriscenjem Ojler 2 transformacije.
K2 = 0.1; % proporcionalno pojacanje
Ti2 = 0.8; % vremenska konstanta integraljenja
Td2 = 0.06; % vremenska konstanta diferenciranja
%% 
% Kao sto je i receno na predavanjima, D dejstvo pojacava sum, zbog cega je
% neophodno da uvedemo modifikaciju D dejstva.

%% Realni PID regulator
N = 3; % vremenska konstanta niskopropusnog filtra
b = 0.7; % tezinski faktor
%%
% Uvodjenjem modifikovanog D dejstva primecujemo da se amplituda
% oscilacija znatno smanjila sto je objasnjeno u predavanjima.

