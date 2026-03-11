import vlrdevapi as vlr 
import pandas as pd 
import time
from typing import List


def collect_players():

    rows = []

    for player_id in range(1001, 1401):

        print(f"\n player {player_id}")

        try:
            profile = vlr.players.profile(player_id=player_id)

            if profile is None:
                print("no profile")
                continue 

            agent_stats = vlr.players.agent_stats(
                player_id=player_id,
                timespan="all"
            )

            if not agent_stats:
                print(" no agent stats")
                continue

            for stat in agent_stats:

                row = {
                    "player_id": player_id,
                    "handle": profile.handle,
                    "real_name": profile.real_name,
                    "country": profile.country,
                    "current_team": getattr(profile, "current_team", None),

                    "agent": stat.agent,
                    "usage_count": stat.usage_count,
                    "usage_percent": stat.usage_percent,
                    "rounds_played": stat.rounds_played,

                    "rating": stat.rating,
                    "acs": stat.acs,
                    "kd": stat.kd,
                    "adr": stat.adr,
                    "kast": stat.kast,
                    "kpr": stat.kpr,
                    "apr": stat.apr,
                    "fkpr": stat.fkpr,
                    "fdpr": stat.fdpr,

                    "kills": stat.kills,
                    "deaths": stat.deaths,
                    "assists": stat.assists,
                    "first_kills": stat.first_kills,
                    "first_deaths": stat.first_deaths,
                }

                rows.append(row)

            print("complete")

        
            time.sleep(2)

        except Exception as e:
            print(f" error {player_id}: {e}")
            continue

    
    df = pd.DataFrame(rows)

    if df.empty:
        print("no data collected")
        return

    df = df[df["agent"].notna()]
    df = df.sort_values(by=["agent", "player_id"])

    df.to_csv("test_set.csv", mode='a',index=False,header=False)

    print("\n csv created: valo_all_time.csv")
    print(f"Total rows: {len(df)}")

    return df


if __name__ == "__main__":
    collect_players()

 
