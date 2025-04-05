import os
from Editor import videoBulkEditor

class IOManagement:
    def __init__(self, parentFolder : str):
        self.parentFolder = parentFolder
        self.folders = list()

        self.actions = {
            'nosound' : self.removesound,
            'reverse' : self.reverse,
            'flipped' : self.flip,
            'reverse + flipped' : self.reverse_flip,
            'fade': self.fadeEffect
        }
        
        self.currentAction = None
        
        self.VideoEditor = videoBulkEditor() 
        
    def substractFolders(self, folderList):
        
        folderList = [int(index) for index in folderList.split(',')]
        
        print('Those are the selected folders:')
        
        for index, folder in enumerate(os.listdir(f'./{self.parentFolder}')):
            if os.path.isdir(f'./{self.parentFolder}/{folder}') and index in folderList:
                self.folders.append(f'./{self.parentFolder}/{folder}')
                print(f'--------- ./{self.parentFolder}/{folder}')
                
                
    def initiateCommandLine(self):
        print("\n\nYou have available the following folders:")
        
        for index, folder in enumerate(os.listdir(f'./{self.parentFolder}')):
            if os.path.isdir(f'./{self.parentFolder}/{folder}'):
                print(f'{index}.', folder)
                
        command = input("\nSelect one or more (eg. '1,2' |  '3'): ")
        
        self.substractFolders(command)
        
        self.selectAction()
        
    def removesound(self, pathList):
        self.VideoEditor.remove_sound(pathList, writeout=True)
    
    def reverse(self, pathList):
        self.VideoEditor.reverse_clips(pathList)
    
    def flip(self, pathList):
        self.VideoEditor.flip_clips(pathList)
        
    
    def reverse_flip(self, pathList):
        self.removesound(pathList)
        pass
    
    def fadeEffect(self, pathList):
        self.removesound(pathList)
        pass
        
        
    def selectAction(self):
        
        print('\n\nPlease, select the action you want to take:')
        for index, action in enumerate(self.actions.keys()):
            print(f'{index}.', action)
        
        actionIndex = int(input(''))
        
        actionName = list(self.actions.keys())[actionIndex]
        print(f"\n\nYou have selected '{actionName}' ")
        
        self.currentAction = self.actions[actionName]
    
        self.initiateAction()

    def initiateAction(self):
        print('Current state:')
        
        print("Folders selected: ", self.folders)
        print("Current action: ", self.currentAction.__name__, '\n')
        
        
        while True:
            
            continueStatement = input("Do you want to continue? y (yes), n (no): ")
            
            if continueStatement == 'y' or continueStatement == 'yes':
                self.currentAction(self.folders)
                break
            
            if continueStatement == 'n' or continueStatement == 'no':
                break

        