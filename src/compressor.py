import os
import ffmpeg
import subprocess

def compress_video(video_path, size_goal_KB):
    """Compress resulting video to deisred file size in KB. 

    Args:
        video_path (str): path to video or animation created in earlier function. 
        size_goal_KB (_type_): specified file size upper limit. 

    Returns:
        output_vid: location of outputted compressed video. 
    """
    filename, extension = os.path.splitext(video_path)
    extension = '.mp4'

    probe = ffmpeg.probe(video_path)
    duration = float(probe['format']['duration'])
    target_total_bitrate = (size_goal_KB * 1024 * 8) / (1.073741824 * duration)
    video_bitrate = target_total_bitrate

    if filename.endswith('.mp4'):
        i = ffmpeg.input(video_path)
        output_vid = os.path.join(f'{filename}_compressed' ,{extension}) #change to correct filename of resulting movie
        ffmpeg.output(i, output_vid,
                          **{'c:v': 'libx264', 'b:v': video_bitrate}
                          ).overwrite_output().run()
    return output_vid




# Simplified version and explanation at: https://stackoverflow.com/a/64439347/12866353

