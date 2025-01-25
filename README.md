# Quran Visualization Pattern

A Python-based visualization project that reveals fascinating numerical patterns within the structure of the Quran. This project creates a visual representation of the number of verses (ayat) in each chapter (surah), highlighting specific patterns known as "Lam-Lam-Ha" and "Alif".

![Quran Visualization](preview.png)

## Features

- Visualizes all 114 surahs and their corresponding number of verses
- Highlights the "Lam-Lam-Ha" pattern (orange fill with blue outline)
- Displays the "Alif" pattern (purple outline with orange fill)
- Interactive matplotlib plot with grid lines for easy reference

## Requirements

- Python 3.6+
- pandas
- numpy
- matplotlib

## Installation

1. Clone the repository: 
bash
git clone https://github.com/yourusername/quran-visualization.git
cd quran-visualization

2. Install required packages:
bash
pip install -r requirements.txt

## Usage

1. Make sure both `quran_data.py` and `plot_quran_visualization.py` are in the same directory
2. Run the visualization script:
bash
python plot_quran_visualization.py

The script will generate a plot showing:
- A scatter plot of all surahs (x-axis) and their number of verses (y-axis)
- The "Lam-Lam-Ha" pattern filled in orange with blue outline
- The "Alif" pattern with purple outline and orange fill
- Grid lines for reference

## Project Structure
quran-visualization/
├── plot_quran_visualization.py # Main visualization script
├── quran_data.py # Quran structural data
├── requirements.txt # Python dependencies
├── README.md # This file
└── preview.png # Visualization preview image


## Data Structure

The project uses a simple data structure in `quran_data.py`:


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- Thanks to all contributors who help maintain and improve this visualization
- Special thanks to the Islamic scholars and researchers who study the numerical patterns in the Quran

## Contact

Your Name - [@coretheohmcorps](https://twitter.com/coretheohmcorps)

Project Link: [https://github.com/ohmcorps/quran-visualization](https://github.com/ohmcorps/quran-visualization)

## Note

This visualization is intended for educational and research purposes. The patterns shown are based on the numerical structure of the Quran's chapters and verses.