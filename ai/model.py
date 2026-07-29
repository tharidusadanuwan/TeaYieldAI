from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor






def create_random_forest():



    model = RandomForestRegressor(

        n_estimators=200,

        max_depth=10,

        random_state=42,

        n_jobs=-1

    )


    return model






def create_xgboost():



    model = XGBRegressor(

        n_estimators=200,

        learning_rate=0.05,

        max_depth=5,

        random_state=42,

        objective="reg:squarederror"

    )


    return model