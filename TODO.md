# Important TODO's are tracked here
- Specify an IP address and port for the manager's server.
- Don't forget: you may need to give MicroRTS and it's two agents that pairs with it a unique ID so that it is know who pairs with who.
In the event that there are multiple instances of MicroRTS and multiple instances of Agents it is mandatory to know who pairs with who and you do this by a UNIQUE ID(maybe unique experiment ID ?????) - O alta idee si mai puternica decat atribuirea unui ID unic fiecarui client si fiecarui server este folosirea de certificate. Practic serverul are certificatul propriu + fiecare client are certificatul sau/ sau certificatul de client si astfel validezi ca cine se conecteaza la server este cine trebuie/cine se conecteaza la client este cine trebuie -> ca sa nu poti sa falsifice ID-ul.
E O IDEE FOARTE FOARTE BUNA, MERITA SA FIE EXPLORATA MAI DEPARTE.
- O alta idee ce trebuie tinuta minte este ideea de matching si anume:
  - Ai mai multe instante de MicroRTS conectate la server
  - Ai mai multe instante de Agenti conectate la server
  -> COMUNICATIA DINTRE SERVER SI TOTI CLIENTII ESTE SECURIZATA CU CERTIFICATE.
  -> TREBUIE SA IMPERECHEZI instantele de MicroRTS cu instantele de Agenti, sa stii care MicroRTS se conecteaza la care Agenti (intre cine si cine faci comunicarea).
  -> TREBUIE TINUT MINTE ASTA.
  -> IDEEA DE BAZA: o instanta de MicroRTS se imperecheaza cu o instanta de Agenti.
  -> cand ai mai multe copii de MicroRTS si mai multe copii de Agenti, trebuie sa stii cine se imperecheaza cu cine ca sa poti face legatura/comunicarea intre ele.
  -> Managerul e cel care face imperecherea si trimiterea mesajelor.

- ALTA IDEE BUNA: FIECARE CLIENT CARE SE CONECTEAZA LA SERVER TREBUIE SA ANUNTE(SPUNA) SERVERULUI DACA ESTE MicroRTS SAU AGENTI. TOT IN IDEEA DE MATCHING, SERVERUL TREBUIE SA STIE CA SA CONECTAT MicroRTS SAU CA SA CONECTAT AGENTII. DECI CLIENTUL TREBUIE SA SPUNA SERVERULUI DACA ESTE MicroRTS sau Agentii.

- ALTA IDEE BUNA: Fiecare instanta trebuie sa fie identificata unic prin ceva, probabil printr-un ID unic. DECI AM 2 id-uri unice:
  -> ID-ul unic de client = identifica unic acel client
  -> ID-ul de experiment = identifica unic acel experiment particular si pe baza lui stiu sa fac matching-ul dintre MicroRTS<->Agenti.
  -> Fiecare client trebuie sa spuna ce tip este, daca este MicroRTS sau Agenti.

- In loc de Agenti, cred ca trebuie gasita o noua denumire.

- Toate astea trebuie sa le adaugi la notite sa nu le uiti.

- CUM imi vin mie idei marete la 3 dimineata BOSS.

Deci am asa:
     - Securizarea comunicatiei bidirectionale MicroRTS <-> Manager si Manager<->Agenti folosind certificate.
     - MicroRTS + Manager ruleaza impreuna pe acelasi server(nu neaparat cu gpu). NU E NEVOIE DE GPU. SAU ESTE NEVOIE ?????
     - Agentii ruleaza pe alt server(Google Colab sau server propriu) OBLIGATORIU cu GPU.
     - Fiecare Client are asociat un ID unic. ID-ul acesta unic este atribuit de manager ????? CE FAC CU ID-UL ASTA UNIC AL FIECARUI CLIENT ?? LA CE IL FOLOSESC ????? PRESUPUN CA AM NEVOIE DE EL DAR NU STIU INCA LA CE L-AS FOLOSI!!!
     - Fiecare experiment are asociat un ID unic. Folosindu-se de acest ID se face match-ul de instanta MicroRTS <-> instanta Agenti intotdeauna, mai ales cand am multiple instante de MicroRTS si Agenti.
     - MicroRTS e pornit intotdeauna de Manager pentru ca ruleaza ambii pe acelasi server.
     - Agentii:
	- Daca Agentii sunt rulati in Google Colab => sunt porniti de catre Manager prin google colab cli.
	- Daca Agentii sunt rulati pe server propriu(obligatoriu cu GPU) => atunci ei NU SUNT PORNITI De Manager, pentru ca Managerul nu se poate conecta la serverul unde ruleaza agentii. Ei trebuie porniti manual, pe acel server propriu, cu gpu, pe care ruleaza.