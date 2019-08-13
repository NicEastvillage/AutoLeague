from autoleague.google_api_calls import get_matches

if __name__ == "__main__":
    result = get_matches(league_play_week=2, spreadsheet_id="1PxGGNaPXclPlvWxnZBC4uXoEL8YdKaz8H2vWbdy6MME",sheet_name="Ark1",range="D4:L48")
    with open("./ladder.txt", "w") as file:
        file.write(result)
    with open("./current_week.txt", "w") as file:
        file.write(result)
        
    result2 = get_matches(league_play_week=1, spreadsheet_id="1PxGGNaPXclPlvWxnZBC4uXoEL8YdKaz8H2vWbdy6MME",sheet_name="Ark1",range="D4:L48")
    with open("./previous_week.txt", "w") as file:
        file.write(result2)
