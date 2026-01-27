# AI-Based Traffic Management System

An intelligent traffic management solution using YOLOv8 computer vision for real-time vehicle detection, traffic density analysis, and automated signal control.

## Features

- **Vehicle Detection**: Real-time detection and tracking of vehicles using YOLOv8
- **Traffic Analysis**: Analyzes vehicle density and classifies congestion levels
- **Signal Control**: Intelligent traffic signal optimization based on traffic density
- **Web Interface**: User-friendly dashboard for traffic monitoring and analysis
- **Video Processing**: Supports MP4, AVI, MOV, and MKV video formats
- **Real-time Visualization**: Visual overlay of detected vehicles and traffic data

## Project Structure

```
.
├── app.py                      # Flask web application
├── web_processor.py            # Video processing logic
├── src/
│   ├── vehicle_detector.py     # YOLOv8-based vehicle detection
│   ├── traffic_analyzer.py     # Traffic density analysis
│   ├── signal_controller.py    # Signal control logic
│   ├── visualizer.py           # Visualization utilities
│   └── config.py               # Configuration settings
├── templates/                  # HTML templates
├── static/                     # CSS and JavaScript files
├── models/                     # Model weights directory
└── sample_videos/              # Sample video files for testing
```

## Installation

### Requirements
- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd AI-Based-Traffic-Management-System
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Start the Web Server
```bash
python app.py
```
The application will be available at `http://localhost:5000`

### Upload and Analyze Videos
1. Navigate to the web interface
2. Upload a traffic video
3. The system will detect vehicles and analyze traffic patterns
4. View results with visual overlays and analytics

## Technologies Used

- **YOLOv8**: Object detection model for vehicle detection
- **OpenCV**: Computer vision and image processing
- **Flask**: Web framework
- **NumPy & Pandas**: Data processing
- **Python**: Core programming language

## Key Modules

| Module | Purpose |
|--------|---------|
| `vehicle_detector.py` | Detects and tracks vehicles in video frames |
| `traffic_analyzer.py` | Analyzes vehicle density per zone and classifies congestion |
| `signal_controller.py` | Controls traffic signal timing based on traffic density |
| `visualizer.py` | Creates visual overlays and output videos |

## Configuration

Edit `src/config.py` to customize:
- Detection model path
- Confidence thresholds
- Video processing parameters
- Traffic zones definition

## License

See LICENSE file for details.
