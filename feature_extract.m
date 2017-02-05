function final_feature = feature_extract(filename1,audiofile)
%obtaining the fields arguments from the fields function
[Begin,End,Emotion]=fields(filename1);
%constructing miraudio for all the  times
n=size(End,1);
j=1;
for i=1:n
    audio(i) = miraudio(audiofile,'Extract',Begin(i),End(i));
    if Begin(i)~=End(i)
        chroma = mirchromagram(audio(i));
        chroma_feat(j) = mirstat(chroma);
        rms_feat(j) = mirgetdata(mirrms(audio(i)));
        tempo_feat(j) = mirgetdata(mirtempo(audio(i)));
        j=j+1;
    end
end
        
    
for i=1:(j-1)
    feat_mean_arr = (chroma_feat(i).Mean)'; 
    chroma_cell{i,1} = feat_mean_arr;
    chroma_cell{i,2} = rms_feat(i);
    chroma_cell{i,3} = tempo_feat(i);
    chroma_cell{i,4} = Emotion{i};
end

final_feature = cell2table(chroma_cell);
end

function [Begin,End,Emotion] = fields(filename)

%opening the first clip with reading permission
fileID=fopen(filename,'r');

%reading the values from files into array data types
file_time = textscan(fileID,'%f%f%s%*[^\n\r]','Delimiter',',', 'ReturnOnError', false);
fclose(fileID);
End = file_time{1};
Begin = file_time{2};
Emotion = file_time{3};

end


