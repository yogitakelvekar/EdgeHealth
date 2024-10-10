import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class CardiovascularDataVisualizer:
    def plot_top_5_ccgs_by_mortality_rate(self, top_5_ccgs: pd.DataFrame, output_path: str):
        """ a bar chart of the top 5 CCGs by mortality rates   """
        try:
            plt.figure(figsize=(10, 6))

            # Seaborn barplot
            sns.barplot(x='CCG Name', y='mortality_rate', data=top_5_ccgs, palette='viridis')

            # Add labels and title
            plt.title('Top 5 CCGs with the Greatest Mortality Rates (Heart Disease + Stroke) - 2021', fontsize=14)
            plt.xlabel('Clinical Commissioning Group (CCG)', fontsize=12)
            plt.ylabel('Mortality Rate (Per Population)', fontsize=12)
            plt.xticks(rotation=45, ha='right')

            #source information
            plt.figtext(0.5, -0.1, 'Source: Department of Health and Social Care - 2021 Cardiovascular Health Dataset',
                        wrap=True, horizontalalignment='center', fontsize=10)


            plt.tight_layout()
            plt.savefig(output_path)
            print(f"Chart saved successfully to {output_path}")
        except Exception as e:
            raise Exception(f"Error creating or saving the chart: {e}")
