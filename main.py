from etl.data_extractor import CardiovascularDataExtractor
from etl.data_transformer import CardiovascularDataTransformer
from etl.data_visualizer import CardiovascularDataVisualizer

def run_cardiovascular_etl_pipeline():
    # Define file paths
    input_file = r'C:\Sandbox\EdgeHealth_\data\Cardiovascular_health_indicators_2021_Technical_Exercise_ (2) (1).xlsx'
    output_chart = 'output/top_5_ccgs_mortality_rate_chart.png'

    # Step 1: Extract data
    extractor = CardiovascularDataExtractor(input_file)
    data = extractor.load_data()

    # Step 2: Transform data
    transformer = CardiovascularDataTransformer()
    data = transformer.calculate_total_mortalities(data)
    data = transformer.calculate_mortality_rate(data)
    top_5_ccgs = transformer.get_top_5_ccgs_by_mortality_rate(data)

    # Step 3: Visualize data
    visualizer = CardiovascularDataVisualizer()
    visualizer.plot_top_5_ccgs_by_mortality_rate(top_5_ccgs, output_chart)

if __name__ == "__main__":
    try:
        run_cardiovascular_etl_pipeline()
    except Exception as e:
        print(f"ETL pipeline execution failed: {e}")
