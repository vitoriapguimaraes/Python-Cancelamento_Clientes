"""
# Customer Churn Analysis and Reduction for Subscription Service
A company with over 800,000 customers noticed that most of its customer base is inactive, meaning they have already canceled the service. To improve results, the company wants to understand the main reasons for these cancellations and the most effective actions to reduce this number.
"""

import os
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.io as pio
from fpdf import FPDF
from PIL import Image

def load_and_clean_data(dataset_path):
    """Load dataset and perform initial cleaning."""
    df = pd.read_csv(dataset_path)
    df = df.drop("CustomerID", axis=1)
    print("Initial dataset loaded:")
    print(df)
    print("\nData info before cleaning:")
    print(df.info())
    df = df.dropna()
    print("\nData info after removing missing values:")
    print(df.info())
    return df

def plot_histograms(df, output_dir):
    """Plot and save histograms for each feature by churn."""
    print("\nPlotting histograms for each feature by churn and saving as PNG...")
    os.makedirs(output_dir, exist_ok=True)
    print(f"HISTOGRAM folder created: {output_dir}")
    png_files = []
    for column in df.columns:
        if column != "cancelou":
            fig = px.histogram(df, x=column, color="cancelou", width=600)
            png_path = os.path.join(output_dir, f"hist_{column}.png")
            pio.write_image(fig, png_path, format="png")
            png_files.append(png_path)
            print(f"Saved: {png_path}")
    return png_files

def compile_pdf(png_files, pdf_path):
    """Compile all PNGs into a single PDF."""
    pdf = FPDF()
    for png_file in png_files:
        cover = Image.open(png_file)
        width, height = cover.size
        width, height = width * 0.264583, height * 0.264583
        pdf.add_page()
        pdf.image(png_file, 0, 0, width, height)
    pdf.output(pdf_path, "F")
    print(f"PDF with all histograms saved as: {pdf_path}")

def main():
    DATASET_PATH = "../dataset/cancelamentos_sample.csv"
    png_base_dir = "../results"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    png_dir = os.path.join(png_base_dir, timestamp)
    pdf_path = os.path.join(png_dir, "all_histograms.pdf")

    df = load_and_clean_data(DATASET_PATH)
    png_files = plot_histograms(df, png_dir)
    compile_pdf(png_files, pdf_path)

if __name__ == "__main__":
    main()
