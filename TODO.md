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