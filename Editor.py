import os
from moviepy import VideoFileClip, ImageSequenceClip, vfx, CompositeVideoClip, concatenate_videoclips

class videoBulkEditor:
    def __init__(self):
        
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
    
    def remove_sound(self, videoPathList, writeout = False):
        
        
        if not len(videoPathList):
            print("No folders available")
            print()
            return
        
        for videosPath in videoPathList:
            
            listDir = os.listdir(videosPath)
            
            print('We are working on the following videos: ')
            print(listDir)
            print()
            
            if not len(listDir):
                continue
            
            else:
            
                
                    for videoPath in listDir:
                        try:
                            if '.mp4' not in videoPath:
                                continue 
                            
                            print(f"Editing {videosPath}/{videoPath}................")
                            print()
                            clip = VideoFileClip(f'{videosPath}/{videoPath}')

                            # remove audio on every video
                            # no video should have audio
                            clipWithoutSound = clip.without_audio()
                            
                            if writeout:
                                
                                if 'nosounds' not in os.listdir(videosPath):
                                    os.mkdir(f'{videosPath}/nosounds')
                                
                                clipWithoutSound.write_videofile(f'{videosPath}/nosounds/{videoPath}')
                    
                        except Exception as error:
                            print(str(error))
                            
                            print()
                            print("File error:", videoPath)
                            print("Those errors appear usually when the .mp4 file is corupted")
                            continueStatement = input('Enter to continue....')
                            print()
                            print()
                            continue
                        
                    
    
    def flip_clips(self, videoPathList, writeout = True):
        
        if not len(videoPathList):
            print("No folders available")
            print()
            return
        
        for videosPath in videoPathList:
            
            listDir = os.listdir(videosPath)
            
            print('We are working on the following videos: ')
            print(listDir)
            print()
            
            if not len(listDir):
                continue
            
            else:
            
                
                    for videoPath in listDir:
                        try:
                            if '.mp4' not in videoPath:
                                continue 
                            
                            print(f"Editing {videosPath}/{videoPath}................")
                            print()
                            clip = VideoFileClip(f'{videosPath}/{videoPath}')

                            # remove audio on every video
                            # no video should have audio
                            clipWithoutSound = clip.without_audio()

                            # flip the clip
                            clipFlipped = clipWithoutSound.with_effects([vfx.MirrorX()])
                            
                            if writeout:
                                
                                if 'flipped' not in os.listdir(videosPath):
                                    os.mkdir(f'{videosPath}/flipped')
                                
                                clipFlipped.write_videofile(f'{videosPath}/flipped/{videoPath}')
                    
                        except Exception as error:
                            print(str(error))
                            
                            print()
                            print("File error:", videoPath)
                            print("Those errors appear usually when the .mp4 file is corupted")
                            continueStatement = input('Enter to continue....')
                            print()
                            print()
                            continue
        
    