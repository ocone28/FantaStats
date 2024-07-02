from fastapi import FastAPI,Request
from pymongo import MongoClient
import connection
import querys
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura le origini consentite
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:7070",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500"  # se stai usando un server live di sviluppo come quello di VSCode
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    return "Welcome!"

@app.get("/test/Allplayer")
def get_all_player():
    result=querys.get_all_player()
        
    return(result)

@app.get("/test/AllplayerStats")
def get_all_player_stats():
    result=querys.get_all_player_stats()
        
    return(result)

@app.get("/test/NumberPlayer")
def get_number_player():
    result=querys.get_number_player()
        
    return(result)

@app.get("/test/NumPlayersForRoles")
def get_number_player_for_roles():
    result=querys.get_number_player_for_roles()
        
    return(result)


@app.get("/test/AverageForTeam")
def get_average_for_team():
    result=querys.get_average_for_team()
        
    return(result)

@app.get("/test/NumPlayerAvgGTE6")
def get_number_player_avg_gte6():
    result=querys.get_number_player_avg_gte6()
        
    return(result)

@app.get("/test/NumPlayerGrowupPrice")
def get_number_player_growup_price():
    result=querys.get_number_player_growup_price()
        
    return(result)

@app.get("/test/PlayerTopScorer")
def get_player_top_scorer():
    result=querys.get_player_top_scorer()
        
    return(result)

@app.get("/test/GetPlayerStats")
def get_player_stats(cognome:str):
    result=querys.get_player_stats(cognome)
        
    return(result)

@app.get("/test/GetPlayer")
def get_player(cognome:str):
    result=querys.get_player(cognome)
        
    return(result)


@app.get("/test/GetStatsPenaltys")
def get_stats_penaltys():
    result=querys.get_stats_penaltys()
        
    return(result)


@app.get("/test/Get5PlayerUpPrice")
def get_player_up_fatamedia():
    result=querys.get_player_up_fatamedia()
        
    return(result)


@app.get("/test/GetAllPlayer")
def get_all_player_for_name(cognome:str):
    result=querys.get_all_player_for_name(cognome)
        
    return(result)




@app.post("/test/UpdatePlayer")
async def update_player(request: Request):
    data = await request.json()
    result=querys.update_player(data)
    return (result)

@app.post("/test/AddPlayer")
async def add_player(request: Request):
    data = await request.json()
    result=querys.add_player(data)
    return (result)



@app.get("/test/DeletePlayer")
def delete_player(cognome:str):
    result=querys.delete_player(cognome)
        
    return(result)


@app.get("/test")
def get_player(sq:str):
    result=querys.get_player_team(sq)
        
    return(result)
