import streamlit as st
import spacy
from spacy import displacy

# Load my trained NER model MedEntity
output_dir = "/app/model-best"
nlp_loaded = spacy.load(output_dir)

#  colors for each entity type
colors = {
    "CHEBI": "#F67DE3",
    "CL": "#7DF6D9",
    "MONDO": "#a6e22d",
    "GO_BP": "#FF5733",
    "GO_CC": "#33FF57",
    "GO_MF": "#5733FF",
    "MOP": "#33A1FF",
    "NCBITAXON": "#A133FF",
    "PR": "#FFD033",
    "SO": "#33FFA1",
    "UBERON": "#FF23A1"
}

#  the Streamlit app
def main():
    #  title and description
    st.title("MedEntity")
    st.title("Fachpraktikum CIE - Fernuni-Hagen")
    st.write("This model MedEntity is trained from scratch using (CRAFT) Corpus")
    
    st.write("Enter a sentence to extract named entities.")

    #  user input
    sentence = st.text_input("Enter a sentence:")

    # Process the input sentence with the NER model
    if st.button("Extract Entities"):
        doc = nlp_loaded(sentence)
        
        # Display the whole text sentence with entities highlighted
        html = displacy.render(doc, style="ent", page=False, options={"colors": colors})
        html = html.replace("\n", " ")  # Remove newlines
        st.write(html, unsafe_allow_html=True)



    # Display the ontology labels
    st.write("Reference Labels for Biomedical Terminology Ontologies:")
    st.write("- CHEBI: Chemical Entities of Biological Interest")
    st.write("- CL: Cell Ontology")
    st.write("- GO CC: Gene Ontology for Cellular Component")
    st.write("- GO BP: Gene Ontology for Biological Process")
    st.write("- GO MF: Gene Ontology for Molecular Function")
    st.write("- MOP: Molecular Process Ontology")
    st.write("- NCBITAXON: NCBI Taxonomy")
    st.write("- PR: Protein Ontology")
    st.write("- SO: Sequence Ontology")
    st.write("- UBERON: UBERON Anatomy Ontology")

if __name__ == "__main__":
    main()

