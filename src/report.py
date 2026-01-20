import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_report(df_daily, df_province):
    print("\n--- COVID-19 Argentina Report ---")
    print(f"Total cases (sample): {df_daily['daily_cases'].sum()}")
    print(f"Total deaths (sample): {df_daily['daily_deaths'].sum()}")
    print(f"Average daily mortality rate: {df_daily['mortality_rate'].mean():.2f}%")
    
    # Top provinces by cases
    print("\nTop 5 provinces by cases:")
    print(df_province.nlargest(5, 'total_cases')[['residencia_provincia_nombre', 'total_cases', 'fallecido']])
    
    # Plot daily cases/deaths
    plt.figure(figsize=(14, 8))
    plt.plot(df_daily['fecha_diagnostico'], df_daily['daily_cases'], label='Daily Cases', color='blue')
    plt.plot(df_daily['fecha_diagnostico'], df_daily['daily_deaths'], label='Daily Deaths', color='red')
    plt.title('COVID-19 Argentina - Daily Cases and Deaths')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend()
    plt.grid()
    
    output_path = os.path.join('data', 'processed', 'covid_report_plot.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.show()
    
    print(f"Report plot saved to {output_path}")