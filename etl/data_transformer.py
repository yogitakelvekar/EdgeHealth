import pandas as pd


class CardiovascularDataTransformer:
    def calculate_total_mortalities(self, data: pd.DataFrame) -> pd.DataFrame:
        """ Add a total_mortalities column by summing stroke and heart disease mortalities for all ages  """
        data['total_stroke_mortalities'] = data['Number of stroke mortalities (under 75 yrs)'] + \
                                           data['Number of stroke mortalities (75 yrs and above)']
        data['total_heart_disease_mortalities'] = data['Number of  Heart Disease mortalities (under 75 yrs)'] + \
                                                  data['Number of  Heart Disease mortalities (over 75 yrs)']
        data['total_mortalities'] = data['total_stroke_mortalities'] + data['total_heart_disease_mortalities']
        return data

    def calculate_mortality_rate(self, data: pd.DataFrame) -> pd.DataFrame:
        """ Add a mortality_rate column by dividing total mortalities by the population of the area.
        Assumed that  population data is available in 'Population in Area (under 75yrs)' and 'Population in Area (75yrs and above)'.
        """
        # Calculate total population by summing under 75 , over 75 populations
        data['total_population'] = data['Population in Area (under 75yrs)'] + data[
            'Population in Area (75yrs and above)']

        # Calculate mortality rate as total mortalities divided by total population
        data['mortality_rate'] = data['total_mortalities'] / data['total_population']
        return data

    def get_top_5_ccgs_by_mortality_rate(self, data: pd.DataFrame) -> pd.DataFrame:
        """ top 5 Clinical Commissioning Groups (CCGs) with the greatest mortality rates."""

        top_5_ccgs = data[['CCG Name', 'mortality_rate']].sort_values(by='mortality_rate', ascending=False).head(5)
        return top_5_ccgs
