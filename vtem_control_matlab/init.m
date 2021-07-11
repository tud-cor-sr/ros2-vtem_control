% set RMW Implementation
setenv('RMW_IMPLEMENTATION','')

% load custom messages
pkgFolderPath = fullfile(pwd, "..\");
ros2genmsg(pkgFolderPath)

% parameters
vtemDeviceAddress = "192.168.1.101";
vtemPort = 502;