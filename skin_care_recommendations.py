import pandas as pd

# Load raw dataset
data = pd.read_csv("/Users/choihyeseon/Desktop/열심히 하자/recommandation/skin_care_recommendations_raw_dataset.csv")

# Define mappings for keywords and recommendations
keywords_mapping = {
    "Q1 (피부 타입)": {
        "건성": ["보습 강화"],
        "지성": ["피지 조절"],
        "복합성": ["유수분 밸런스"],
        "민감성": ["저자극"]
    },
    "Q2 (피부 고민)": {
        "여드름 및 피지": ["항염", "진정"],
        "모공 확장 및 블랙헤드": ["모공 관리"],
        "잦은 건조": ["보습 강화"],
        "민감성으로 인한 붉은기": ["진정", "저자극"],
        "주름 및 탄력 저하": ["안티에이징"]
    },
    "Q3 (문제 위치)": {
        "T존": ["T존 관리"],
        "U존": ["U존 관리"],
        "얼굴 전체": ["전체 관리"],
        "없음": ["기본 관리"]
    },
    "Q4 (피부 상태)": {
        "유분 과다": ["피지 조절"],
        "건조함": ["보습 강화"],
        "붉은기": ["진정"],
        "균형 잡힘": ["유지 관리"]
    },
    "Q5 (여드름 형태)": {
        "염증성": ["항염"],
        "좁쌀여드름": ["각질 관리"],
        "블랙헤드": ["모공 관리"],
        "다양한 형태": ["종합 관리"]
    },
    "Q6 (클렌징 습관)": {
        "이중 세안": ["적절한 세정"],
        "단일 세안": ["추가 세정 필요"],
        "불규칙한 세안": ["루틴 필요"],
        "과도한 세안": ["피부 장벽 보호"]
    },
    "Q7 (사용 제품)": {
        "기본 단계": ["기본 관리"],
        "기능성 제품 위주": ["기능성 관리"],
        "최소한의 사용": ["루틴 필요"],
        "자주 바뀜": ["안정된 루틴"]
    },
    "Q8 (햇볕 반응)": {
        "금방 붉어짐": ["강력한 자외선 차단"],
        "쉽게 탐": ["SPF 50+ 필요"],
        "별다른 변화 없음": ["기본 자외선 차단"],
        "번들거림": ["가벼운 자외선 차단"]
    },
    "Q9 (관리 제품)": {
        "약국 제품": ["약국 제품 보완"],
        "스킨케어 브랜드 제품": ["시너지 효과"],
        "특별히 사용하지 않음": ["기본 관리 필요"],
        "홈케어 방법": ["효율적인 관리"]
    },
    "Q10 (주의 성분)": {
        "알레르기 있음": ["저자극 성분"],
        "없음": ["모든 성분 가능"],
        "모르겠다": ["안전한 성분"]
    }
}

recommendations_mapping = {
    "보습 강화": "히알루론산 크림 추천",
    "피지 조절": "저자극 피지 조절 클렌저",
    "항염": "병풀 토너",
    "진정": "알로에 젤",
    "유수분 밸런스": "가벼운 보습 세럼",
    "저자극": "무향, 무색소 제품",
    "모공 관리": "AHA/BHA 토너",
    "안티에이징": "콜라겐 크림",
    "T존 관리": "피지 조절 클렌저",
    "U존 관리": "리치 보습 크림",
    "전체 관리": "복합성 토너",
    "기본 관리": "일반 스킨케어 제품",
    "적절한 세정": "약산성 클렌저",
    "추가 세정 필요": "클렌징 워터 추가",
    "루틴 필요": "기본 스킨케어 루틴 정착",
    "피부 장벽 보호": "세라마이드 크림",
    "강력한 자외선 차단": "SPF 50+ 무기 자외선 차단제",
    "가벼운 자외선 차단": "논코메도제닉 자외선 차단제",
    "약국 제품 보완": "보습 강화 크림",
    "시너지 효과": "기능성 세럼 추가",
    "기능성 관리": "미백 및 주름 개선 세럼",
    "종합 관리": "다기능 케어 제품",
    "안정된 루틴": "꾸준히 사용 가능한 스킨케어"
}

# Generate keywords based on responses
def generate_keywords(row):
    keywords = []
    for question, answer in row.items():
        if question in keywords_mapping and answer in keywords_mapping[question]:
            keywords.extend(keywords_mapping[question][answer])
    return ", ".join(keywords)

# Generate recommendations based on keywords
def generate_recommendations(keywords):
    keywords_list = keywords.split(", ")
    recommendations = [recommendations_mapping[k] for k in keywords_list if k in recommendations_mapping]
    return "; ".join(recommendations)

# Apply logic to dataset
data['추천 키워드'] = data.apply(generate_keywords, axis=1)
data['결과값'] = data['추천 키워드'].apply(generate_recommendations)

# Save completed dataset
data.to_csv("completed_skin_care_recommendations.csv", index=False)
print("Completed dataset saved as 'completed_skin_care_recommendations.csv'")
