Attached you will find two csvs, that when combined, gives all the "diagnoses" codes experienced in all encounters for a particular patient.  "patient2encounters.csv" (P2E.csv) and "encounter2codes.csv" (E2C.csv).  P2E.csv contains all the encounters, identified by "encounter_id", a particular patient identified by "ssn" has had.  (Encounters are visits to a healthcare office).  E2C.sv contains all the codes (i.e. ICD10 codes for diagnoses, procedure, etc.), identified by "icd10_code", for a particular encounter identified by "encounter_id".  In other words, "encounter_id" is what one would "jon" the two csvs on.  Additional reminder: the values in icd10_code have no connection to reality, so it's not fruitful to look up what a particular icd10 code means.


The task is to come up with something yielding "insight".  That could be in the form of predictive/prescriptive models, retrospective analysis, etc.  For example, one could try to asnwer questions like:
1) Procedures the patient should be having that they are not?
2) Excess care?
3) Procedure code groupings?

There are no correct answers.  Pick a particular problem and try to solve it.

There are 3 guidelines:
A) Python is heavily preferred.  Please feel free to use libraries!
B) Efforts needs to be repeatable, minimize future struggles, and enable further discovery.  It needs to work from the command line.
C) Whatever solution is devised needs to work during "apply" time.  For example, a ML-based model requires saving after training, and reloading when it's applying.

Hence, try to wrap up your solution such that it can effortlessly work on other data resembling the input csvs.  Also, please "zip" or "tar" your solution up such that it can make it past the email filters :)
