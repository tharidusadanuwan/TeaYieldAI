import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart



SMTP_SERVER = "smtp.gmail.com"

SMTP_PORT = 587


EMAIL_ADDRESS = "tharidusadanuwan100@gmail.com"

EMAIL_PASSWORD = "cers twgf gpdg lxqh"



def send_reset_email(

    receiver_email:str,

    reset_link:str

):


    message = MIMEMultipart()


    message["From"] = EMAIL_ADDRESS


    message["To"] = receiver_email


    message["Subject"] = (

        "TeaYield AI - Password Reset"

    )



    html = f"""

    <html>

    <body

    style="

    font-family:Arial;

    background:#f3f4f6;

    padding:30px;

    "

    >


    <div

    style="

    max-width:600px;

    margin:auto;

    background:white;

    padding:30px;

    border-radius:15px;

    "

    >


    <h2

    style="

    color:#166534;

    "

    >

    TeaYield AI

    </h2>



    <h3>

    Reset Your Password

    </h3>



    <p>

    We received a request to reset your TeaYield AI password.

    </p>



    <p>

    Click the button below to create a new password.

    </p>



    <a

    href="{reset_link}"

    style="

    display:inline-block;

    background:#15803d;

    color:white;

    padding:13px 22px;

    border-radius:8px;

    text-decoration:none;

    font-weight:bold;

    "

    >

    Reset Password

    </a>



    <p

    style="

    margin-top:25px;

    color:#6b7280;

    "

    >

    This link expires in 30 minutes.

    </p>



    <p

    style="

    color:#6b7280;

    "

    >

    If you did not request a password reset, you can ignore this email.

    </p>


    </div>


    </body>

    </html>

    """



    message.attach(

        MIMEText(

            html,

            "html"

        )

    )



    server = smtplib.SMTP(

        SMTP_SERVER,

        SMTP_PORT

    )



    server.starttls()



    server.login(

        EMAIL_ADDRESS,

        EMAIL_PASSWORD

    )



    server.sendmail(

        EMAIL_ADDRESS,

        receiver_email,

        message.as_string()

    )



    server.quit()