import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://devsdav-web.up.railway.app/",
    cors_allowed_origins=["https://devsdav-web.vercel.app/", "http://localhost:3000/"]
)