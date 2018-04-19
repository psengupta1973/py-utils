import sys
import os


# Count number of lines in a file
def countLines(fileName):
	try:
                  inFile = open(fileName, 'r');
                  lines = inFile.readlines();
                  c = len(lines);
                  inFile.close();
                  for line in lines:
                    if line.strip().startswith('//') or len(line.strip()) == 0:
                        c = c-1;
                  return c;
	except IOError:
		print("IO_ERROR: "+fileName);
	return 0;


# search all files by their types and count number of lines in each file
def search(lines, fileType):
	outFile = open(fileType+'.csv', 'w');
	i=0;
	for line in lines:
		if line.endswith("."+fileType, 0, len(line)-1):
			i = i + 1;
			fileName = line[0 : len(line)-1];
			c = countLines(fileName);
			if c > 0:
				line = str(i) +','+ fileName +','+ str(c)+"\n";
				outFile.write(line);
			else:
				i = i -1;
	outFile.close();
	print(fileType+": "+ str(i)+ str(' (Report file: '+fileType+'.csv)'));
	if i == 0:
		os.remove(fileType+'.csv');		# remove files with zero lines
	return i;


# get all file types and prepare set
def getExtensions(lines, selectedTypes):
    extSet = set();
    for line in lines:
        extPos = line.rfind(".", 1);
        if extPos > -1:
            ext = line[extPos+1:line.find("\n")];
            if (ext not in extSet) and (ext.find("/") == -1) and (ext.find("\\") == -1 and (ext in selectedTypes)):
                extSet.add(ext);
    print('EXT: ' + str(extSet));
    print('TOTAL EXT: '+ str(len(extSet)));
    return extSet;


# find all files and prepare master list in _find.dat
def prepareLists(selectedTypes):
    find_command = 'dir '+sys.argv[1]+' /s /b > '+'_find.dat';
    #print(find_command);
    os.system(find_command);
    try:
        inFile = open('_find.dat', 'r');
        lines = inFile.readlines();
        inFile.close();
    except (IOError, UnicodeDecodeError) as e:
        print("ERROR: "+str(e)+"; FILE: "+fileName);
        return 0;
    typeSet = getExtensions(lines, selectedTypes);
    typeList = list(typeSet);
    typeList.sort();
    totalCount=0;
    for t in typeList:
          totalCount = totalCount + search(lines, t);
    print("TOTAL FILES: "+ str(totalCount));


def main():
	if len(sys.argv) < 2:
		print('Usage: python ana.py <path> [<type1> <type2>...<typeN>]');
		return;
	#types = findExtensions(lines);
	types = ['java', 'jsp', 'xsd', 'xml', 'sql', 'css', 'less', 'html', 'js', 'json', 'properties', 'sh', 'jar', 'groovy', 'MF', 'vt', 'svg','eot', 'woff', 'txt', 'png', 'jpg', 'ttf', 'gif', 'zip', 'map', 'gzip', 'md', 'yml', 'pom'];
	types.sort();
	if len(sys.argv) > 2:
		types = sys.argv[2:];
	prepareLists(types);

main();

# find ./sybilla -type f -printf "%f\n" > _tmp.dat
# dir <path> /s /b
# for /r %i in (*) do @echo %~nxi

