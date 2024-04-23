
import supervision as sv

VIDEO_DIR_PATH = f"C:/Users/arn18/Documents/GitHub/40.-MIT--Fire-Flame-and-Smoke-Detection"
IMAGE_DIR_PATH = f"C:/Users/arn18/Documents/GitHub/40.-MIT--Fire-Flame-and-Smoke-Detection/images_data"
FRAME_STRIDE = 10


video_paths = sv.list_files_with_extensions(
    directory=VIDEO_DIR_PATH,
    extensions=["mov", "mp4"])

# TEST_VIDEO_PATHS, TRAIN_VIDEO_PATHS = video_paths[:2], video_paths[2:]
# for video_path in tqdm(TRAIN_VIDEO_PATHS):
#     video_name = video_path.stem
#     image_name_pattern = video_name + "-{:05d}.png"
#     with sv.ImageSink(target_dir_path=IMAGE_DIR_PATH, image_name_pattern=image_name_pattern) as sink:
#         for image in sv.get_video_frames_generator(source_path=str(video_path), stride=FRAME_STRIDE):
#             sink.save_image(image=image)


for video_path in video_paths:
    video_name = video_path.stem
    image_name_pattern = video_name + "-{:05d}.png"
    with sv.ImageSink(target_dir_path=IMAGE_DIR_PATH, image_name_pattern=image_name_pattern) as sink:
        for image in sv.get_video_frames_generator(source_path=str(video_path), stride=FRAME_STRIDE):
            sink.save_image(image=image)