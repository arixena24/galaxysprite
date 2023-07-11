def compress_video(self, path_output):
    if filename.endswith('.mp4'):
        input_vid = os.path.join(path_output, self)
        output_vid = os.path.join(path_output, f'compressed_{self}' ) #change to correct filename of resulting movie

        ffmpeg_cmd = f'ffmpeg -i {input_vid} -c:v libx265 -c:a copy -crf 24 {output_vid}'
        subprocess.run(ffmpeg_cmd, shell=True)
    return output_vid

