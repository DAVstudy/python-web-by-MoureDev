import reflex as rx


# Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "avatar.png"

_meta = [
        {"name": "og:type", "content": "website"},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@devsdav"}
    ]

# Index 
index_title = "DevsDav | Aprendiendo a Programar"
index_description = "Hola soy DevsDav, Ingeniero Electrónico que esta aprendiendo a programar"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)


# Cursos
courses_title = "DevsDav | Cursos realizados"
courses_description = "Estos son los cursos que he completado en mi formación autodidacta"

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)