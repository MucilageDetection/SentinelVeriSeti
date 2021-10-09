% Bahri ABACI
% Save extracted IMG_DATA folder as Matlab mat file

% folder to unzip
Directory = 'E:/Dropbox/Dataset/satellite/sentinel2/';
SentinelGrids = {'35TPF', '35TPE'};
ResolutionList = {'R20m','R60m'};

% go over the all grids
for g = 1:length(SentinelGrids)
    gridName = SentinelGrids{g};
    
    % set the input and output directory
    InputDirectory = fullfile(Directory, strcat(gridName, '_IMGDATA'));
    OutputDirectory = fullfile(Directory, strcat(gridName, '_MATDATA'));

    % create output directory
    if ~isfolder(OutputDirectory)
        fprintf('Creating output directory...');
        mkdir(OutputDirectory);
    end
    
    FileList = dir(InputDirectory);
    FileList(1:2) = [];
    for f = 1:length(FileList)
        files = FileList(f).name;
        
        % set the output file directory
        InputFileDirectory = fullfile(InputDirectory, files);
        OutputFileDirectory = fullfile(OutputDirectory, files);
        
        % create output directory
        if ~isfolder(OutputFileDirectory)
            fprintf('Creating output file directory...\n');
            mkdir(OutputFileDirectory);
        end
        
        % go over all resolutions
        for r = 1:length(ResolutionList)
            resolutions = ResolutionList{r};
            % create array
            SentinelData.date   = files(12:19);
            SentinelData.year   = str2double(files(12:15));
            SentinelData.month  = str2double(files(16:17));
            SentinelData.day    = str2double(files(18:19));
            SentinelData.group = files(20:26);
            SentinelData.tile  = files(39:44);
    
            fprintf('creating %s.mat for %s\n', resolutions, files);
            
            jp2Files = dir(fullfile(InputFileDirectory, resolutions));
            jp2Files(1:2) = [];
            for j = 1:length(jp2Files)
                jpFileName = jp2Files(j).name;
                BandName = jpFileName(24:26);
                SentinelData.(BandName) = imread(fullfile(InputFileDirectory, resolutions, jpFileName));
            end
            
            % save the image
            save(fullfile(OutputFileDirectory, strcat(resolutions, '.mat')), 'SentinelData');
        end
    end
end
% goodbye
fprintf('Done\n');
