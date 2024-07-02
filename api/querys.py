import connection
import json

def get_player_team(val):
    result = connection.collection.find({"Squadra":val})
    items=[]
    for i in result:
        prova=dict({"Nome":i['Cognome'],"Squadra": i['Squadra'],"Ruolo": i['Ruolo'],"Media": i['Media Voto'],"Fantamedia": i['Media Fantavoto'],"Quotazione iniziale": i['Quotazione Iniziale'],"Quotazione attuale": i['Quotazione Attuale']})
        items.append(prova)
        
    return(items)


def get_all_player():
    result = connection.collection.find().sort({'Cognome':1})

    items=[]

    for i in result:
        prova=dict({"Nome":i['Nome Completo'],"Cognome":i['Cognome'],"Squadra": i['Squadra'],"Ruolo": i['Ruolo'],"Media": i['Media Voto'],"Fantamedia": i['Media Fantavoto'],"Quotazione iniziale": i['Quotazione Iniziale'],"Quotazione attuale": i['Quotazione Attuale']})
        items.append(prova)
        
    return(items)


def get_number_player():
    result = connection.collection.count_documents({})
    return(result)


def get_number_player_for_roles():
    roles = ['P', 'D', 'C', 'A']
    counts = {}
    for role in roles:
        counts[role] = connection.collection.count_documents({'Ruolo': role})
    return counts


def get_all_player_stats():
    result = connection.collection2.find()

    items=[]

    for i in result:
        prova=dict({"Nome":i['Cognome'],"Squadra": i['Squadra'],"ParGiocate": i['Partite Giocate'],"GoalFatti": i['Goal Fatti']
                    ,"GoalSubiti": i['Goal Subiti'],"Assist": i['Assist'],"Ammonizioni": i['Ammonizioni'],"Espulsioni": i['Espulsioni']
                    ,"Autogoal": i['Autogoal']})
        items.append(prova)
       
    return(items)



def get_average_for_team():
    pipeline = [
       {
        '$match': {
            'Media Fantavoto': {'$gt': 0}  # Filtra i documenti con fantamedia > 0
        }
    },
    {
        '$group': {
            '_id': '$Squadra',  # Raggruppa per il campo 'squadra'
            'avgvalue': {'$avg': '$Media Fantavoto'}  # Calcola la media del campo 'fantamedia'
        }
    },
    {
        '$sort': {
            'avgvalue': -1  # Ordina le medie in ordine decrescente
        }
    },
    {
        '$limit': 1  # Limita i risultati a 1 documento (quello con la media più alta)
    },
    {
        '$project': {
            '_id': 0,
            'squadra': '$_id',  # Rinomina '_id' in 'squadra'
            'max_avgvalue': '$avgvalue'  # Mantieni il campo 'avgvalue' come 'max_avgvalue'
        }
    }
    ]
    results = connection.collection.aggregate(pipeline)
    items=[]
    for i in results:
        prova=dict({"Squadra":i['squadra'],"Media": i['max_avgvalue']})
        items.append(prova)
    return(items)



def get_number_player_avg_gte6():
    results = connection.collection.count_documents({'Media Fantavoto': {'$gte': 6}})
    print(results)
    return(results)


def get_number_player_growup_price():

    results = connection.collection.count_documents({'$expr':{'$gt':['$Quotazione Attuale','$Quotazione Iniziale']}})
    print(results)
    return(results)

def get_player_top_scorer():

    pipeline = [
    {
        '$sort': {'Goal Fatti': -1}  # Ordina le medie in ordine decrescente
        
    },
    {
        '$limit': 1  # Limita i risultati a 1 documento (quello con la media più alta)
    }
        
        ]
   
    results = connection.collection2.aggregate(pipeline)
    items=[]
    for i in results:
        prova=dict({"Cognome":i['Cognome'],"Squadra": i['Squadra'],"PartiteGiocate": i['Partite Giocate'],"GoalFatti": i['Goal Fatti'],"RigoriCalciati": i['Rigori Calciati'],"RigoriSegnati": i['Rigori Segnati'],"Assist": i['Assist'],"Ammonizioni": i['Ammonizioni'],"Espulisioni": i['Espulsioni']})
        items.append(prova)
        
    return(items) 


def get_player_stats(cognome):
   
    results = connection.collection2.find({"Cognome":cognome})
    items=[]
    for i in results:
        prova=dict({"Cognome":i['Cognome'],"Squadra": i['Squadra'],"PartiteGiocate": i['Partite Giocate'],"GoalFatti": i['Goal Fatti'],"RigoriCalciati": i['Rigori Calciati'],"RigoriSegnati": i['Rigori Segnati'],"Assist": i['Assist'],"Ammonizioni": i['Ammonizioni'],"Espulisioni": i['Espulsioni']})
        items.append(prova)
        
    return(items) 



def get_player(cognome):
    result = connection.collection.find({"Cognome":cognome})
    items=[]
    for i in result:
        prova=dict({"NomeCompleto":i['Nome Completo'],"Cognome":i['Cognome'],"Squadra": i['Squadra'],"Ruolo": i['Ruolo'],"Media": i['Media Voto'],"Fantamedia": i['Media Fantavoto'],"QuotazioneIniziale": i['Quotazione Iniziale'],"QuotazioneAttuale": i['Quotazione Attuale'],"Foto": i['Foto']})
        items.append(prova)
        
    return(items)
        

def get_stats_penaltys():
    pipeline = [
    {
        '$group': {
            '_id':None,
            'RigParati': {'$sum': '$Rigori Parati'},  # Calcola la media del campo 'fantamedia'
            'RigSbagliati': {'$sum': '$Rigori Sbagliati'},  # Calcola la media del campo 'fantamedia'
            'RigSegnati': {'$sum': '$Rigori Segnati'},  # Calcola la media del campo 'fantamedia'
            'RigCalciati': {'$sum': '$Rigori Calciati'},  # Calcola la media del campo 'fantamedia'
        }
    }
    ]
    
    results = connection.collection2.aggregate(pipeline)
    items=[]
    for i in results:
        prova=dict({"RigParati":i['RigParati'],"RigSbagliati": i['RigSbagliati'],"RigSegnati": i['RigSegnati'],"RigCalciati": i['RigCalciati']})
        items.append(prova)
    return(items)


def get_player_up_fatamedia():
    pipeline = [
     {
        '$addFields': {
            'incremento_valore': {'$subtract': ['$Quotazione Attuale', '$Quotazione Iniziale']}
        }
    },
    {
        '$sort': {'incremento_valore': -1}
    },
    {
        '$limit': 5
    },
    {
        '$project': {
            '_id':0,
            'cognome': '$Cognome',
            'valore_iniziale': '$Quotazione Iniziale',
            'valore_attuale': '$Quotazione Attuale',
            'incremento_valore': 1
        }
    }
        
    ]
    
    results = connection.collection.aggregate(pipeline)
    items=[]
    for i in results:
        prova=dict({"Cognome":i['cognome'],"ValoreIniziale": i['valore_iniziale'],"ValoreAttuale": i['valore_attuale'],"IncrementoValore": i['incremento_valore']})
        items.append(prova)
        
    return(items)




def get_all_player_for_name(cognome):
    pipeline = [
        {
        '$lookup': {
            'from': 'Statistiche',
            'localField': 'Cognome',
            'foreignField': 'Cognome',
            'as': 'newdata',
        }
    },
     {
        '$unwind': '$newdata'
    },
     {
        '$match': {
            'Cognome': cognome  # Filtra i documenti con fantamedia > 0
        }
    },
    {
        '$project': {
            '_id':0,
            'Cognome':'$Cognome',
            'NomeCompl':'$Nome Completo',
            'Ruolo':'$Ruolo',
            'RuoloMantra':'$Ruoli Mantra',
            'QuotazioneAttuale':'$Quotazione Attuale',
            'QuotazioneIniziale':'$Quotazione Iniziale',
            'Squadra':'$Squadra',
            'Foto':'$Foto',
            'Piede':'$Piede',
            'Nazionalità':'$Nazionalità',
            'DataNascita':'$Data Nascita',
            'MediaVoto':'$Media Voto',
            'MediaFantavoto':'$Media Fantavoto',

            'PartiteGiocate': '$newdata.Partite Giocate',
            'GoalFatti': '$newdata.Goal Fatti',
            'GoalSubiti': '$newdata.Goal Subiti',
            'RigoriParati':'$newdata.Rigori Parati',
            'RigoriCalciati': '$newdata.Rigori Calciati',
            'RigoriSegnati': '$newdata.Rigori Segnati',
            'RigoriSbagliati':'$newdata.Rigori Sbagliati',
            'Assist': '$newdata.Assist',
            'Ammonizioni':'$newdata.Ammonizioni',
            'Espulsioni': '$newdata.Espulsioni',
            'Autogoal': '$newdata.Autogoal'

        }
    }
        
    ]
    
    results = connection.collection.aggregate(pipeline)
    items=[]
    for i in results:
        prova=dict({"Cognome":i['Cognome'],"NomeCompl": i['NomeCompl'],"Ruolo": i['Ruolo'],"RuoloMantra": i['RuoloMantra'],
                    "QuotazioneAttuale":i['QuotazioneAttuale'],"QuotazioneIniziale": i['QuotazioneIniziale'],"Squadra": i['Squadra'],"Foto": i['Foto'],
                    "Piede":i['Piede'],"Nazionalità": i['Nazionalità'],"DataNascita": i['DataNascita'],"MediaVoto": i['MediaVoto'],"MediaFantavoto": i['MediaFantavoto'],
                    "PartiteGiocate":i['PartiteGiocate'],"GoalFatti": i['GoalFatti'],"GoalSubiti": i['GoalSubiti'],"RigoriParati": i['RigoriParati'],
                    "RigoriCalciati":i['RigoriCalciati'],"RigoriSegnati": i['RigoriSegnati'],"RigoriSbagliati": i['RigoriSbagliati'],"Assist": i['Assist'],"Ammonizioni": i['Ammonizioni'],
                    "Espulsioni":i['Espulsioni'],"Autogoal": i['Autogoal']
                })
        items.append(prova)
        
    return(items)


def update_player(data):
    data2=json.loads(data)
    filter={'Cognome':data2['Cognome']}


    update={
        '$set':{
            'Cognome': data2['Cognome'],
            'Nome Completo': data2['Nome Completo'],
            'Ruolo': data2['Ruolo'],
            'Ruoli Mantra':  data2['Ruoli Mantra'],
            'Quotazione Attuale':  data2['Quotazione Attuale'],
            'Quotazione Iniziale': data2['Quotazione Iniziale'],
            'Squadra': data2['Squadra'],
            'Piede': data2['Piede'],
            'Nazionalità': data2['Nazionalità'],
            'Data Nascita':  data2['Data Nascita'],
            'Media Voto':  data2['Media Voto'],
            'Media Fantavoto':  data2['Media Fantavoto']
        }
    }

    update2={
        '$set':{
            'Cognome': data2['Cognome'],
            'Squadra': data2['Squadra'],
            'Partite Giocate': data2['Partite Giocate'],
            'Goal Fatti':  data2['Goal Fatti'],
            'Goal Subiti':  data2['Goal Subiti'],
            'Rigori Parati':  data2['Rigori Parati'],
            'Rigori Calciati':  data2['Rigori Calciati'],
            'Rigori Segnati':  data2['Rigori Segnati'],
            'Rigori Sbagliati':  data2['Rigori Sbagliati'],
            'Assist':  data2['Assist'],
            'Ammonizioni':  data2['Ammonizioni'],
            'Espulsioni':  data2['Espulsioni'],
            'Autogoal':  data2['Autogoal']
        }
    }

    result=connection.collection.update_one(filter,update)
    result2=connection.collection2.update_one(filter,update2)
    print(result.matched_count)
    print(result.modified_count)
    print(result2.matched_count)
    print(result2.modified_count)

    return()


def add_player(data):
    data2=json.loads(data)

    update={
   
            'Cognome': data2['Cognome'],
            'Nome Completo': data2['Nome Completo'],
            'Ruolo': data2['Ruolo'],
            'Ruoli Mantra':  data2['Ruoli Mantra'],
            'Quotazione Attuale':  data2['Quotazione Attuale'],
            'Quotazione Iniziale': data2['Quotazione Iniziale'],
            'Squadra': data2['Squadra'],
            'Piede': data2['Piede'],
            'Nazionalità': data2['Nazionalità'],
            'Data Nascita':  data2['Data Nascita'],
            'Media Voto':  data2['Media Voto'],
            'Media Fantavoto':  data2['Media Fantavoto'],
            'Foto':data2['Foto']
        
    }

    update2={
        
            'Cognome': data2['Cognome'],
            'Squadra': data2['Squadra'],
            'Partite Giocate': data2['Partite Giocate'],
            'Goal Fatti':  data2['Goal Fatti'],
            'Goal Subiti':  data2['Goal Subiti'],
            'Rigori Parati':  data2['Rigori Parati'],
            'Rigori Calciati':  data2['Rigori Calciati'],
            'Rigori Segnati':  data2['Rigori Segnati'],
            'Rigori Sbagliati':  data2['Rigori Sbagliati'],
            'Assist':  data2['Assist'],
            'Ammonizioni':  data2['Ammonizioni'],
            'Espulsioni':  data2['Espulsioni'],
            'Autogoal':  data2['Autogoal']
        
    }

    result=connection.collection.insert_one(update)
    result2=connection.collection2.insert_one(update2)

    print(result.inserted_id)
    print(result2.inserted_id)

    return()




def delete_player(cognome):

    result = connection.collection.delete_one({"Cognome": cognome})
    result2 = connection.collection2.delete_one({"Cognome": cognome})

    print(result.deleted_count)
    print(result2.deleted_count)

    return()