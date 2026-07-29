import pandas as pd

from sqlalchemy import text

from database import SessionLocal


from backend.ai.fertilizer.feature_engineering import create_features






def load_dataset():


    db = SessionLocal()



    try:


        print(
            "Loading AI dataset..."
        )




        query = """

        SELECT


        y.field_id,


        y.harvest_date,


        y.tea_weight AS tea_yield,



        w.temperature,

        w.humidity,

        w.rainfall,

        w.wind_speed,

        w.weather_condition,



        s.ph_level,

        s.nitrogen,

        s.phosphorus,

        s.potassium,



        f.quantity AS fertilizer_amount



        FROM yield_records y



        LEFT JOIN weather_data w


        ON 

        y.field_id = w.field_id

        AND

        DATE(y.harvest_date)

        =
        
        DATE(w.recorded_date)





        LEFT JOIN soil_data s


        ON

        y.field_id = s.field_id





        LEFT JOIN fertilizer_usage f


        ON

        y.field_id = f.field_id



        """





        result = db.execute(
            text(query)
        )



        df = pd.DataFrame(

            result.fetchall(),

            columns=result.keys()

        )






        if df.empty:


            print(
                "No dataset found"
            )


            return pd.DataFrame()






        print(
            "Raw Dataset:"
        )


        print(
            df.head()
        )








        # ==========================
        # FEATURE ENGINEERING
        # ==========================


        df = create_features(
            df
        )






        print(
            "Feature Dataset:"
        )


        print(
            df.head()
        )



        return df





    except Exception as e:


        print(
            "Dataset loading error:",
            e
        )


        return pd.DataFrame()




    finally:


        db.close()