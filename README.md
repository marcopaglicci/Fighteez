# Fighteez

## Descrizione
Fighteez è un social network dedicato ai fighter professionisti e agli amanti degli sport di combattimento. La piattaforma consente agli utenti di connettersi, condividere esperienze, seguire i propri fighter preferiti e scoprire nuovi talenti.

## Funzionalità principali

### 1. Registrazione e Login
Gli utenti possono creare un account tramite registrazione o accedere con le loro credenziali esistenti.

### 2. Profilo Utente
Ogni utente ha un profilo personalizzabile dove può aggiungere foto, informazioni personali e dettagli sulla propria carriera di combattente.

### 3. Seguire (Follow)
Gli utenti possono seguire altri fighter per rimanere aggiornati sulle loro attività e post.

### 4. Mi Piace (Like)
Gli utenti possono mettere "Mi Piace" ai post degli altri, mostrando apprezzamento per le loro foto  e aggiornamenti.

### 5. Commenti
Gli utenti possono commentare i post per interagire e condividere opinioni o complimenti.

### 6. Pubblicazione di Foto e Video
Gli utenti possono caricare e condividere foto e video dei loro allenamenti, combattimenti e momenti salienti.

### 7. Ricerca Utenti
La piattaforma include una funzionalità di ricerca che permette di trovare nuovi utenti tramite nome, nickname o parole chiave 

### 8. Feed di Attività
Un feed di attività aggiornato in tempo reale mostra i post, i mi piace e i commenti degli utenti seguiti.

## Tecnologie Utilizzate
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL
- **Autenticazione:** Django Allauth
- **Hosting:** Render

## Installazione
Per eseguire il progetto in locale, segui questi passaggi:

1. Clona il repository:
   git clone https://github.com/Marco-Paglicci/Fighteez.git
   cd Fighteez

2.Modifica settings.py-> cambia le seguenti impostazioni per assicurarti il run in locale
   -Cambia ALLOWED_HOST = ... in ALLOWED_HOSTS = []
   -Cancella o Commenta (riga 90 settings.py):
      database_url = os.environ.get("DATABASE_URL")
      DATABASES["default"] = dj_database_url.parse(database_url)
      
3. Crea un ambiente virtuale e attivalo:
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Installa le dipendenze:
  pip install -r requirements.txt
  
4.Applica le migrazioni al database:
  python manage.py migrate
  
5.Avvia il server di sviluppo:
  python manage.py runserver

Contatti
Per qualsiasi domanda o suggerimento, non esitare a contattarmi via email: marco.paglicci@example.com

Grazie per aver scelto Fighteez! Unisciti alla nostra comunità e inizia a condividere la tua passione per gli sport di combattimento.

Questo README fornisce una panoramica completa del progetto, le sue funzionalità principali, le tecnologie utilizzate e le istruzioni per l'installazione e il contributo. Puoi personalizzarlo ulteriormente secondo le tue esigenze.


   
