# Design Approaches -- Second round of the Adaptyv Round 2 -- Hackathon/Challenge (https://www.adaptyvbio.com/blog/po102)

## >>> Design 1:  top_binder_1
This design was generated based on the top protein-binder generated and ranked by Bindcraft, described in (Pacesa et al. 2024). The specific Notebook used was: https://colab.research.google.com/github/martinpacesa/BindCraft/blob/main/notebooks/BindCraft.ipynb.

## >>> Design 2: ggggs_3_linked_top_binders_1_and_2
This design was generated based on the two top protein-binders generated by Bindcraft.
=> And then linked with a (Gly4Ser)3-Linker. (amino acid sequence of the linker = GGGGSGGGGSGGGGS)
// This linker was chosen as glycine-serine linkers are commonly used in the rational design of fusion proteins.
// The particular advantage that they add is a high degree of flexibility between two fused protein as opposed to different more rigid possible linkers.

This design decision was made based on the fact that there was the heuristic that if you linked two strongly binding proteins together into one protein-constructs you might possibly create a protein with even more superior binding kinetics. Of course this is more a hypothesis that remains to be evaluated, if you decide on evaluating this or similar designs in the lab.
Furthermore, it is of course possible that linking two protein binders to each other could decrease the ability of both these binder to bind to EGFR and or to fold as intended/simulated.
On the other hand this represents possibly unique approach that holds potential. Should any two EGFR-proteins be close to each other in the Biolayer when the interferometry assay is performed two smartly linked binding proteins (i.e. their exact binding surface is not obstructed by the other fused protein) could theoretically possibly even inhibit two EGFR-molecules at the same time. In this theoretical scenario this fused protein could be superior to non-fused binders.

The following designs offer a few spins on these linked constructs, because there is the possibility that binding is improved by linking the constructs in a different orientation. (Of course not all orientations were tried out because of the limited number of designs one is allowed to enter.)

Furthermore, the two unsupervised approaches mentioned in your post (Hie et al., 2023 and Shanker et al., 2024) were also tried out on top of the Bindcraft-Simulation + linking of the top scoring proteins.

## >>> Design 3: ggggs_3_linked_top_binders_1_rev_and_2_rev
The same two binder-proteins developed against EGFR, this time with their amino-acid-sequences reversed and then linked.

## >>> Design 4: ggggs_3_linked_top_binders_1_and_2_efficiently_evolved
This design was generated based on the two top protein-binders generated by Bindcraft.
=> These were then fed into the (Hie et al., 2023) tool (Efficient evolution from general protein language models) in order to make the proteins be more similar to a human antibody.
=> Three changes were proposed by the tool for top_2_binder, none were proposed for the top_1_binder.
=> And then linked with a (Gly4Ser)3-Linker. (amino acid sequence of the linker = GGGGSGGGGSGGGGS)

## >>> Design 5: ggggs_3_linked_top_binders_1_and_2_efficiently_evolved_and_sapiens_evolved
This design was generated based on the two top protein-binders generated by Bindcraft.
=> These were then fed into the (Hie et al., 2023) tool (Efficient evolution from general protein language models) in order to make the proteins be more similar to a human antibody.
=> Three changes were proposed by the tool for top_2_binder, none were proposed for the top_1_binder.
=> Then 10 random positions in the amino acid-sequence were masked (with a ‚*‘) and then replaced by the amino-acids suggested by the Merck/Sapiens model, with the ‚H‘ option, to make it more similar to an antibody heavy chain.
=> And then linked with a (Gly4Ser)3-Linker. (amino acid sequence of the linker = GGGGSGGGGSGGGGS)

---

# References

Hie, B. L., Shanker, V. R., Xu, D., Bruun, T. U. J., Weidenbacher, P. A., Tang, S., Wu, W., Pak, J. E., & Kim, P. S. (2023). Efficient evolution of human antibodies from general protein language models. In Nature Biotechnology (Vol. 42, Issue 2, pp. 275–283). Springer Science and Business Media LLC. https://doi.org/10.1038/s41587-023-01763-2

Shanker, V. R., Bruun, T. U. J., Hie, B. L., & Kim, P. S. (2024). Unsupervised evolution of protein and antibody complexes with a structure-informed language model. In Science (Vol. 385, Issue 6704, pp. 46–53). American Association for the Advancement of Science (AAAS). https://doi.org/10.1126/science.adk8946

Pacesa, M., Nickel, L., Schmidt, J., Pyatova, E., Schellhaas, C., Kissling, L., Alcaraz-Serna, A., Cho, Y., Ghamary, K. H., Vinué, L., Yachnin, B. J., Wollacott, A. M., Buckley, S., Georgeon, S., Goverde, C. A., Hatzopoulos, G. N., Gönczy, P., Muller, Y. D., Schwank, G., … Correia, B. E. (2024). BindCraft: one-shot design of functional protein binders. Cold Spring Harbor Laboratory. https://doi.org/10.1101/2024.09.30.615802
