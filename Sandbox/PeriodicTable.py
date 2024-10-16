import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

periodic_table = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "atomic_weight": 1.008, "group": "Nonmetals"},
    "He": {"name": "Helium", "atomic_number": 2, "atomic_weight": 4.002602, "group": "Noble gases"},
    "Li": {"name": "Lithium", "atomic_number": 3, "atomic_weight": 6.94, "group": "Alkali metals"},
    "Be": {"name": "Beryllium", "atomic_number": 4, "atomic_weight": 9.0122, "group": "Alkaline earth metals"},
    "B": {"name": "Boron", "atomic_number": 5, "atomic_weight": 10.81, "group": "Metalloids"},
    "C": {"name": "Carbon", "atomic_number": 6, "atomic_weight": 12.011, "group": "Nonmetals"},
    "N": {"name": "Nitrogen", "atomic_number": 7, "atomic_weight": 14.007, "group": "Nonmetals"},
    "O": {"name": "Oxygen", "atomic_number": 8, "atomic_weight": 15.999, "group": "Nonmetals"},
    "F": {"name": "Fluorine", "atomic_number": 9, "atomic_weight": 18.998, "group": "Halogens"},
    "Ne": {"name": "Neon", "atomic_number": 10, "atomic_weight": 20.1797, "group": "Noble gases"},
    "Na": {"name": "Sodium", "atomic_number": 11, "atomic_weight": 22.989769, "group": "Alkali metals"},
    "Mg": {"name": "Magnesium", "atomic_number": 12, "atomic_weight": 24.305, "group": "Alkaline earth metals"},
    "Al": {"name": "Aluminum", "atomic_number": 13, "atomic_weight": 26.981538, "group": "Post-transition metals"},
    "Si": {"name": "Silicon", "atomic_number": 14, "atomic_weight": 28.085, "group": "Metalloids"},
    "P": {"name": "Phosphorus", "atomic_number": 15, "atomic_weight": 30.973762, "group": "Nonmetals"},
    "S": {"name": "Sulfur", "atomic_number": 16, "atomic_weight": 32.06, "group": "Nonmetals"},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "atomic_weight": 35.45, "group": "Halogens"},
    "Ar": {"name": "Argon", "atomic_number": 18, "atomic_weight": 39.948, "group": "Noble gases"},
    "K": {"name": "Potassium", "atomic_number": 19, "atomic_weight": 39.098, "group": "Alkali metals"},
    "Ca": {"name": "Calcium", "atomic_number": 20, "atomic_weight": 40.078, "group": "Alkaline earth metals"},
    "Sc": {"name": "Scandium", "atomic_number": 21, "atomic_weight": 44.955908, "group": "Transition metals"},
    "Ti": {"name": "Titanium", "atomic_number": 22, "atomic_weight": 47.867, "group": "Transition metals"},
    "V": {"name": "Vanadium", "atomic_number": 23, "atomic_weight": 50.9415, "group": "Transition metals"},
    "Cr": {"name": "Chromium", "atomic_number": 24, "atomic_weight": 51.9961, "group": "Transition metals"},
    "Mn": {"name": "Manganese", "atomic_number": 25, "atomic_weight": 54.938044, "group": "Transition metals"},
    "Fe": {"name": "Iron", "atomic_number": 26, "atomic_weight": 55.845, "group": "Transition metals"},
    "Co": {"name": "Cobalt", "atomic_number": 27, "atomic_weight": 58.933194, "group": "Transition metals"},
    "Ni": {"name": "Nickel", "atomic_number": 28, "atomic_weight": 58.933194, "group": "Transition metals"},
    "Cu": {"name": "Copper", "atomic_number": 29, "atomic_weight": 63.546, "group": "Transition metals"},
    "Zn": {"name": "Zinc", "atomic_number": 30, "atomic_weight": 65.38, "group": "Transition metals"},
    "Ga": {"name": "Gallium", "atomic_number": 31, "atomic_weight": 69.723, "group": "Post-transition metals"},
    "Ge": {"name": "Germanium", "atomic_number": 32, "atomic_weight": 72.630, "group": "Metalloids"},
    "As": {"name": "Arsenic", "atomic_number": 33, "atomic_weight": 74.921595, "group": "Metalloids"},
    "Se": {"name": "Selenium", "atomic_number": 34, "atomic_weight": 78.971, "group": "Nonmetals"},
    "Br": {"name": "Bromine", "atomic_number": 35, "atomic_weight": 79.904, "group": "Halogens"},
    "Kr": {"name": "Krypton", "atomic_number": 36, "atomic_weight": 83.798, "group": "Noble gases"},
    "Rb": {"name": "Rubidium", "atomic_number": 37, "atomic_weight": 85.4678, "group": "Alkali metals"},
    "Sr": {"name": "Strontium", "atomic_number": 38, "atomic_weight": 87.621, "group": "Alkaline earth metals"},
    "Y": {"name": "Yttrium", "atomic_number": 39, "atomic_weight": 88.90584, "group": "Transition metals"},
    "Zr": {"name": "Zirconium", "atomic_number": 40, "atomic_weight": 91.224, "group": "Transition metals"},
    "Nb": {"name": "Niobium", "atomic_number": 41, "atomic_weight": 92.90637, "group": "Transition metals"},
    "Mo": {"name": "Molybdenum", "atomic_number": 42, "atomic_weight": 95.95, "group": "Transition metals"},
    "Tc": {"name": "Technetium", "atomic_number": 43, "atomic_weight": 98, "group": "Transition metals"},
    "Ru": {"name": "Ruthenium", "atomic_number": 44, "atomic_weight": 101.07, "group": "Transition metals"},
    "Rh": {"name": "Rhodium", "atomic_number": 45, "atomic_weight": 102.90550, "group": "Transition metals"},
    "Pd": {"name": "Palladium", "atomic_number": 46, "atomic_weight": 106.42, "group": "Transition metals"},
    "Ag": {"name": "Silver", "atomic_number": 47, "atomic_weight": 107.8682, "group": "Transition metals"},
    "Cd": {"name": "Cadmium", "atomic_number": 48, "atomic_weight": 112.414, "group": "Post-transition metals"},
    "In": {"name": "Indium", "atomic_number": 49, "atomic_weight": 114.818, "group": "Post-transition metals"},
    "Sn": {"name": "Tin", "atomic_number": 50, "atomic_weight": 118.710, "group": "Post-transition metals"},
    "Sb": {"name": "Antimony", "atomic_number": 51, "atomic_weight": 121.760, "group": "Metalloids"},
    "Te": {"name": "Tellurium", "atomic_number": 52, "atomic_weight": 127.60, "group": "Metalloids"},
    "I": {"name": "Iodine", "atomic_number": 53, "atomic_weight": 126.90447, "group": "Halogens"},
    "Xe": {"name": "Xenon", "atomic_number": 54, "atomic_weight": 131.293, "group": "Noble gases"},
    "Cs": {"name": "Cesium", "atomic_number": 55, "atomic_weight": 132.90545196, "group": "Alkali metals"},
    "Ba": {"name": "Barium", "atomic_number": 56, "atomic_weight": 137.327, "group": "Alkaline earth metals"},
    "La": {"name": "Lanthanum", "atomic_number": 57, "atomic_weight": 138.90547, "group": "Lanthanides"},
    "Ce": {"name": "Cerium", "atomic_number": 58, "atomic_weight": 140.116, "group": "Lanthanides"},
    "Pr": {"name": "Praseodymium", "atomic_number": 59, "atomic_weight": 140.90766, "group": "Lanthanides"},
    "Nd": {"name": "Neodymium", "atomic_number": 60, "atomic_weight": 144.242, "group": "Lanthanides"},
    "Pm": {"name": "Promethium", "atomic_number": 61, "atomic_weight": 145, "group": "Lanthanides"},
    "Sm": {"name": "Samarium", "atomic_number": 62, "atomic_weight": 150.36, "group": "Lanthanides"},
    "Eu": {"name": "Europium", "atomic_number": 63, "atomic_weight": 151.964, "group": "Lanthanides"},
    "Gd": {"name": "Gadolinium", "atomic_number": 64, "atomic_weight": 157.25, "group": "Lanthanides"},
    "Tb": {"name": "Terbium", "atomic_number": 65, "atomic_weight": 158.92535, "group": "Lanthanides"},
    "Dy": {"name": "Dysprosium", "atomic_number": 66, "atomic_weight": 162.500, "group": "Lanthanides"},
    "Ho": {"name": "Holmium", "atomic_number": 67, "atomic_weight": 164.93033, "group": "Lanthanides"},
    "Er": {"name": "Erbium", "atomic_number": 68, "atomic_weight": 167.259, "group": "Lanthanides"},
    "Tm": {"name": "Thulium", "atomic_number": 69, "atomic_weight": 168.93422, "group": "Lanthanides"},
    "Yb": {"name": "Ytterbium", "atomic_number": 70, "atomic_weight": 173.04, "group": "Lanthanides"},
    "Lu": {"name": "Lutetium", "atomic_number": 71, "atomic_weight": 174.9668, "group": "Lanthanides"},
    "Hf": {"name": "Hafnium", "atomic_number": 72, "atomic_weight": 178.49, "group": "Transition metals"},
    "Ta": {"name": "Tantalum", "atomic_number": 73, "atomic_weight": 180.94788, "group": "Transition metals"},
    "W": {"name": "Tungsten", "atomic_number": 74, "atomic_weight": 183.84, "group": "Transition metals"},
    "Re": {"name": "Rhenium", "atomic_number": 75, "atomic_weight": 186.207, "group": "Transition metals"},
    "Os": {"name": "Osmium", "atomic_number": 76, "atomic_weight": 190.23, "group": "Transition metals"},
    "Ir": {"name": "Iridium", "atomic_number": 77, "atomic_weight": 192.217, "group": "Transition metals"},
    "Pt": {"name": "Platinum", "atomic_number": 78, "atomic_weight": 195.084, "group": "Transition metals"},
    "Au": {"name": "Gold", "atomic_number": 79, "atomic_weight": 196.966569, "group": "Transition metals"},
    "Hg": {"name": "Mercury", "atomic_number": 80, "atomic_weight": 200.592, "group": "Transition metals"},
    "Tl": {"name": "Thallium", "atomic_number": 81, "atomic_weight": 204.38, "group": "Post-transition metals"},
    "Pb": {"name": "Lead", "atomic_number": 82, "atomic_weight": 207.2, "group": "Post-transition metals"},
    "Bi": {"name": "Bismuth", "atomic_number": 83, "atomic_weight": 208.98040, "group": "Post-transition metals"},
    "Po": {"name": "Polonium", "atomic_number": 84, "atomic_weight": 209, "group": "Metalloids"},
    "At": {"name": "Astatine", "atomic_number": 85, "atomic_weight": 210, "group": "Halogens"},
    "Rn": {"name": "Radon", "atomic_number": 86, "atomic_weight": 222, "group": "Noble gases"},
    "Fr": {"name": "Francium", "atomic_number": 87, "atomic_weight": 223, "group": "Alkali metals"},
    "Ra": {"name": "Radium", "atomic_number": 88, "atomic_weight": 226, "group": "Alkaline earth metals"},
    "Ac": {"name": "Actinium", "atomic_number": 89, "atomic_weight": 227, "group": "Actinides"},
    "Th": {"name": "Thorium", "atomic_number": 90, "atomic_weight": 232.0377, "group": "Actinides"},
    "Pa": {"name": "Protactinium", "atomic_number": 91, "atomic_weight": 231.03588, "group": "Actinides"},
    "U": {"name": "Uranium", "atomic_number": 92, "atomic_weight": 238.02891, "group": "Actinides"},
    "Np": {"name": "Neptunium", "atomic_number": 93, "atomic_weight": 237, "group": "Actinides"},
    "Pu": {"name": "Plutonium", "atomic_number": 94, "atomic_weight": 244, "group": "Actinides"},
    "Am": {"name": "Americium", "atomic_number": 95, "atomic_weight": 243, "group": "Actinides"},
    "Cm": {"name": "Curium", "atomic_number": 96, "atomic_weight": 247, "group": "Actinides"},
    "Bk": {"name": "Berkelium", "atomic_number": 97, "atomic_weight": 247, "group": "Actinides"},
    "Cf": {"name": "Californium", "atomic_number": 98, "atomic_weight": 251, "group": "Actinides"},
    "Es": {"name": "Einsteinium", "atomic_number": 99, "atomic_weight": 252, "group": "Actinides"},
    "Fm": {"name": "Fermium", "atomic_number": 100, "atomic_weight": 257, "group": "Actinides"},
    "Md": {"name": "Mendelevium", "atomic_number": 101, "atomic_weight": 258, "group": "Actinides"},
    "No": {"name": "Nobelium", "atomic_number": 102, "atomic_weight": 259, "group": "Actinides"},
    "Lr": {"name": "Lawrencium", "atomic_number": 103, "atomic_weight": 262, "group": "Actinides"},
    "Rf": {"name": "Rutherfordium", "atomic_number": 104, "atomic_weight": 267, "group": "Transition metals"},
    "Db": {"name": "Dubnium", "atomic_number": 105, "atomic_weight": 268, "group": "Transition metals"},
    "Sg": {"name": "Seaborgium", "atomic_number": 106, "atomic_weight": 271, "group": "Transition metals"},
    "Bh": {"name": "Bohrium", "atomic_number": 107, "atomic_weight": 270, "group": "Transition metals"},
    "Hs": {"name": "Hassium", "atomic_number": 108, "atomic_weight": 277, "group": "Transition metals"},
    "Mt": {"name": "Meitnerium", "atomic_number": 109, "atomic_weight": 278, "group": "Transition metals"},
    "Ds": {"name": "Darmstadtium", "atomic_number": 110, "atomic_weight": 281, "group": "Transition metals"},
    "Rg": {"name": "Roentgenium", "atomic_number": 111, "atomic_weight": 282, "group": "Transition metals"},
    "Cn": {"name": "Copernicium", "atomic_number": 112, "atomic_weight": 285, "group": "Post-transition metals"},
    "Nh": {"name": "Nihonium", "atomic_number": 113, "atomic_weight": 286, "group": "Post-transition metals"},
    "Fl": {"name": "Flerovium", "atomic_number": 114, "atomic_weight": 289, "group": "Post-transition metals"},
    "Mc": {"name": "Moscovium", "atomic_number": 115, "atomic_weight": 288, "group": "Post-transition metals"},
    "Lv": {"name": "Livermorium", "atomic_number": 116, "atomic_weight": 293, "group": "Post-transition metals"},
    "Ts": {"name": "Tennessine", "atomic_number": 117, "atomic_weight": 294, "group": "Halogens"},
    "Og": {"name": "Oganesson", "atomic_number": 118, "atomic_weight": 294, "group": "Noble gases"},
}

def display_element_info():
    symbol = symbol_entry.get()
    element = periodic_table.get(symbol)
    if element:
        info = f"{element['name']} (Symbol: {symbol}, Atomic Number: {element['atomic_number']}, Atomic Weight: {element['atomic_weight']}, Group: {element['group']})"
    else:
        info = "Element not found."
    
    messagebox.showinfo("Element Information", info)

# Create the main window
root = tk.Tk()
root.title("Periodic Table")

# Load and display the periodic table image
try:
    img = Image.open("periodic_table.png")  # Load the image
    img = img.resize((500, 300), Image.LANCZOS)  # Resize the image (using LANCZOS for high-quality downsampling)
    periodic_table_image = ImageTk.PhotoImage(img)  # Create a PhotoImage
    image_label = tk.Label(root, image=periodic_table_image)  # Create a label for the image
    image_label.pack(pady=10)  # Place the image label in the window
except Exception as e:
    print(f"Error loading image: {e}")

# Create and place a label
label = tk.Label(root, text="Enter Element Symbol:")
label.pack(pady=10)

# Create and place an entry box
symbol_entry = tk.Entry(root)
symbol_entry.pack(pady=10)

# Create and place a button
info_button = tk.Button(root, text="Get Info", command=display_element_info)
info_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()