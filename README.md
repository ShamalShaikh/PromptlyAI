# FastTextGenAPI

FastTextGenAPI is a FastAPI-based service for generating text using a language model. It leverages the power of Hugging Face's Transformers to provide a scalable and efficient text generation API.

## Features

- **Text Generation**: Generate coherent text based on a given prompt.
- **Batch Processing**: Efficiently handle multiple requests simultaneously.
- **Logging and Monitoring**: Track requests and responses for analysis and improvement.

## Getting Started

### Prerequisites

- Python 3.7+
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/FastTextGenAPI.git
   cd FastTextGenAPI
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the FastAPI Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

### Sending Batch Requests

Use the `send_batches.py` script to send batch requests to the API:

```bash
python send_batches.py
```

### Testing

Run tests using pytest:

```bash
pytest tests
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/) 