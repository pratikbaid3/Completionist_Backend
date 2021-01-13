import sqlite3

conn = sqlite3.connect("PS4_Game_Database.db")

gamesc = conn.cursor()
gamesc.execute("SELECT * FROM PS4_Games")
games = gamesc.fetchall()
game_list = []
for data in games:
    game_name = data[0]
    gold = 0
    silver = 0
    bronze = 0
    platinum = 0
    c = conn.cursor()
    # Get count of gold trophies
    c.execute(
        f'SELECT COUNT(*) FROM PS4_Games_Guide WHERE game_name = "{game_name}" AND trophy_type = "GOLD"'
    )
    gold = c.fetchone()[0]

    # Get count of silver trophies
    c.execute(
        f'SELECT COUNT(*) FROM PS4_Games_Guide WHERE game_name = "{game_name}" AND trophy_type = "SILVER"'
    )
    silver = c.fetchone()[0]

    # Get count of bronze trophies
    c.execute(
        f'SELECT COUNT(*) FROM PS4_Games_Guide WHERE game_name = "{game_name}" AND trophy_type = "BRONZE"'
    )
    bronze = c.fetchone()[0]

    # Get count of platinum trophies
    c.execute(
        f'SELECT COUNT(*) FROM PS4_Games_Guide WHERE game_name = "{game_name}" AND trophy_type = "PLATINUM"'
    )
    platinum = c.fetchone()[0]

    print(game_name)
    # Update the PS4_Games db
    c.execute(
        f'UPDATE PS4_Games SET GOLD = "{gold}", SILVER = "{silver}", BRONZE = "{bronze}", PLATINUM = "{platinum}" WHERE game_name = "{game_name}"'
    )
    conn.commit()

conn.commit()
conn.close()
