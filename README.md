# Video Archiver

## Description

Video Archiver is a command-line utility that helps you manage disk space by archiving .mov video files. It extracts screenshots from videos at specified intervals, allowing you to delete or archive the original videos while retaining visual representations of their content. This is especially useful for archiving large video files where the entire video may not be needed, but having periodic snapshots is beneficial.

## Features

*   Extracts screenshots from .mov video files.
*   Customizable screenshot interval.
*   Option to automatically delete original .mov files after processing.
*   Option to archive original .mov files to another directory.
*   Progress bar to visualize the processing of each video.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Requirements

*   Python 3.7+
*   `opencv-python`
*   `tqdm`

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python video_archiver.py <input_directory> <output_directory> [options]