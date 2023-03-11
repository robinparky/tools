import sys
import os
    
def fix_ms2(input_ms2_file: str, output_mgf_file: str):
    invalid_start = ('cr', 'in', 'us', 'lo', 'GP', 'ti')
    invalid_end = ('.ms2\n', 'ne\n')
    with open(input_ms2_file) as input:
        with open(output_mgf_file, 'w') as output:
            for line in input:
                if line.startswith(invalid_start) or line.endswith(invalid_end):
                    continue
                output.write(line)
                
def main():

    mapfile = sys.argv[1]
    backup = sys.argv[1] + ".orig"
    os.rename(sys.argv[1], backup)        
    fix_ms2(backup, mapfile)    
    # fix_ms2('/home/ip2/data/MIDIA/7806_complte_feather/ms2_no_min_score_limit/pfp001/mz_map3.txt', '/home/ip2/data/MIDIA/7806_complte_feather/ms2_no_min_score_limit/pfp001/mz_map-3.txt')    

if __name__ == "__main__":
    main()
    

