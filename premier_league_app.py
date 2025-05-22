
import requests
import streamlit as st

API_KEY = 'edc3f951e2e347e3ae3b1e7757eb6834'  # 🔑 เปลี่ยนตรงนี้ให้เป็น API Key ของคุณ
headers = {'X-Auth-Token': API_KEY}
url = 'https://api.football-data.org/v4/competitions/PD/matches?season=2024'

def get_results():
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return ["❌ ไม่สามารถดึงข้อมูลได้"]

    data = response.json()
    matches = data['matches']
    results = []

    count = 0
    for match in reversed(matches):
        score = match['score']['fullTime']
        if score['home'] is not None and score['away'] is not None:
            home = match['homeTeam']['name']
            away = match['awayTeam']['name']
            date = match['utcDate'][:10]
            results.append(f"{date} - {home} {score['home']} : {score['away']} {away}")
            count += 1
        if count == 5:
            break

    return results

st.title("📊 ผลลาลีกาสเปนล่าสุด")
if st.button("ดึงข้อมูลผลการแข่งขัน"):
    for line in get_results():
        st.write(line)
