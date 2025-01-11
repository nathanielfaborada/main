import threading
import time
import random

class VirtualCamera:
    def __init__(self, vr_cameras):
        
        self.vr_cameras = vr_cameras
        # Camera status: True means available, False means in use
        self.camera_status = {camera: True for camera in vr_cameras}
        # Platform status: True means available, False means in use
        self.platform_status = {}
        # Lock to ensure no two threads access the critical section at the same time
        self.lock = threading.Lock() 

    def use_camera(self, camera, platform):
        with self.lock:
            # Check if the camera or platform is not available
            if not self.camera_status[camera] or not self.platform_status.get(platform, True):
                print(f"Virtual Camera {camera} is Unavailable on {platform}.")
                return  # If the camera or platform is unavailable

            #  the camera and platform is ginagamit
            print(f"Virtual Camera {camera} is now active on {platform}.")
            time.sleep(3)
            self.camera_status[camera] = False 
            self.platform_status[platform] = False 

        
        time.sleep(3)

        # when done using the camera and platform, make them available again
        with self.lock:
            self.camera_status[camera] = True  # Camera is available again
            self.platform_status[platform] = True  # Platform is available again
            print(f"Virtual Camera {camera} operation on {platform} completed and is now available.")
            
    def assign_cameras(self, iterations=10):
        platforms = ["Zoom", "Teams", "Skype", "Discord"]

        
        for i in range(iterations):
            print(f"\n--- Iteration {i + 1} ---")
            threads = []  # List to keep track of all the threads

            for i in range(len(self.vr_cameras)):
               
                with self.lock:
                    available_cameras = [cam for cam in self.vr_cameras if self.camera_status[cam]]
                    available_platforms = [platform for platform in platforms if self.platform_status.get(platform, True)]
                    
                    if available_cameras and available_platforms:
                        camera = random.choice(available_cameras)
                        platform = random.choice(available_platforms)

                    # Create a new thread to do using the camera on the platform
                        thread = threading.Thread(target=self.use_camera, args=(camera, platform))
                        threads.append(thread)
                        thread.start()

            # Wait for all threads to complete their tasks
            for thread in threads:
                thread.join()


if __name__ == "__main__":
	virtual_cameras_list = ["0", "1", "2", "3", "4"] 
	vc = VirtualCamera(virtual_cameras_list)
	vc.assign_cameras(iterations=10)
