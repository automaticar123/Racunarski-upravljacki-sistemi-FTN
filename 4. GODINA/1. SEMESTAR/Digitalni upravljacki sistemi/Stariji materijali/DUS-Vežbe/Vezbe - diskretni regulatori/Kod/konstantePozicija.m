%%
% Anja Buljevic
% April 2020
%% Inicijalizacija
% Priprema radnog prostora. Brisanje svih promenljivih. Brisanje radnog
% prostora. Napomena: Pri pokretanju MATLAB koda preporucujemo
% pokretanje sekcije po sekciju tako što se pozicionirate u sekciju i
% pritisnete komande Ctrl+Enter.

clc
close all
clear all
%% Upravljanje pozicijom
% Drugi primer koji cemo razmatrati jeste upravljanje pozicijom jednosmernog motora.
% Funkcija prenosa motora je data izrazom G(s) = c/(s*(s + a))
% Konstante motora za upravljanje pozicijom su sledece:

a = 0.8;
c = 140;
T = 0.01; %perioda odabiranja
N = 8; % vremenska konstanta niskopropusnog filtra
b = 0.7; % tezinski faktor

%% Realni P regulator
% *Domaci*: Projektovati realni P regulator. Da li postoji greska u
% ustaljenom stanju i zasto? Da li na potiskivanje greske u ustaljenom
% stanju, kao posledice signala reference, moze da utice struktura samog
% sistema (tacnije postojanje integratora)?
b = 1;
K = 3;
%% Realni PD regulator
K3 = 3; % proporcionalno pojacanje
Td3 = 0.3; % vremenska konstanta diferenciranja
%%
% Kao i u prethodnom primeru, greska u ustaljenom stanju je ocekivano
% jednaka nuli zbog astatizma koji se nalazi u samom modelu procesa kojim
% upravljamo. PD regulator trebalo bi da obezbedi brzi odziv sistema, i u
% slucaju ovakve strukture modela, lakse podesavanje parametara, jer
% uvodjenjem PD regulatora, uvodimo nulu u strukturu sistema i postoje dva
% podesiva parametra, sto daje vecu slobodu da uticemo na ponasanje
% sistema.

%% Realni PD regulator sa poreme?ajem
% U sledecu simulaciju cemo ubaciti i poremecaj l(t) koji je modelovan kao
% konstannta pobuda amplitude 0.2 i cije dejstvo pocinje od 25s.

%%
% Nakon simuliranja primecujemo da postoji greška u ustaljenom stanju. *ZASTO?* 

%% Realni PID regulator

K4 = 5; % proporcionalno pojacanje
Td4 = 0.1; % vremenska konstanta diferenciranja
Ti4 = 1.1; % vremenska konstanta integraljenja

%%
% *Domaci:* Naci opseg parametra PID-a za koji sistem stabilan.
%% 
% *Domaci:* Uvesti konstantan poremecaj amplitude 0.2 posle 50s. Da li ce PID
% uspeti da eliminiše uticaj poremecaja na gresku u ustaljenom stanju?
%%
% *Domaci:*	Pronaci parametre PID regulatora tako da sistem bude stabilan i
% otporan na uticaj poremecaja modelovanog u primeru pre i na uticaj mernog
% suma koji se modeluje kao sinusni signal, amplitude 0.05 i ucestanosti
% 50000rad/s.