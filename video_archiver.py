import cv2
import os
import shutil
import argparse
import sys
from tqdm import tqdm

def extract_screenshots(video_path, output_dir, interval_seconds):
    """
    Extracts screenshots from a video at a specified interval.

    Args:
        video_path (str): Path to the .mov video file.
        output_dir (str): Directory to save the screenshots.
        interval_seconds (int): Time interval in seconds between screenshots.
    """

    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_seconds = frame_count / fps

    success, image = vidcap.read()
    count = 0
    screenshot_count = 0

    progress_bar = tqdm(total=int(duration_seconds // interval_seconds), desc=f"Processing {os.path.basename(video_path)}", unit="screenshot")

    while success:
        current_time = count / fps
        if current_time >= screenshot_count * interval_seconds:
            screenshot_name = os.path.join(output_dir, f"frame_{screenshot_count:04d}.jpg")
            cv2.imwrite(screenshot_name, image)
            screenshot_count += 1
            progress_bar.update(1)

        success, image = vidcap.read()
        count += 1

    progress_bar.close()
    vidcap.release()

def main():
    parser = argparse.ArgumentParser(description="Extract screenshots from .mov files and optionally delete them to save disk space.")
    parser.add_argument("input_dir", help="Directory containing .mov files.")
    parser.add_argument("output_dir", help="Directory to store the screenshots.")
    parser.add_argument("-i", "--interval", type=int, default=60, help="Time interval in seconds between screenshots (default: 60).")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete the original .mov files after processing.")
    parser.add_argument("-a", "--archive", action="store_true", help="Move .mov to archive folder after processing (must provide -ad option).")
    parser.add_argument("-ad", "--archive_dir", help="Directory to move processed .mov files")

    args = parser.parse_args()
    
    if args.archive and not args.archive_dir:
        parser.error("--archive requires --archive_dir to be specified.")
        
    if not os.path.exists(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist.")
        sys.exit(1)

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        
    if args.archive:
        if not os.path.exists(args.archive_dir):
            os.makedirs(args.archive_dir)

    for filename in os.listdir(args.input_dir):
        if filename.endswith(".mov"):
            video_path = os.path.join(args.input_dir, filename)
            video_output_dir = os.path.join(args.output_dir, os.path.splitext(filename)[0])
            
            if not os.path.exists(video_output_dir):
                os.makedirs(video_output_dir)

            extract_screenshots(video_path, video_output_dir, args.interval)

            if args.delete:
                os.remove(video_path)
                print(f"Deleted: {filename}")
            elif args.archive:
                archive_path = os.path.join(args.archive_dir, filename)
                shutil.move(video_path, archive_path)
                print(f"Moved {filename} to {args.archive_dir}")


if __name__ == "__main__":
    main()