from moviepy import VideoFileClip, ImageSequenceClip, vfx, CompositeVideoClip, concatenate_videoclips

class videoBulkEditor:
    def __init__(self, videoListPath : list):
        self.videoPathList = videoListPath
        
        self.editedClips = {
            'nosound' : list(),
            'flipped' : list(),
            'reversed' : list(),
            'fade' : list()
        }
        
        """
        # each editedClips field should contain as follows:
        #
        # nosound: [ { title : "video_name.mp4",  clip: <CLIP Object>  } ]
        # meaning when you access edited.Clips['nosound'][index]['title'] you'll get the name of the file
        # meaning when you access edited.Clips['nosound'][index]['clip'] you'll get the  of the clip object
        """
        
    def remove_sound(self):
        
        if not len(self.videoPathList):
        
            for videoPath in self.videoPathList:
                
                clip = VideoFileClip(videoPath)
                
                self.videoclips_without_sound.append(clip)

    
    def flip_clips(self):
        
        if not len(self.videoclips_without_sound):
            print("There are no videos available for editing. Please, check again.")
            return
        
        
        for videoclip in self.videoclips:
            
            flippedVideo = videoclip.with_effects([vfx.MirrorX()])
        
            flippedVideo.write_videofile(f'../flipped/flipped-{video_name}')
                
    