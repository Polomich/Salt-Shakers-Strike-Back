# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define cond = Character('Conducteur', color="#dd5045")
define c = Character('Clown', color="#259967")
define a = Character("Athlète", color="#5068a1") #fille
define i  = Character("Intello", color="#aac7e3")
define r = Character("Rebelle", color="#b25853") #fille
define p = Character("Enseignant", color="#FFFFFF")

# Le jeu commence ici
label start:
    "C'était une nuit sombre et orageuse. Le dernier groupe d'élèves de l'orchestre de l'école monta à bord du train pour retourner à Montréal."

    "Tout d'un coup, le train s'arrete."

    cond "Le train ne bougera pas tant que les voies ne seront pas dégagées. Je dois aller m’assurer que les passagers vont bien."

    call screen arrowScreen
    show screen arrowScreen


label checkingOnStudents:
    scene train passenger

    c "*Ronfle doucement*"

    menu :
        "Réveiller":
            jump wakeupclown

        "Laisser reposer":
            jump athlete   


label wakeupclown:
    c "Euh, allô ?" 
    c "*Il secoue sa tête*"
    c "Sommes-nous arrivés ?"

    cond "Nous avons été retardés, je vérifie juste que touts les passagers vont bien."

    c "Ohh ..ok.." 

    menu: 
        "Aller verifier le prochain passager":
            jump athlete


label athlete:
    a "*Elle regarde par la fenêtre.*"
    a "Bonjour, monsieur, pourquoi s'est-on arrêté?"

    cond "Les voies sont bloquées, on va attendre qu'on les libère."

    a "Oh, qu'est-ce qui a bloqué les voies?"

    cond "Je ne sais pas." 
    cond "UN MONSTRE"

    a "*Elle rit*"
    
    cond "Ne vous inquiétez pas. Vous allez bien ?"

    a  "Je vais bien, mais j'ai cru entendre quelqu'un crier ?"

    cond "Vous savez qui a crié ?"

    a "Je ne sais pas, mais il était quelque part derrière moi."

    cond "Merci."
    cond "Je vous surveille, gamine."

    menu: 
        "Aller verifier le prochain passager":
            jump nerdpanic

label nerdpanic:
    i "*Regarde autour en panique*"
    i "Bonjour, monsieur ! Que s'est-il passé!?!"

    cond "Les voies sont bloquées, on va juste rester arrêtés le temps qu'elles soient libérées."

    i "J'ai entendu un cri ! Vous êtes sûr que tout va bien ?"

    cond "Peu importe. Qu'est-ce qui ne va pas ?"
   
    i "J'ai entendu un cri… puis un horrible gargouillement quelque part derrière nous… J'ai… J'écoute ces podcasts sur des meurtres… Et je crois qu'il y a un meurtrier dans le train…"
   
    cond "D'accord..."
    cond "Quand as-tu entendu tout ça?"
   
    i "Quand tout est devenu noir, après qu'on se soit arrêtés."
   
    cond "Merci, mon garçon."
    cond "Ne t'inquiète pas, ça va aller."
    cond "*Il se tourne vers l'athlete.*"
    cond "Toi aussi, tu as entendu un cri ? D'où l'as-tu entendu ?"

    a "Il venait de derrière moi. Je crois que c'était notre professeur…"

    cond "Tu te souviens d'autre chose ?"
    
    a "Je crois, je crois que quelqu'un est passé devant moi… Avec beaucoup de tissu qui froissait…"

    cond "Je vais me renseigner."
    cond "Ne t'inquiète pas."

    menu: 
        "Aller verifier le prochain passager":
            jump rebel

label rebel:
    r "*Elle renifle doucement, complètement endormie."

    cond "Excusez-moi, mademoiselle ..."

    r "*Elle marmonne et s'agite, ses vêtements bruissent.*"

    cond "Mademoiselle ..."

    r "Elle gémit et cligne des yeux, puis sursaute et fusille le conducteur du regard."
    r "Pourquoi m'as-tu réveillé, mec ?!"

    cond "Je voulais juste vérifier si tu allais bien."
    
    r "Je dormais, mec ! J'étais en pleine forme ! Merci d'avoir gâché ma nuit."

    cond "Protocole standard ... 'mec'. Je dois m'assurer que tout le monde va bien."

    r "Eh bien, c'est un protocole complètement stupide."

    cond "*Vous vous tournez vers l'Intello.*" 
    cond "T'as des vêtements vraiment souillés, toi. T'as pas fait une promenade pendant que les lumières étaient éteintes, hein ?"

    i "Les lumières étaient éteintes ? J'ai l'air de m'etre promené? Je dormais."

    cond "T'es sûr ?"

    i "Je dormais ici ! Demandez à n'importe qui, bien sûr, j'en suis sûr!"

    cond "D'accord ..."

    menu: 
        "Aller verifier le prochain passager":
            jump theprof

label theprof:
    p "*Il est allongé, immobile et silencieux, contre la fenêtre. Son col est relevé pour se protéger du froid de la cabine, un léger bruit de gouttelettes et une odeur de fosse septique désagréable se font entendre.*"

    menu: 
        "Reveiller":
            jump wakeprof
        "Laisser dormir":
            jump notwakeprof

label wakeprof:
    p "*Il s’effondre en avant. Son corps est froid et sans vie.*"

    "Tout le monde crie."

    c "*Vous vous autorisez à incarner le roturier que vous aimeriez être, puis votre formation policière prend le dessus et vous évaluez la situation.*"

    menu:
        "Commencer l'investigation":
            jump investigation

label notwakeprof:
    p "*Il est allongé, étrangement immobile. L’odeur dans l’air vous rappelle des souvenirs… Un souvenir de votre vie antérieure… De policier…*"

    menu:
        "Commencer l'investigation":
            jump investigation

label investigation:
    "L’homme est encore chaud au toucher. Aucune trace de rigidité n’est présente, ce qui indique que le décès a eu lieu au cours des trois dernières heures. Le train est parti il ​​y a deux heures, pile à l’heure, ce qui signifie que l’homme était vivant lorsqu’il est monté à bord."
    "Le visage est éclatant, ce qui suggère vraisemblablement une cause de décès, mais probablement due à une vie passée à hurler sur des jeunes turbulents. L’âge de cet homme est difficile à déterminer, bien qu’il se situe quelque part dans la moyenne de sa vie, à moins que l’éducation ne l’ait prématurément vieilli. Inutile de deviner sa profession : le costume démodé et la mallette indiquent clairement sa profession."

    menu:
        "Verifier son cou":
            jump cou
        "Verifier ses bras":
            jump bras
        "Verifier son sac":
            jump sac
        "Verifier son portefeuille":
            jump paper

label cou:
    "Vous baissez le col de l’homme. Vos soupçons sont confirmés : une fine ligne rouge et menaçante se dessine autour de son cou. Elle est fine et constitue manifestement la cause du décès. Autour de son cou se trouve un petit crucifix en or suspendu à une chaîne, une arme du crime plausible ?"
    "Vous regardez attentivement."
    "Une petite zone de chair intacte est visible sur le côté du cou. Cet homme a été attaqué depuis le couloir."

    menu:
        "Verifier ses bras":
            jump bras
        "Verifier son sac":
            jump sac
        "Verifier son portefeuille":
            jump paper
        "Finir l'investigation":
            jump interupt

label bras:
    "Cet homme ne présente aucune blessure défensive. Pas de sang sous les ongles, pas de peau et aucune trace de lutte. En résumé, une victime d’une passivité déprimante ; il dormait peut-être au moment des faits. Une montre à remontoir égrène les heures sans relâche, sans donner aucune indication sur l’heure du décès. Le coupable ne savait-il pas que la procédure standard pour les criminels était de briser l’objet ?"
    "Vous regardez attentivement."
    "Les ongles des mains sont exceptionnellement bien entretenus pour un universitaire et un homme. Il porte une alliance à un doigt ; vous êtes content de ne plus être dans la police ! Le côté déprimant du métier ne vous concerne plus. Il n’y a aucun dommage apparent au doigt autour de la bague. Si le mobile était le vol, le voleur n’a soit pas remarqué la bague, soit n’a pas tenté de l’enlever, soit savait que c’était peine perdue."

    menu:
        "Verifier son cou":
            jump cou
        "Verifier son sac":
            jump sac
        "Verifier son portefeuille":
            jump paper
        "Finir l'investigation":
            jump interupt

label sac:
    " Le sac de l'homme contient une pochette de partitions et une liasse de feuilles d'exercices à moitié corrigées. Tout le contenu du sac est recouvert d'une fine couche de sel et de miettes de cacahuètes, qui se sont répandues d'un sac à moitié ouvert, jeté avec le reste des affaires. Le sac ne contient aucune indication discernable du nom ou de l'identité de l'homme."
    "La poche avant du sac contient trois trombones, un emballage de chewing-gum rempli de chewing-gum mâché et un permis de conduire."
    "François Merick \n1966-06-06 n\666 Rue Van Horne \nMontréal \nSexe M"
    "Vous plissez les yeux en regardant l'homme, et son nom vous échappe. Pour vous, on l'appellera simplement l'enseignant."

    menu:
        "Verifier son cou":
            jump cou
        "Verifier ses bras":
            jump bras
        "Verifier son portefeuille":
            jump paper
        "Finir l'investigation":
            jump interupt

label paper:
    "L'enseignant est mort, laissant les copies à moitié corrigées. Aucune n'a de très bonnes notes, et la note la plus élevée (un B+ attribué à un étudiant nommé Ned) est couverte de suggestions et de notes pointilleuses. La note la plus basse est un F avec deux signes moins, obtenu par une étudiante nommée Ruby. Il y a tellement de rouge sur la page qu'il est difficile de voir ce qui se passe en dessous. Les autres notes oscillent toutes entre C et D. La plupart sont des D. Soit les étudiants sont nuls, soit il est un correcteur sévère."

    menu:
        "Verifier son cou":
            jump cou
        "Verifier ses bras":
            jump bras
        "Verifier son sac":
            jump sac
        "Finir l'investigation":
            jump interupt

label interupt:
    "Les élèves vous regardent par-dessus leur siège. Ils semblent méfiants et inquiets."

    r "Dis donc, qu’est-ce que tu fais à notre prof ?"
    i "Lache-le, pervers!"

    cond "Votre professeur a été assassiné. Restez calmes et à votre place.."

    "Les élèves vous regardent d’un air incrédule."

    a "C’est une blague, monsieur ?"

    cond "Non, votre professeur est mort."

    i "JE SAVAIS QU'IL S'ÉTAIT PASSÉ QUELQUE CHOSE D'HORRIBLE ! C'EST UN MEURTRE ! LE MEURTRIER EST TOUJOURS PARMI NOUS ET ON ALLAIT TOUS MOURIR !!!!"

    i "*Il fond en larmes.*"

    "Les autres élèves se regardent d'un air absent."

    cond "C'était un meurtre, mais vous n'avez rien à craindre. Je vous protégerai!"

    r "Que fait-on maintenant ?"

    cond "Reste où tu es pendant que j'appelle le 911."

    i "On ne peut pas appeler le 911 ! J'ai déjà essayé !"
    i "*Il montre son telephone sans reseau.*"

    cond "*Ton téléphone n'a pas de réseau non plus, tu es coupé et seul.*"

    cond "Restez où tu es. J'ai des questions pour vous tous."


