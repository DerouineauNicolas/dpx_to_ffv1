
def is_ffmpeg_available():
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which("ffmpeg") is not None

def encode_dpx_scans(path, output, num_scan, offset, fps, num_decimal=3):
    print("Encoding is starting")
    print(path)
    print(output)
    print(num_scan)
    print(offset)
    print(fps)

    # Ref command for ffv1 encoding
    #ffmpeg -y -framerate 24 -start_number 12487 
    # -i folder/%06d.dpx 
    # -vframes 3919 -vcodec ffv1 -level 3 -threads 32 -coder 1 -context 1 -g 1 -slices 24 -slicecrc 1 
    # -r 24 test.mkv