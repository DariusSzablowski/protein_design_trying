from Bio import PDB
from Bio.PDB import Model, Chain, Residue

# Load the PDB structure
parser = PDB.PDBParser(QUIET=True)  # QUIET suppresses warnings for better clarity
structure = parser.get_structure('protein', './6aru.pdb')

# Specify the chain and residue range to extract
chain_id = 'A'
start_residue = 320
end_residue = 494

# Create a new structure to store the filtered residues and non-standard groups
io = PDB.PDBIO()
model = structure[0]  # Assuming we're dealing with the first model

# Create a new chain to store the selected residues and HETATMs
selected_chain = Chain.Chain(chain_id)

# Define common carbohydrate and aminoglycoside residue names
carbohydrate_residues = {"NAG", "MAN", "BMA", "GLC", "FUC", "GAL", "XYS", "SIA", "NDG"}  # Extend as needed
aminoglycoside_residues = {"KAN", "GEN", "NEO", "TOB", "AMI"}  # Example aminoglycosides

# Extract residues 320 to 494 from the chain
source_chain = model[chain_id]
for residue in source_chain:
    residue_id = residue.get_id()[1]  # Extracts the residue number (ignores insertion code)
    if start_residue <= residue_id <= end_residue:
        selected_chain.add(residue.copy())

# Keep track of added residues to prevent duplicates
added_residues = set()

# Exclusion criteria for specific residues (e.g., NAG 310)
exclude_residue = ("NAG", 301, " ")

# Extract HETATM residues (carbohydrates and aminoglycosides)
for chain in model:
    for residue in chain:
        if residue.id[0].startswith('H_'):  # Check if the residue is a HETATM
            residue_key = (residue.resname, residue.id[1], residue.id[2])  # (name, sequence number, insertion code)
            if (residue.resname in carbohydrate_residues or residue.resname in aminoglycoside_residues) and residue_key != exclude_residue:
                if residue_key not in added_residues:
                    selected_chain.add(residue.copy())
                    added_residues.add(residue_key)

# Add the selected chain to a new model to save
new_model = Model.Model(0)
new_model.add(selected_chain)

# Save the modified structure to a new PDB file
io.set_structure(new_model)
io.save('./chain_A_residues_320_494_with_carbohydrates_excluding_NAG_310.pdb')
