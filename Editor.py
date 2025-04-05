import os
import ffmpeg


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
            
                            if writeout:
                                
                                if 'nosounds' not in os.listdir(videosPath):
                                    os.mkdir(f'{videosPath}/nosounds')
                                
                                (
                                ffmpeg
                                .input(rf"{videosPath}/{videoPath}")
                                .output(f'{videosPath}/nosounds/{videoPath}', preset="ultrafast", threads="6", an=None)
                                .run(overwrite_output=True)
                                )

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

                            
                            if writeout:
                                
                                if 'flipped' not in os.listdir(videosPath):
                                    os.mkdir(f'{videosPath}/flipped')
                                
                                (
                                ffmpeg
                                .input(rf"{videosPath}/{videoPath}")
                                .output(f'{videosPath}/flipped/{videoPath}', vf='hflip', preset="ultrafast", threads="6", an=None)
                                .run(overwrite_output=True)
                                )
                    
                        except Exception as error:
                            print(str(error))
                            
                            print()
                            print("File error:", videoPath)
                            print("Those errors appear usually when the .mp4 file is corupted")
                            continueStatement = input('Enter to continue....')
                            print()
                            print()
                            continue
        
        
    # reverseFlip
    def reverseFlip(self, videoPathList, writeout = True):
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
                            
                            if writeout:

                                if 'rf' not in os.listdir(videosPath):
                                    os.mkdir(f'{videosPath}/rf')
                                
                                (
                                ffmpeg
                                .input(rf"{videosPath}/{videoPath}")
                                .output(f'{videosPath}/rf/{videoPath}', vf='reverse,hflip', preset="ultrafast", threads="6", an=None)
                                .run(overwrite_output=True)
                                )
                    
                        except Exception as error:
                            print(str(error))
                            
                            print()
                            print("File error:", videoPath)
                            print("Those errors appear usually when the .mp4 file is corupted")
                            continueStatement = input('Enter to continue....')
                            print()
                            print()
                            continue


    def reverse_clips(self, videoPathList, writeout = True):
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
                            
                            if writeout:
                                
                                if 'reverted' not in os.listdir(videosPath):
                                    os.mkdir(f'{videosPath}/reverted')
                                
                                (
                                ffmpeg
                                .input(rf"{videosPath}/{videoPath}")
                                .output(f'{videosPath}/reverted/{videoPath}', vf='reverse', preset="ultrafast", threads="6", an=None)
                                .run(overwrite_output=True)
                                )
                    
                        except Exception as error:
                            print(str(error))
                            
                            print()
                            print("File error:", videoPath)
                            print("Those errors appear usually when the .mp4 file is corupted")
                            continueStatement = input('Enter to continue....')
                            print()
                            print()
                            continue
    
    def fadeInOut(self, videoPathList, writeout = True):
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
                        
                        if writeout:
                            
                            if 'fade' not in os.listdir(videosPath):
                                os.mkdir(f'{videosPath}/fade')
                            
                            probe = ffmpeg.probe(rf"{videosPath}/{videoPath}")

                            (
                            ffmpeg
                            .input(rf"{videosPath}/{videoPath}")
                            .filter('fade', t='in', st=0, d=2)
                            .filter('fade', t='out', st=float(probe['format']['duration'])-2, d=2)
                            .output(f'{videosPath}/fade/{videoPath}', preset="ultrafast", threads="6", an=None)
                            .run(overwrite_output=True)
                            )
                
                    except Exception as error:
                        print(str(error))
                        
                        print()
                        print("File error:", videoPath)
                        print("Those errors appear usually when the .mp4 file is corupted")
                        continueStatement = input('Enter to continue....')
                        print()
                        print()
                        continue

            

                if 'fade' in os.listdir(videosPath):
                    with open(f'{videosPath}/fade/file_list.txt', 'w') as f:
                        for fadedClips in os.listdir(f'{videosPath}/fade'):
                            if 'mp4' in fadedClips:
                                f.write(f"file '{fadedClips}'\n")

                    (   
                    ffmpeg
                    .input(f'{videosPath}/fade/file_list.txt', format='concat', safe=0)
                    .output(f'{videosPath}/fade/output_concated.mp4', c='copy', preset="ultrafast", threads=f"{os.cpu_count()}")
                    .run(overwrite_output=True)
                    )

                    os.chdir(rf"{videosPath}/fade/")
                    os.system("del file_list.txt")
                    print(os.getcwd())
                    os.chdir('../../../')          
                    print(os.getcwd())

