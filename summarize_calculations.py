import numpy as np
import sys as sys
from os import listdir, getcwd, path, chdir


"""
python3 summarize_calculations.py element_name folder_name functional(opt, PS) correction(opt, D3)

A summary of the calculations is created, specific for each case, with the creating of a summary file.
No resources are needed for these computations.
"""


# Loading name of the compound, the name of the folder and IBRION (optional)


element = sys.argv[1]

folder_name = sys.argv[2]

functional = 'PS'
if len(sys.argv) > 3:
    functional = sys.argv[3]

correction = 'D3'
if len(sys.argv) > 4:
    correction = sys.argv[4]

flag = functional
if len(correction):
    flag = f'{functional}+{correction}'

dir_path = f'../{element}/{folder_name}'


# Loading the information


if folder_name == 'convergence':
    for folder in listdir(dir_path):
        try:  # Loading the OSZICAR file
            with open(f'{dir_path}/{folder}/OSZICAR', 'r') as OSZICAR_file:
                OSZICAR_lines = OSZICAR_file.readlines()

            # Getting the data of the convergence
            
            aux = folder.split('eV_')
            E_cutoff = float(aux[0])
            KPoints = int(aux[1].split('KP')[0])

            # Getting the last converged energy
            
            energy = OSZICAR_lines[-1].split('=')[1]
            
            # Removing the units and appending
            
            energy = float(energy.split()[0])
            print(E_cutoff, KPoints, energy)
        except (FileNotFoundError, NotADirectoryError):
            pass
        except IndexError:
            print(f'### Caution, simulation not finished at {folder}')


elif folder_name == 'relaxation':
    for folder in listdir(dir_path):
        try:  # Loading the CONTCAR file
            with open(f'{dir_path}/{folder}/CONTCAR', 'r') as CONTCAR_file:
                CONTCAR_lines = CONTCAR_file.readlines()
            
            # Getting the data of the convergence
            
            aux = folder.split('+')
            if len(aux) > 1:
                functional = aux[0]
                correction = aux[1]
            else:
                functional = folder
                correction = 'None'
            
            # Getting the relaxed parameters
            
            scale = CONTCAR_lines[1][:-1]
            a = CONTCAR_lines[2].split()[0]
            b = CONTCAR_lines[3].split()[1]
            c = CONTCAR_lines[4].split()[2]

            # Appending
            
            print(functional, correction, scale, a, b, c)
        except (FileNotFoundError, NotADirectoryError):
            pass
        except IndexError:
            print(f'### Caution, simulation not finished at {folder}')


elif folder_name == 'gamma_point':
    try:  # Loading the OUTCAR file
        with open(f'{dir_path}/{flag}/OUTCAR', 'r') as OUTCAR_file:
            OUTCAR_lines = OUTCAR_file.readlines()

        # Checking for the lines with imaginary (negative) phonon frequencies

        minimum_real = None
        for line in OUTCAR_lines:
            try:
                split_line = line.split()
                if split_line[1] == 'f/i=':
                    print(f'Imaginary phonon frequency at {split_line[-2]} meV')
                elif split_line[1] == 'f':
                    candidate = split_line[-2]
                    if minimum_real is None:
                        minimum_real = candidate
                    elif minimum_real > candidate:
                        minimum_real = candidate
            except IndexError:
                    pass
        print(f'Minimum phonon frequency at {minimum_real} meV')
    except IndexError:
        print(f'### Caution, simulation not finished at flag = {flag}')


elif folder_name == 'phonon_spectra':
    for folder in listdir(dir_path):
        # Checking if we are in a valid folder
        
        try:
            NCORE = int(folder)
        except ValueError:
            continue
        
        # Loading the OUTCAR file
        
        try:
            with open(f'{dir_path}/{folder}/OUTCAR', 'r') as OUTCAR_file:
                OUTCAR_lines = OUTCAR_file.readlines()
        except IndexError:
            print(f'### Caution, simulation not finished at NCORE = {NCORE}')
            continue

        # Checking for the lines with imaginary (negative) phonon frequencies
        
        for line in OUTCAR_lines:
            try:
                split_line = line.split()
                if (split_line[0] == 'Elapsed') & (split_line[1] == 'time'):
                    print(f'NCORE = {NCORE} -> Elapsed time = {split_line[-1]}')
            except IndexError:
                continue


elif folder_name == 'band_gap':
    try:
        with open(f'{dir_path}/{flag}/DOSCAR', 'r') as DOSCAR_file:
            DOSCAR_lines = DOSCAR_file.readlines()
        
        enery_states = np.array([line.split() for line in DOSCAR_lines if len(line.split()) == 3], dtype=float)
        
        fermi_energy = float(DOSCAR_lines[5].split()[3])
        fermi_idx = np.argmin(np.abs(enery_states[:, 0] - fermi_energy))
        same_DOS = np.where(enery_states[:, 2] == enery_states[fermi_idx, 2])[0]
        band_gap = enery_states[same_DOS[-1]+1, 0] - enery_states[same_DOS[0], 0]
        
        print(f'Band gap: {band_gap}, Valence band: {enery_states[same_DOS[0], 0]}')
    except FileNotFoundError:
        print(f'### Caution, simulation not finished')


elif (folder_name == 'energy') or (folder_name == 'consistent_energy'):
    OSZICAR_path = f'{element}/absorption_spectra/{flag}/OSZICAR'
    print(OSZICAR_path)
    with open(OSZICAR_path, 'r') as OSZICAR_file:
        OSZICAR_lines = OSZICAR_file.readlines()
    
    energy_line = OSZICAR_lines[-2].split()
    for E0_index in range(len(energy_line)):
        if energy_line[E0_index] == 'E0=':
            E0_value = energy_line[E0_index+1]
            break
    
    #print(f'Energy: {E0_value}')
    print(f'{element} {E0_value}')


elif folder_name == 'absorption_spectra':
    try:
        absorption_path = f'{dir_path}/{flag}/ABSORPTION.dat'
        if not path.exists(absorption_path):
            current_dir = getcwd()
            chdir(f'{dir_path}/{flag}')
            system(f'echo -e "711\n1" | ~/vaspkit.1.3.5/bin/vaspkit')
            chdir(f'{current_dir}')

        absorption_data = np.loadtxt(absorption_path)

        visible_eV = 3.26

        visible_index = np.where(absorption_data[:, 0] >= visible_eV)[0][0]
        
        absorption = np.mean(absorption_data[visible_index, 1:4])

        print(f'Absorption: {absorption}')
    except FileNotFoundError:
        print(f'### Caution, simulation not finished')
