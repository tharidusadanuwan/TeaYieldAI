import pandas as pd




def create_features(df):


    df = df.copy()



    # =========================
    # DATE FEATURES
    # =========================


    if "harvest_date" in df.columns:


        df["harvest_date"] = pd.to_datetime(
            df["harvest_date"]
        )


        df["month"] = (
            df["harvest_date"]
            .dt.month
        )


        df["season"] = (
            df["harvest_date"]
            .dt.quarter
        )





    # =========================
    # WEATHER FEATURES
    # =========================


    if "temperature" in df.columns:


        df["temperature_avg"] = (

            df.groupby("field_id")
            ["temperature"]
            .transform(
                "mean"
            )

        )






    if "rainfall" in df.columns:


        df["rainfall_total"] = (

            df.groupby("field_id")
            ["rainfall"]
            .transform(
                "sum"
            )

        )







    # =========================
    # SOIL QUALITY SCORE
    # =========================


    soil_columns = [

        "nitrogen",

        "phosphorus",

        "potassium",

        "ph_value"

    ]



    available = [

        c for c in soil_columns

        if c in df.columns

    ]



    if available:


        df["soil_quality_score"] = (

            df[available]
            .mean(axis=1)

        )







    # =========================
    # FERTILIZER EFFICIENCY
    # =========================


    if (

        "fertilizer_amount" in df.columns

        and

        "tea_yield" in df.columns

    ):


        df["fertilizer_efficiency"] = (

            df["tea_yield"]

            /

            (df["fertilizer_amount"] + 1)

        )







    # =========================
    # PREVIOUS HARVEST
    # =========================


    if "tea_yield" in df.columns:


        df["previous_yield"]=(

            df.groupby("field_id")

            ["tea_yield"]

            .shift(1)

        )


        df["previous_yield"].fillna(

            0,

            inplace=True

        )





    return df