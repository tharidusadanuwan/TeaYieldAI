import pandas as pd
from sqlalchemy import create_engine
import os



# PostgreSQL connection

DATABASE_URL = "postgresql://postgres:Admin123@localhost:5432/TeaYieldAI"



engine = create_engine(
    DATABASE_URL
)





query = """

SELECT

s.field_id,

s.ph_level,

s.nitrogen,

s.phosphorus,

s.potassium,

s.moisture,

s.organic_matter,


w.temperature,

w.humidity,

w.rainfall,


f.fertilizer_type,


f.quantity,


f.nitrogen_content,

f.phosphorus_content,

f.potassium_content,


y.tea_weight,


y.quality_grade


FROM soil_data s


JOIN weather_data w

ON s.field_id = w.field_id



JOIN fertilizer_usage f

ON s.field_id = f.field_id



JOIN yield_records y

ON s.field_id = y.field_id


"""





# Load data

df = pd.read_sql(

    query,

    engine

)





print(
    "Dataset Created"
)



print(
    df.head()
)





# Rename target column


df.rename(

    columns={

        "fertilizer_type":
        "recommended_fertilizer"

    },

    inplace=True

)







# Save dataset


BASE_DIR = os.path.dirname(__file__)



OUTPUT = os.path.join(

    BASE_DIR,

    "fertilizer_dataset.csv"

)





df.to_csv(

    OUTPUT,

    index=False

)




print(
    "Saved:",
    OUTPUT
)