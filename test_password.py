from utils.security import verify_password


hashed = "$2b$12$e0CkJGrFLRS/g3sdlJt0I.WzvJ99Qd/EemN/tzNPhdwmD2FSWwrn6"


password = "YOUR_REGISTER_PASSWORD"


print(
    verify_password(
        password,
        hashed
    )
)