# Image Optimizer

This repository contains a simple web application for optimizing images using Streamlit and PIL. The application allows users to upload an image in PNG, JPG, or JPEG format and converts it to an optimized WebP format.

## Features

- **Image Upload**: Users can upload images in PNG, JPG, or JPEG format.
- **Image Optimization**: The uploaded image is converted and optimized to WebP format.
- **Download Optimized Image**: Users can download the optimized WebP image.

## Technologies Used

- **[Streamlit](https://streamlit.io/)**: For building the web application.
- **[PIL (Pillow)](https://python-pillow.org/)**: For image processing.
- **[WebP](https://pypi.org/project/webp/)**: For saving images in WebP format.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/image-optimizer.git
   cd image-optimizer
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure your `requirements.txt` contains:
   ```text
   streamlit
   pillow
   webp
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501` to use the application.


## Contributing

Contributions are welcome! If you have any ideas or suggestions to improve the project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
