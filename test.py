
from phytooracle_data.rgb import RGB_Data
rgb = RGB_Data(season=10)
no_double_lettuce_df = rgb.df[ rgb.df.double_lettuce == 0 ]
treatment_1_no_lettuce_df = no_double_lettuce_df[ no_double_lettuce_df.treatment == 'treatment 1' ]
print("All Plants...")
print("Number of observations by date")
print(rgb.number_observations_by_date())
print("Treatment 1 / no doubles...")
print("Number of observations by date")
print(rgb.number_observations_by_date(df=treatment_1_no_lettuce_df))
print("All Plants...")
print("Number of plants with n observations")
print(rgb.number_plants_with_n_observations())
print("Treatment 1 / no doubles...")
print("Number of plants with n observations")
print(rgb.number_plants_with_n_observations(df=treatment_1_no_lettuce_df))
rgb.plot_number_observations_vs_date_per_column('treatment')
rgb.plot_number_observations_vs_date_per_column('double_lettuce')
