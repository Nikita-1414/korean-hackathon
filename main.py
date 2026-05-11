# Define the resume data
resume_data = {
    "01": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning",
    "02": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS",
    "03": "Java, Spring Boot, MySql, Microservices, Docker, kubernates",
    "04": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib",
    "05": "C++, Algoritms, Data Structure, competitive programming, python",
    "06": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD",
    "07": "Python, Sklearn, XGboost, feature engineering, SQL, tableau",
    "08": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma",
    "09": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest",
    "10": "python, R, statistics, ML, regression, clustering, Power-BI"
}

# Define the SKILL_ALIASES mapping
SKILL_ALIASES = {
    # Languages
    "python": "python",
    "pyhton": "python",
    "java": "java",
    "javascript": "javascript",
    "javascrpit": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "typescrpit": "typescript",
    "c++": "cpp",
    "cpp": "cpp",
    "r": "r",
    "kotlin": "kotlin",

    # ML / Data
    "machinelearning": "machine_learning",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "sklearn": "machine_learning",
    "deeplearning": "deep_learning",
    "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch",
    "keras": "keras",
    "nlp": "nlp",
    "bert": "bert",
    "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics",
    "stats": "statistics",
    "regression": "regression",
    "clustering": "clustering",
    "data-viz": "data_visualization",
    "data visualization": "data_visualization",
    "data viz": "data_visualization",
    "matplotlib": "data_visualization",
    "tableau": "data_visualization",
    "power-bi": "data_visualization",
    "power bi": "data_visualization",
    "powerbi": "data_visualization",
    "pandas": "pandas",
    "numpy": "numpy",

    # Web — Frontend
    "react": "react",
    "reacts": "react",
    "reactjs": "react",
    "vue": "vue",
    "vue.js": "vue",
    "vuejs": "vue",
    "redux": "redux",
    "tailwind": "tailwind",
    "html/css": "html_css",
    "html css": "html_css",
    "html": "html_css",
    "css": "html_css",
    "jest": "jest",
    "graphql": "graphql",

    # Web — Backend
    "node.js": "nodejs",
    "nodejs": "nodejs",
    "node js": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot",
    "springboot": "spring_boot",
    "rest api": "rest_api",
    "rest": "rest_api",
    "restapi": "rest_api",
    "microservices": "microservices",

    # Databases
    "sql": "sql",
    "mysql": "mysql",
    "mysq": "mysql",
    "postgresql": "postgresql",
    "postgres": "postgresql",
    "mongodb": "mongodb",
    "redis": "redis",

    # DevOps / Cloud
    "docker": "docker",
    "kubernetes": "kubernetes",
    "kubernates": "kubernetes",
    "k8s": "kubernetes",
    "ci/cd": "ci_cd",
    "cicd": "ci_cd",
    "ci cd": "ci_cd",
    "aws": "aws",

    # Mobile
    "android": "android",
    "firebase": "firebase",

    # CS Fundamentals
    "algorithms": "algorithms",
    "algoritms": "algorithms",
    "data structure": "data_structures",
    "data structures": "data_structures",
    "competitive programming": "competitive_programming",

    # Design
    "ui/ux": "ui_ux",
    "ui ux": "ui_ux",
    "figma": "figma",
}


def normalize_skills(raw_skills):
    text = raw_skills.lower()

    # Step 1: Try multi-word phrases FIRST (before splitting)
    multi_word_keys = sorted(
        [k for k in SKILL_ALIASES if " " in k or "-" in k or "/" in k],
        key=len, reverse=True  # longest first to avoid partial matches
    )
    replacements = {}
    for phrase in multi_word_keys:
        if phrase in text:
            placeholder = phrase.replace(" ", "_").replace("-", "_").replace("/", "_")
            replacements[placeholder] = SKILL_ALIASES[phrase]
            text = text.replace(phrase, placeholder)

    # Step 2: Split on commas
    tokens = [t.strip() for t in text.split(",")]

    # Step 3: Map each token
    normalized = []
    for token in tokens:
        token = token.strip()
        if token in replacements:
            normalized.append(replacements[token])
        elif token in SKILL_ALIASES:
            normalized.append(SKILL_ALIASES[token])
        # else: discard (not in alias map)

    return normalized


# Normalize all resumes
normalized_resume_data = {}
for key, value in resume_data.items():
    normalized_resume_data[key] = normalize_skills(value)

# Deduplicate (preserve order with dict trick)
deduplicated_resume_data = {}
for key, value in normalized_resume_data.items():
    seen = []
    for skill in value:
        if skill not in seen:
            seen.append(skill)
    deduplicated_resume_data[key] = seen

# Print results
print("=== Normalized & Deduplicated Skills ===")
for candidate_id, skills in deduplicated_resume_data.items():
    print(f"Resume {candidate_id}: {skills}")
